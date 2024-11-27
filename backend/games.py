from fastapi.websockets import WebSocket
import chess
import time
from messages import MOVE, GAME_OVER

class Game():
    def __init__(self, player1:WebSocket, player2: WebSocket):
        self.player1 = player1
        self.player2 = player2
        self.board = chess.Board()
        self.timePeriod = time.time()
        self.winner =  None

    def display_object_details(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")




    def makeMove(self,sid, move):
        try:
            self.board.push(move)  # Trying to push the move
        except Exception as e:  # Catching any exception
            print(f"Error occurred: {e}") 
            return 

        #check if the game is OVer
        if(self.board.is_game_over()):
            self.player1.emit(type = GAME_OVER,winner = "black" if self.board.turn() == "w" else "white"
 )                            
        # Send the updated board
        if len(self.board.moves) % 2 == 0:
            # It's player 1's turn (even number of moves)
            self.player1.emit("updatedBoard", self.board)
        else:
            # It's player 2's turn (odd number of moves)
            self.player2.emit("updatedBoard", self.board)





        