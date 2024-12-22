import asyncio
import time


async def async_sleep(n):
    print('sleeping',n)
    await asyncio.sleep(5)
    print('sleeping ends',n)

async def print_hello():
    print('Hello')

async def main():
    start_time = time.time()
    task = asyncio.create_task(async_sleep(1)) #---Created a task so that it can run paralelly
    await async_sleep(2)
    await task #---Awaiting the execution of the task
    await print_hello()
    end_time = time.time()
    print('Total Time ',(end_time-start_time))

    #-- Here we still have the problem with the print_hello which has to wait for both the async_sleep to be executed



if __name__ == '__main__':
    asyncio.run(main())