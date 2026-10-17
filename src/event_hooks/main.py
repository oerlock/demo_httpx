"""Run the demo: send a request with hooks attached and observe the logs.

Usage:
    uv run python -m src.event_hooks.main
"""

import asyncio
import logging

from src.event_hooks.hooks import build_client

API_URL = "https://httpbin.org/get"


async def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    async with build_client() as client:
        response = await client.get(API_URL)
        response.raise_for_status()


if __name__ == "__main__":
    asyncio.run(main())
