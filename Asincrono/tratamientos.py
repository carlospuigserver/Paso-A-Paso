import asyncio
import aiohttp
from urllib.parse import urlparse
from functools import partial
import sys
from os import sep
from sys import stderr
from bs4 import BeautifulSoup
from timeit import timeit
from descargar_y_parsear import wget
from ejecutor import download
from descargar_y_parsear import get_images_src_from_html
from descargar_y_parsear import get_uri_from_images_src


async def get_images(session, page_uri):  
    html = await wget(session, page_uri)  
    if not html:  
        print("Error: no se ha encontrado ninguna imagen", 
sys.stderr)  
        return None  
    images_src_gen = get_images_src_from_html(html)  
    images_uri_gen = get_uri_from_images_src(page_uri, 
images_src_gen)  
    async for image_uri in images_uri_gen:  
        print('Descarga de %s' % image_uri)  
        await download(session, image_uri) 

async def main():  
    web_page_uri = 'http://www.formation-python.com/'  
    async with aiohttp.ClientSession() as session:  
        await get_images(session, web_page_uri) 

asyncio.run(main()) 

event_loop = asyncio.get_event_loop()  
event_loop.run_until_complete(main()) 

if __name__ == '__main__':
    print('--- Starting standard download ---')
    web_page_uri = 'http://www.formation-python.com/'
    print(timeit('test()',
                 number=10,
                 setup="from __main__ import test"))
