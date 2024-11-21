from fastapi import FastAPI
from game_manager import GameManager
import socketio
# sio = socketio.AsyncServer(
#     async_mode = 'asgi',
#     cors_allowed_origins = []
# )
#Fast API application
app = FastAPI()
#Socket io (sio) create a Socket.IO server
sio=socketio.AsyncServer(cors_allowed_origins='*',async_mode='asgi')
gamemanager =  GameManager()

# @app.get('/')
# async def home():
#     return {'message': "hello"}

@sio.event
async def connect(sid, environ):
    print(sid)
    # gamemanager.connect(sid)

@sio.event
async def disconnect(sid):
    # gamemanager.disconnect(sid)

@sio.event
async def messages(sid, data):
    # gamemanager.my_message(sid, data)


