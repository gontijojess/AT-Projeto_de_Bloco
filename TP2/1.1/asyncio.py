import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt

async def download_url(session, url):
    async with session.get(url) as response:
        content = await response.text()
        print(f"Downloaded {url}: {len(content)} bytes")

async def download_all(urls, max_concurrent_downloads):
    semaphore = asyncio.Semaphore(max_concurrent_downloads)

    async def download_with_semaphore(url):
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                await download_url(session, url)

    tasks = [download_with_semaphore(url) for url in urls]
    await asyncio.gather(*tasks)

def measure_download_time(urls, max_downloads=10):
    times = []
    for concurrent_downloads in range(1, max_downloads + 1):
        start_time = time.time()
        asyncio.run(download_all(urls, concurrent_downloads))
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)
        print(f"Concurrent downloads: {concurrent_downloads}, Time: {elapsed_time:.2f} seconds")
    
    plt.plot(range(1, max_downloads + 1), times, marker='o')
    plt.title("Number of Concurrent Downloads vs Execution Time")
    plt.xlabel("Number of Concurrent Downloads")
    plt.ylabel("Time (seconds)")
    plt.savefig('grafico_download_async.png')
    print('Grafico salvo como grafico_download_async.png')

if __name__ == "__main__":
    url_list = [
        "https://www.google.com",
        "https://www.instagram.com",
        "https://www.facebook.com",
        "https://www.infnet.edu.br",
        "https://www.gmail.com"
    ]

    measure_download_time(url_list, max_downloads=8)