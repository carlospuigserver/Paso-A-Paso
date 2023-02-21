import asyncio
from urllib.parse import urlparse
import asyncio
from bs4 import BeautifulSoup






async def get_images_src_from_html(html_doc):  
    soup = BeautifulSoup(html_doc, "html.parser")  
    for img in soup.find_all('img'):  
        yield img.get('src')  
        await asyncio.sleep(0.001) 

async def get_uri_from_images_src(base_uri, images_src):  
    """Devuelve una a una cada URI de imagen a descargar"""  
    parsed_base = urlparse(base_uri)  
    async for src in images_src:  
        parsed = urlparse(src)  
        if parsed.netloc == '':  
            path = parsed.path  
            if parsed.query:  
                path += '?' + parsed.query  
            if path[0] != '/':  
                if parsed_base.path == '/':  
                    path = '/' + path  
                else:  
                    path = '/' + '/'.join(parsed_base.path.split('/')[:-1]) + '/' + path  
            yield parsed_base.scheme + '://' + parsed_base.netloc + path  
        else:  
            yield parsed.geturl()  
        await asyncio.sleep(0.001) 