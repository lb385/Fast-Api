import os
import socket
import subprocess
import sys
import time
from collections.abc import Iterator
from urllib.parse import urlparse

import pytest


def _is_port_open(host: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        return sock.connect_ex((host, port)) == 0


@pytest.fixture(scope="session", autouse=True)
def ensure_app_running() -> Iterator[None]:
    base_url = os.getenv("E2E_BASE_URL", "http://127.0.0.1:8000")
    parsed = urlparse(base_url)
    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or 8000

    # If already running (e.g., CI started it), do not spawn another process.
    if _is_port_open(host, port):
        yield
        return

    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "app.main:app",
            "--host",
            host,
            "--port",
            str(port),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    try:
        for _ in range(30):
            if _is_port_open(host, port):
                break
            time.sleep(0.3)
        else:
            raise RuntimeError("FastAPI server did not start for E2E tests")

        yield
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
