# Day 34 Script: Advanced Concurrency Patterns Demo
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def cpu_bound(n):
    return sum(i * i for i in range(n))

async def main():
    # I/O-bound: asyncio
    print('Starting asyncio task...')
    await asyncio.sleep(1)
    
    # CPU-bound: ProcessPool
    with ProcessPoolExecutor() as pool:
        result = await asyncio.get_running_loop().run_in_executor(
            pool, cpu_bound, 10**7)
        print(f'CPU-bound result: {result}')

# asyncio.run(main())
