import random, os

Ai = ('ai', 'AI', 'Ai', 'aI')
Hu = ('human', 'Human')
moves = ('A1,A2,A3,A4,A5,A6,A7,A8,A9')
letter = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z'
    )

class Game:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def play_games(self,p1,p2,keys):
        print("welcome to Naughts and Crosses")
        print(f"Player 1 = {self.p1.move} Player 2 = {self.p2.move}")
        A1 = A2 = A3 = A4 = A5 = A6 = A7 = A8 = A9 = " "
        Grid = [A1,A2,A3,A4,A5,A6,A7,A8,A9]
        A1_free,A2_free,A3_free,A4_free,A5_free,A6_free,A7_free,A8_free,A9_free = "A1","A2","A3","A4","A5","A6","A7","A8","A9"
        freemoves = [A1_free,A2_free,A3_free,A4_free,A5_free,A6_free,A7_free,A8_free,A9_free]
        positions_taken = 0
        while positions_taken < 9:
            self.p1.round(Grid,freemoves,keys)
            self.p2.round(Grid,freemoves,keys)

    def settings(self):
        an = input("enter settings yes/no")[0:3]
        if an == "yes":
            an1 = input(f"pick a number\n 1:config \n 2:players \n 3:grid size \n 4:difficulty \n 5:zoom \n 6:back")[0:1]
            if an1 == 1:
                x = input("enter mumbers on your numpad from left to right then down all the way")[0:9]
                key1, key2, key3, key4, key5, key6, key7, key8, key9 = x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]
                with open("NACSettings.jke","w+") as f:
                    f.write(f"{key1}, {key2}, {key3}, {key4}, {key5}, {key6}, {key7}, {key8}, {key9}")
                f.close()
            else:
                print("used else")
                x = input("enter mumbers on your numpad from left to right then down all the way")[0:9]
                key1, key2, key3, key4, key5, key6, key7, key8, key9 = x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]
                with open("NACSettings.jke","w+") as f:
                    f.write(f"{key1}:{key2}:{key3}:{key4}:{key5}:{key6}:{key7}:{key8}:{key9}: KEY CONFIG")
                f.close()

class player:

    def __init__(self):
        self.score = 0 
        self.move = "O"

    def round(self,Grid,freemoves,keys):
        print("player 1 turn")
        print(f'\n|{Grid[0]}|{Grid[1]}|{Grid[2]}|\n-------\n|{Grid[3]}|{Grid[4]}|{Grid[5]}|\n-------\n|{Grid[6]}|{Grid[7]}|{Grid[8]}|')
        pos = input ("select a position by numpad")[0:1]
        print(pos)
        if pos == keys[0] and "A1" in freemoves:
            freemoves[0] = "taken"
            Grid[0] = self.move
        elif pos == keys[1] and "A2" in freemoves:
            freemoves[1] = "taken"
            Grid[1] = self.move
        elif pos == keys[2] and "A3" in freemoves:
            freemoves[2] = "taken"
            Grid[2] = self.move
        elif pos == keys[3] and "A4" in freemoves:
            freemoves[3] = "taken"
            Grid[3] = self.move
        elif pos == keys[4] and "A5" in freemoves:
            freemoves[4] = "taken"
            Grid[4] = self.move
        elif pos == keys[5] and "A6" in freemoves:
            freemoves[5] = "taken"
            Grid[5] = self.move
        elif pos == keys[6] and "A7" in freemoves:
            freemoves[6] = "taken"
            Grid[6] = self.move
        elif pos == keys[7] and "A8" in freemoves:
            freemoves[7] = "taken"
            Grid[7] = self.move
        elif pos == keys[8] and "A9" in freemoves:
            freemoves[8] = "taken"
            Grid[8] = self.move
        else: 
            print("invalid move")
        
class AI:
    def __init__(self):
        self.score = 0
        self.move = "X"

    def round(self,Grid,freemoves,keys):
        print("player 2 turn")
        print(f'\n|{Grid[0]}|{Grid[1]}|{Grid[2]}|\n-------\n|{Grid[3]}|{Grid[4]}|{Grid[5]}|\n-------\n|{Grid[6]}|{Grid[7]}|{Grid[8]}|')
        pos = input ("select a position by numpad")[0:1]
        if pos == keys[0] and "A1" in freemoves:
            freemoves[0] = "taken"
            Grid[0] = self.move
        elif pos == keys[1] and "A2" in freemoves:
            freemoves[1] = "taken"
            Grid[1] = self.move
        elif pos == keys[2] and "A3" in freemoves:
            freemoves[2] = "taken"
            Grid[2] = self.move
        elif pos == keys[3] and "A4" in freemoves:
            freemoves[3] = "taken"
            Grid[3] = self.move
        elif pos == keys[4] and "A5" in freemoves:
            freemoves[4] = "taken"
            Grid[4] = self.move
        elif pos == keys[5] and "A6" in freemoves:
            freemoves[5] = "taken"
            Grid[5] = self.move
        elif pos == keys[6] and "A7" in freemoves:
            freemoves[6] = "taken"
            Grid[6] = self.move
        elif pos == keys[7] and "A8" in freemoves:
            freemoves[7] = "taken"
            Grid[7] = self.move
        elif pos == keys[8] and "A9" in freemoves:
            freemoves[8] = "taken"
            Grid[8] = self.move
        else: 
            print("invalid move")

def sequence():
    player1 = player
    player2 = AI
    game = Game(player1(),player2())
    game.settings()
    with open("NACSettings.jke","r") as key:
        x = []
        x.extend(key.read())
        key1,key2,key3,key4,key5,key6,key7,key8,key9 = x[0],x[2],x[4],x[6],x[8],x[10],x[12],x[14],x[16]
        keys = [key1,key2,key3,key4,key5,key6,key7,key8,key9]
    game.play_games(player1,player2,keys)

sequence()