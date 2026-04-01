"""Configuration for integration tests against a live Duco box."""

from __future__ import annotations

import os

import aiohttp
import pytest

from duco.client import DucoClient


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--duco-host",
        action="store",
        default=os.environ.get("DUCO_HOST", "192.168.3.94"),
        help="IP address or hostname of the Duco box (default: 192.168.3.94)",
    )


@pytest.fixture(scope="session")
def duco_host(request: pytest.FixtureRequest) -> str:
    return str(request.config.getoption("--duco-host"))


@pytest.fixture
async def live_client(duco_host: str) -> DucoClient:  # type: ignore[misc]
    """DucoClient connected to the real box."""
    async with aiohttp.ClientSession() as session:
        yield DucoClient(session=session, host=duco_host)
