#!/usr/bin/env python3
"""Small HTTP service used only by the portfolio monitoring lab."""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class StatusHandler(BaseHTTPRequestHandler):
    server_version = "PortfolioStatusService/1.0"

    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        if self.path != "/health":
            self._send_json(404, {"status": "not_found"})
            return

        unhealthy = os.getenv("FORCE_UNHEALTHY", "0") == "1"
        status_code = 503 if unhealthy else 200
        payload = {"status": "degraded" if unhealthy else "ok"}
        self._send_json(status_code, payload)

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"service_log remote={self.client_address[0]} message={fmt % args}")

    def _send_json(self, status_code: int, payload: dict[str, str]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", "8080"))
    server = ThreadingHTTPServer((host, port), StatusHandler)
    print(f"service_start host={host} port={port}")
    server.serve_forever()


if __name__ == "__main__":
    main()

