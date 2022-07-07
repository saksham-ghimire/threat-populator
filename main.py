import asyncio
import yaml 
import threading
from handler import fetchInInterval

def initConfig() -> dict:
    with open("config.yml", "r") as stream:
       config = yaml.safe_load(stream)
    
    return config

    
async def main():
    config = initConfig()
    await asyncio.gather(*[fetchInInterval(i["sources"],i["time"]) for i in config])
    
asyncio.run(main())    
