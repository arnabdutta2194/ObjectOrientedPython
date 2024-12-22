import asyncio

async def async_sleep():
    print('sleeping')
    await asyncio.sleep(5)
    print('sleeping ends')

async def print_hello():
    print('Hello')
    return 'Hello'

async def main():
    await async_sleep()#--- Wait for the task to be executed before giving control back to event loop
    result = await print_hello() 
    print(result)
#--- Above basically works as synchronous program as they are waiting for the execution to end

if __name__ == '__main__':
    asyncio.run(main())