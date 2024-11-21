from fastapi.websockets import WebSocket
import chess
from datetime import time


class Game():
    def __init__(self, player1:WebSocket, player2: WebSocket):
        self.player1 = player1
        self.player2 = player2
        self.board = chess.Board()
        self.timePeriod = time.time()
        self.winner =  None



        
        