"""Tests for the event hooks example, using a mocked transport."""

import logging

import httpx
import pytest

from src.event_hooks.hooks import build_client, log_request, log_response


def mock_handler(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json={"url": str(request.url)})


def make_client() -> httpx.AsyncClient:
    transport = httpx.MockTransport(mock_handler)
    return build_client(transport=transport)


@pytest.fixture
def capture_logs(caplog):
    caplog.set_level(logging.INFO, logger="src.event_hooks.hooks")
    return caplog


async def test_hooks_execute_in_order():
    # httpx fires request hooks before sending and response hooks after.
    events: list[str] = []

    async def tracking_request(request):
        events.append("request")

    async def tracking_response(response):
        events.append("response")

    transport = httpx.MockTransport(mock_handler)
    async with httpx.AsyncClient(
        transport=transport,
        event_hooks={"request": [tracking_request], "response": [tracking_response]},
    ) as client:
        await client.get("https://example.test/api")

    assert events == ["request", "response"]


async def test_log_request_metadata(capture_logs):
    request = httpx.Request("GET", "https://example.test/api")
    await log_request(request)
    assert "Request: GET https://example.test/api" in capture_logs.messages


async def test_log_response_metadata(capture_logs):
    response = httpx.Response(
        200, json={"ok": True}, request=httpx.Request("GET", "https://example.test/api")
    )
    await log_response(response)
    assert "Response: 200 https://example.test/api" in capture_logs.messages


async def test_build_client_registers_hooks(capture_logs):
    async with make_client() as client:
        assert client.event_hooks["request"] == [log_request]
        assert client.event_hooks["response"] == [log_response]
        await client.get("https://example.test/api")

    assert "Request: GET https://example.test/api" in capture_logs.messages
    assert "Response: 200 https://example.test/api" in capture_logs.messages
