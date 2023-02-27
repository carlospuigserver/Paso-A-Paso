import asyncio
import aiohttp
from urllib.parse import urlparse
from functools import partial
import sys
from os import sep
from sys import stderr
from bs4 import BeautifulSoup
from timeit import timeit
from descargar import wget


def write_in_file(filename, content):   
    with open(filename, "wb") as f:   
        f.write(content) 

async def download(session, uri):  
    content = await wget(session, uri)  
    if content is None:  
        return None  
    loop = asyncio.get_running_loop()  
    await loop.run_in_executor(None, partial(write_in_file, 
uri.split(sep)[-1], content))  
    return uri 