# Day 34 Solution: Advanced Concurrency Patterns
import asyncio

async def worker(sem, name, queue):
    while True:
        async with sem:
            task = await queue.get()
            print(f'{name} processing {task}')
            await asyncio.sleep(1)
            queue.task_done()

async def main():
    sem = asyncio.Semaphore(3)  # Max 3 concurrent tasks
    queue = asyncio.Queue()
    
    # Add tasks
    for i in range(10):
        await queue.put(f'Task-{i}')
    
    # Start workers
    workers = [
        asyncio.create_task(worker(sem, f'Worker-{i}', queue))
        for i in range(5)  # 5 workers, but only 3 run concurrently
    ]
    
    await queue.join()
    for w in workers:
        w.cancel()

asyncio.run(main())
