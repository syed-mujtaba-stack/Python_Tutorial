# Day 8: Async Programming in Python

Async programming allows you to write concurrent code using the `asyncio` library, `async` and `await` keywords. Great for I/O-bound tasks (networking, APIs).

**Basic Example:**
```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
```

**Multiple Tasks:**
```python
async def fetch_data():
    await asyncio.sleep(2)
    return 'data'

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

---
**Pro Tip:**
Use async for high-performance networking, web scraping, and API clients.
