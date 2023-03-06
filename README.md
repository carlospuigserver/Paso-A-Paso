# Paso-A-Paso

El link de este repositorio es: https://github.com/carlospuigserver/Paso-A-Paso.git

He realizado un programa de manera asíncrona, el cual te descarga 5  imágenes  de internet (el número de imágenes puede ser el que quiera), cogiendo urls aleatorias, te hace una carpeta images con las imágenes en formato.png, y te dice cuanto tiempo ha tardado en descargar cada imagen. El código es el siguiente:


```
import os
import random
import asyncio
import aiohttp
import time

async def download_image(session, url):
    try:
        start_time = time.monotonic()
        async with session.get(url) as response:
            content = await response.read()
            filename = f"{url.split('/')[-1]}.png"
            filepath = os.path.join("images", filename)
            with open(filepath, "wb") as file:
                file.write(content)
                end_time = time.monotonic()
                print(f"{filename} downloaded in {end_time - start_time:.2f} seconds")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

async def download_images(num_images):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_images):
            url = f"https://picsum.photos/{random.randint(200, 500)}/{random.randint(200, 500)}"
            task = asyncio.ensure_future(download_image(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    num_images = 5
    if not os.path.exists("images"):
        os.mkdir("images")
    asyncio.run(download_images(num_images))
```

<img width="905" alt="foto1" src="https://user-images.githubusercontent.com/91721643/223157067-4f44b4db-0080-45a4-9c2a-ebf746efe3f9.png">


<img width="847" alt="foto2" src="https://user-images.githubusercontent.com/91721643/223157159-9bccbfa7-d434-407a-b599-203ffce9c1be.png">

<img width="902" alt="foto3" src="https://user-images.githubusercontent.com/91721643/223157221-96269959-9898-4299-b1a2-62d9b26f36fd.png">



