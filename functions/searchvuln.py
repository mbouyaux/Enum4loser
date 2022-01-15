import aiohttp
import asyncio

open_redirect_parameter = ['=http','=https','=www','=/','=//']
def openredirect(home_path,hunt_folder,target_folder,name_folder,attacker_srv):
    path = f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/'
    file_of_vuln_urls = open(path+"redirect")
    for url in file_of_vuln_urls:
        for i in open_redirect_parameter:
            if url.count(i) > 0:
                url = url.split("=")
                url_done = url[0] + "="+attacker_srv
                loop = asyncio.new_event_loop()
                loop.run_until_complete(start(url_done))

async def fetch(URL):
    triggered = []
    async with aiohttp.ClientSession(trust_env=True) as session:
        try:
            async with session.get(URL,allow_redirects=True) as response:
                rep = response.url 
                repcheck = response.real_url
                in_url = str(URL)
                if in_url not in str(rep) and in_url not in str(repcheck):
                    if in_url not in triggered:
                        print("\033[91m[$$$] Open redirect found at : {}\033[0m".format(URL))
                        triggered.append(URL)
        except aiohttp.ClientConnectionError as e:
            pass

async def start(url):
    await fetch(url)