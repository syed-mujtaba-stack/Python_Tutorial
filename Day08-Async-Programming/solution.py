# Day 8 Solution: Async Programming
import asyncio

async def wait_and_return():
    await asyncio.sleep(2)
    return 'Done waiting!'

async def main():
    msg = await wait_and_return()
    print(msg)

asyncio.run(main())
