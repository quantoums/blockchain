# An intro to asyncio lib which allows to write asynchronous code.
# asyncio allows us to separate our code into tasks which look like they're running in parallel.

import asyncio
import time


async def greet(name,delay):

    # this allows to sleep for a time delay
    await asyncio.sleep(delay)

    print(f'{name} : I waited {delay} seconnds before saying Hello !')


async def main():
    
    # this create task that can be run concurrently via asyncio.create_task

    task_1 = asyncio.create_task(greet("task_1",3))

    task_2 = asyncio.create_task(greet('task_2',2))

    task_3 = asyncio.create_task(greet('task_3',2))



    start_time = time.time()

    print("0.00s : Program Start")

    await task_1
    await task_2
    await task_3

    print(f'{time.time() -start_time :.2f}s : Program End')

    print(f'\nThe tasks run in "parallel" otherwise the runtime would have been  t1 + t2 + t3 = 7.00s instead of {time.time() -start_time :.2f}s \n')


asyncio.run(main())