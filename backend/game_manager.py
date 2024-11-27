from games import Game
#Define the async server
#Get all the messages or varriables
from messages import MOVE, INIT_GAME

class GameManager():
    def __init__(self):
        self.pendingUser =  None
        self.games = [] #This stores all the active games
        self.users = []


    #Define the events
    def addUser(self,sid):
        self.users.append(sid)
        print(self.users)



    def removeUser(self, sid):
        print('disconnect ', sid)
        self.users.remove(sid)


        #Stop the game




    def handleMessage(self,sid, data):
        message = data
        
        # There are two types of message

        # Check the message type:
        try:

            if (message['type'] == INIT_GAME):
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
                    # print(game.display_object_details())

                    #Since there is no active pending user set it back to NONe
                    self.pendingUser = None

                # print(self.games)
            #This section deals with moves
            if(message['type'] == MOVE):
                print('ok')
                #Find the game with sid
                def findgame(sid):
                    for game in self.games:
                        print(sid)
                        if game.player1 ==  sid or game.player2 == sid: 
                            return game.board

                #Get the actual board of that game
                board = findgame(sid)
                print(board)
                try:
                    board.push(data)
                except Exception as err:
                    print("MOvess failed",err)

        except Exception as err:
            print(err)


        

        



