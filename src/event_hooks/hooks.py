"""Event hooks that log outgoing requests and incoming responses."""

import logging

import httpx

logger = logging.getLogger(__name__)


async def log_request(request):
    """Log the HTTP method and URL before the request is sent."""
    logger.info("Request: %s %s", request.method, request.url)


async def log_response(response):
    """Log the status code and URL after the response is received."""
    logger.info("Response: %s %s", response.status_code, response.url)


def build_client(**kwargs) -> httpx.AsyncClient:
    """Create an httpx.AsyncClient with request/response hooks registered."""
    kwargs.setdefault(
        "event_hooks", {"request": [log_request], "response": [log_response]}
    )
    return httpx.AsyncClient(**kwargs)
