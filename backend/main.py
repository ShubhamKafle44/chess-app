from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sockets import sio_app
#Fast API application
app = FastAPI()


app.mount('/', sio_app)



app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True, 
    allow_methods = ['*'],
    allow_headers = ['*'],
)




