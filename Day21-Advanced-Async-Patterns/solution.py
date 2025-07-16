# Day 21 Solution: Advanced Async Patterns
import asyncio

async def sleeper(n, t):
    await asyncio.sleep(t)
    return f'Slept {t}s for task {n}'

async def main():
    results = await asyncio.gather(
        sleeper(1, 1),
        sleeper(2, 2),
        sleeper(3, 0.5)
    )
    print(results)

asyncio.run(main())
