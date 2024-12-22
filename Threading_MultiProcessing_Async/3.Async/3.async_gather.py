import asyncio
import time


async def async_sleep(n):
    print('sleeping',n)
    await asyncio.sleep(n)
    print('sleeping ends',n)

async def print_hello():
    print('Hello')

async def main():
    start_time = time.time()

    try:
        await asyncio.gather(

            asyncio.wait_for(
            async_sleep(11),10),
            async_sleep(3),
            print_hello(),
        )
    except asyncio.TimeoutError:
        print("Encountered Timeout Error")

    end_time = time.time()
    print('Total Time ',(end_time-start_time))



if __name__ == '__main__':
    asyncio.run(main())