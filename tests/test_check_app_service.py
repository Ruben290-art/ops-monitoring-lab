from __future__ import annotations

import io
import json
import pathlib
import sys
import unittest
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from monitoring.check_app_service import build_check_line  # noqa: E402


class ContextResponse:
    def __init__(self, status: int, payload: dict[str, str]):
        self.status = status
        self._body = json.dumps(payload).encode("utf-8")

    def read(self) -> bytes:
        return self._body

    def __enter__(self) -> "ContextResponse":
        return self

    def __exit__(self, *_args: object) -> None:
        return None


class CheckAppServiceTests(unittest.TestCase):
    @patch("monitoring.check_app_service.urllib.request.urlopen")
    def test_ok_output_is_checkmk_compatible(self, urlopen: MagicMock) -> None:
        urlopen.return_value = ContextResponse(200, {"status": "ok"})

        exit_code, line = build_check_line("http://example.test/health")

        self.assertEqual(exit_code, 0)
        self.assertRegex(line, r'^0 "Portfolio App Health" response_ms=\d+;500;1000;0 ')
        self.assertIn("status=ok", line)

    @patch("monitoring.check_app_service.urllib.request.urlopen")
    def test_http_error_is_critical(self, urlopen: MagicMock) -> None:
        urlopen.side_effect = HTTPError(
            "http://example.test/health", 503, "Unavailable", {}, io.BytesIO()
        )

        exit_code, line = build_check_line("http://example.test/health")

        self.assertEqual(exit_code, 2)
        self.assertEqual(line, '2 "Portfolio App Health" - HTTP error 503')

    @patch("monitoring.check_app_service.urllib.request.urlopen")
    def test_connection_error_is_critical(self, urlopen: MagicMock) -> None:
        urlopen.side_effect = URLError("connection refused")

        exit_code, line = build_check_line("http://example.test/health")

        self.assertEqual(exit_code, 2)
        self.assertIn("Service unreachable", line)

    @patch("monitoring.check_app_service.urllib.request.urlopen")
    def test_invalid_json_is_unknown(self, urlopen: MagicMock) -> None:
        response = ContextResponse(200, {"status": "ok"})
        response._body = b"not-json"
        urlopen.return_value = response

        exit_code, line = build_check_line("http://example.test/health")

        self.assertEqual(exit_code, 3)
        self.assertIn("Invalid response", line)


if __name__ == "__main__":
    unittest.main()

