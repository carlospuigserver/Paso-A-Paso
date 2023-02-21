import aiohttp
import asyncio



async def main(uri):  
     async with aiohttp.ClientSession() as session:  
        async with session.get(uri) as response:  
            if response.status != 200:  
                return None  
            if response.content_type.startswith("text/"):  
                return await response.text()  
            else:  
                return await response.read()  
  
asyncio.run(main("http://www.formation-python.com/")) 