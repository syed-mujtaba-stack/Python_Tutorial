# Day 21 Script: Advanced Async Patterns Demo
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()

async def main():
    html = await fetch('https://example.com')
    print('Fetched', len(html), 'characters')

# Requires aiohttp installed
# asyncio.run(main())
