import socketio
from game_manager import GameManager
sio_server = socketio.AsyncServer(
    async_mode = 'asgi',
    cors_allowed_origins = []
)

sio_app = socketio.ASGIApp(
    socketio_server = sio_server, 
    socketio_path='/sockets'
)

gamemanager  = GameManager()


@sio_server.event
async def connect(sid, environ):
    gamemanager.addUser(sid)
    print("attempting to connect")

@sio_server.event
async def disconnect(sid):
    gamemanager.removeUser(sid)


@sio_server.event
async def handle_message(sid, data):
    gamemanager.handleMessage(sid, data)
