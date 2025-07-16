# Day 21: Advanced Async Patterns (asyncio, trio, async libraries)

Async programming in Python goes beyond basics with advanced patterns, libraries, and best practices for concurrency.

**Advanced asyncio Example:**
```python
import asyncio

async def fetch_data(n):
    await asyncio.sleep(1)
    return f'Data {n}'

async def main():
    results = await asyncio.gather(*(fetch_data(i) for i in range(5)))
    print(results)

asyncio.run(main())
```

**Other async libraries:**
- `trio`: Modern async concurrency
- `aiohttp`: Async HTTP requests
- `aiomysql`, `aioredis`: Async DBs

---
**Pro Tip:**
Use `asyncio.gather`, `asyncio.wait`, and cancellation for robust concurrent workflows.
