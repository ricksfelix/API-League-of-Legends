import uvicorn

from fastapi import FastAPI
from routes import get_images

app = FastAPI()
app.include_router(get_images.router, prefix='/image')


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000
    uvicorn.run(app, host=host, port=port)