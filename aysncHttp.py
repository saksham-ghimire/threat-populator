import asyncio
import requests

def send_request(url:str) -> bytes:
    try:
        response = requests.get(url,timeout=1)
        return response.content    
    except requests.Timeout:
        print("Timed out")
        return None
    except Exception as e:
        print("Unexpected error", e)
        return None
    
async def asyncGet(url:str, parse) -> list:
    print(f"[+] Fetching data from {url}")
    resp = await asyncio.to_thread(send_request,url)
    if resp == None:
        return []
    resp = parse(resp)
    print(f"[+] Data fetched and returned from {url}")
    return  (resp,url)

