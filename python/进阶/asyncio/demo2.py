import asyncio
import time


async def run_delay(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def run_delay_return(delay, what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"


async def demo_await_coroutinue():
    print(f"started at {time.strftime('%X')}")
    await run_delay(1, "hello")
    await run_delay(2, "world")
    print(f"finished at {time.strftime('%X')}")


async def demo_await_task():
    task1 = asyncio.create_task(run_delay(1, "hello"))
    task2 = asyncio.create_task(run_delay(2, "world"))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


async def demo_await_task_return():
    task1 = asyncio.create_task(run_delay_return(1, "hello"))
    task2 = asyncio.create_task(run_delay_return(2, "world"))
    print(f"started at {time.strftime('%X')}")
    res1 = await task1
    res2 = await task2
    print(f"finished at {time.strftime('%X')}")
    print(res1)
    print(res2)


async def demo_gather_task():
    task1 = asyncio.create_task(run_delay_return(1, "hello"))
    task2 = asyncio.create_task(run_delay_return(2, "world"))
    print(f"started at {time.strftime('%X')}")
    res = await asyncio.gather(task1, task2)
    print(f"finished at {time.strftime('%X')}")
    print(res)


async def demo_gather_coroutinue():
    print(f"started at {time.strftime('%X')}")
    res = await asyncio.gather(
        run_delay_return(1, "hello"), run_delay_return(2, "world")
    )
    print(f"finished at {time.strftime('%X')}")
    print(res)


async def demo_task_list():
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(run_delay_return(1, f"hello-{i}")))
    res = await asyncio.gather(*tasks)
    for r in res:
        print(r)


def callback(future):
    # future: asyncio.Future
    print(f"callback: {future.result()}")


async def demo_callback():
    tasks = []
    for i in range(5):
        task = asyncio.create_task(run_delay_return(1, f"hello-{i}"))
        task.add_done_callback(callback)
        tasks.append(task)
    res = await asyncio.wait(tasks, timeout=5)
    for r in res:
        print(r)


if __name__ == "__main__":
    # asyncio.run(demo_await_coroutinue())
    # asyncio.run(demo_await_task())
    # asyncio.run(demo_await_task_return())
    # asyncio.run(demo_gather_task())
    # asyncio.run(demo_gather_coroutinue())
    # asyncio.run(demo_task_list())
    asyncio.run(demo_callback())
