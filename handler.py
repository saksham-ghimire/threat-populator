import asyncio
from aysncHttp import asyncGet
from pymemcache.client import base
from pymemcache.exceptions import MemcacheIllegalInputError  # noqa
from parsers import textParser
import time

parsers = {"text":textParser}

client = base.Client(('localhost', 2222))

def populate(data,url) -> None:
    if len(data) == 0:
        return
    else:
        if data[0] != "":
            try:
                client.set(data[0],url,86400)
            except MemcacheIllegalInputError as e:
                # pass
                print(f"[+] Illegal input detected .. \n Key => {data[0]} \n Value => {url} \n Error => {e}")
            except Exception as e:
                # pass
                print(f"[+] Unexpected error {e}")
            populate(data[1:],url)



async def fetchInInterval(params:dict, interval:int) -> None:
    print(f"[+] New coroutine to fetch in interval of {interval} initialized")
    while True:
        datas = await asyncio.gather(*[asyncGet(i["url"],parsers[i["parser"]]) for i in params])
        for i in datas:
            print(f"[+] Now populating for interval {interval}")
            populate(i[0],i[1])
        await asyncio.sleep(interval)


