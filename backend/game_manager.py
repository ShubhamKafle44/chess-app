from games import Game
#Define the async server
#Get all the messages or varriables
from messages import MOVES, INIT_GAME

class GameManager():
    def __init__(self):
        self.pendingUser =  None
        self.games = [] #This stores all the active games


    #Define the events
    def connect(self,sid):
        print('connect ', sid)

    def disconnect(self, sid):
        print('disconnect ', sid)

    def my_message(self,sid, data):
        print('message ', data)

        #There are two types of message

        #Check the message type:
        try:
            if (data == INIT_GAME):
            #start the game
            #Player 1 joins
            #check if there is a pending user here

                if(self.pendingUser == None):
                    #there is no pre existing user here
                    self.pendingUser = sid
                else:
                    #There is already someone waiting for a game
                    #Start a game between the current user and the pending user
                    game = Game(self.pendingUser, sid)
                    #We also need to store all the games in the gamesList for database and reconnect logic
                    self.games.append(game)
                    #Since there is no active pending user set it back to NONe
                    self.pendingUser = None

            #This section deals with moves
            if(data == MOVES):
                #Find the game with sid
                def findgame(self, sid):
                    for game in self.games:
                        if game.player1 ==  sid or game.player2 == sid: 
                            board = game.board

                #Get the actual board of that game
                board = findgame(sid)
                try:
                    board.push(data)
                except Exception as err:
                    print("MOvess failed",err)

        except Exception as err:
            print(err)
            print(data)

        

        



