# Day 8 Script: Async Programming Demo
import asyncio

async def fetch_url(url):
    print(f'Fetching {url}...')
    await asyncio.sleep(1)
    return f'Data from {url}'

async def main():
    urls = ['a.com', 'b.com', 'c.com']
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print('Results:', results)

asyncio.run(main())
