import asyncio
import requests
import time
import aiohttp


async def get_url_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        
async def get_url_with_requests(url):
    requests.get(url)

async def main():
    urls = ['https://google.com',
            'https://wikipedia.org/wiki/Concurrency',
            'https://python.org',
            'https://pypi.org/project/requests/',
            'https://docs.python.org/3/library/asyncio-task.html',
            'https://www.apple.com',
            'https://www.medium.com/',]
    
    start_time = time.time()
    tasks=[]
    for url in urls:
        tasks.append(asyncio.create_task(
            get_url_with_requests(url)
        ))
    end_time = time.time()
    sync_text_response = await asyncio.gather(*tasks)

    print('Sync Requests took :',(end_time-start_time))


    start_time = time.time()
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(
           get_url_response(url) 
        ))
    async_text_response = await asyncio.gather(*tasks)
    end_time = time.time()



    print('Async Requests took :',(end_time-start_time))

if __name__ == "__main__":
    asyncio.run(main())


    
