#!/usr/bin/env python3
"""Check an HTTP health endpoint and print one Checkmk local-check line."""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

SERVICE_NAME = "Portfolio App Health"


def build_check_line(url: str, timeout: float = 2.0) -> tuple[int, str]:
    """Return process exit code and Checkmk-compatible output line."""
    started = time.monotonic()
    request = urllib.request.Request(url, headers={"User-Agent": "portfolio-monitor/1.0"})

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            response_ms = int((time.monotonic() - started) * 1000)
            payload = json.loads(response.read().decode("utf-8"))
            app_status = payload.get("status", "unknown")

            if response.status == 200 and app_status == "ok":
                return 0, (
                    f'0 "{SERVICE_NAME}" response_ms={response_ms};500;1000;0 '
                    f"Service reachable, status={app_status}"
                )

            return 2, (
                f'2 "{SERVICE_NAME}" response_ms={response_ms};500;1000;0 '
                f"Unexpected health response, http={response.status}, status={app_status}"
            )
    except urllib.error.HTTPError as error:
        return 2, f'2 "{SERVICE_NAME}" - HTTP error {error.code}'
    except (urllib.error.URLError, TimeoutError) as error:
        return 2, f'2 "{SERVICE_NAME}" - Service unreachable: {error.reason}'
    except (json.JSONDecodeError, UnicodeDecodeError, KeyError) as error:
        return 3, f'3 "{SERVICE_NAME}" - Invalid response: {type(error).__name__}'
    except Exception as error:  # Defensive boundary for an agent check.
        return 3, f'3 "{SERVICE_NAME}" - Check failed: {type(error).__name__}'


def main() -> int:
    url = os.getenv("APP_HEALTH_URL", "http://127.0.0.1:8080/health")
    timeout = float(os.getenv("APP_CHECK_TIMEOUT", "2.0"))
    exit_code, line = build_check_line(url, timeout)
    print(line)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

