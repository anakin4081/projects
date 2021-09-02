#!/usr/bin/env python3

import random, sys

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

Ai = ['ai', 'AI', 'Ai', 'aI']
Hu = ['human', 'Human']
moves = ['rock', 'paper', 'scissors']
letter = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z'
    ]


"""The Player class is the parent class for all of the Players
in this game"""

'''#CLASSES'''


class Player:   # Player Controller

    def __init__(self):
        self.score = 0

    def learn(self, my_move, their_move):   # remembers previous move
        self.tie = False
        self.lastmove = their_move
        if beats(my_move, their_move) is True:
            self.score += 1

        elif tie(my_move, their_move) is True:
            self.tie = True


class Human(Player):

    def move(self):
        while True:
            hand = input("[Enter Rock, Paper or Scissors]")
            if hand in moves:
                return hand
            elif "quit" in hand:
                print("bye")
                sys.exit(1)
            else:
                print("Invalid Choice Try Again")


class AI_type1(Player):  # chooses moves at random

    def move(self):
        hand = random.choice(moves)
        return hand


class AI_type2(Player):     # always chooses rock

    def move(self):
        hand = moves[0]
        return hand


class AI_type3(Player):     # immatates player moves

    def __init__(self):
        self.roundstart = 1
        self.score = 0

    def move(self):
        if self.roundstart == 1:
            hand = random.choice(moves)
            self.roundstart += 1
        else:
            hand = self.lastmove
        return hand


class AI_type4(Player):     # cycles between R,P,S

    def __init__(self):
        self.pos = 0
        self.score = 0

    def move(self):     # cycles pos
        if self.pos == 3:
            self.pos = 0
        else:
            pass
        hand = moves[self.pos]      # hand = pos of moves list
        self.pos += 1    # moves pos up 1 everytime its gets called
        return hand


def beats(one, two):    # Tells the program what beats what
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def tie(one, two):      # Tells the program its a tie
    return ((one == 'rock' and two == 'rock') or
            (one == 'scissors' and two == 'scissors') or
            (one == 'paper' and two == 'paper'))


class Game:     # Game class

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.tie = False

    def play_round(self):   # repeats for each round
        print(f"Player 1 = {self.p1.score} Player 2 = {self.p2.score}")
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        # print each move depending what was set to move 1 and 2
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if self.tie is True:
            print("It's a Tie")
        print("")

    def play_game(self, round_count, game_count):
        # play game starts passing self = game and round_count = 3
        for games in range(int(game_count)):
            self.p1.score = 0
            self.p2.score = 0
            print("")
            print("Game start!")
            print("")
            print(f"Game {games + 1} of {game_count}")
            print("")
            for round in range(int(round_count)):
                print(f"Round {round + 1}:")
                self.play_round()
            print(f"Player 1 = {self.p1.score} Player 2 = {self.p2.score}")
            if self.p1.score > self.p2.score:
                print("Player 1 Wins !!!")
            elif self.p2.score > self.p1.score:
                print("Player 2 Wins !!!")
            else:
                self.p2.score == self.p1.score
                print("It's a Tie !!!")
            print("Game over!")
            print("")   # prints game over after all rounds are completed
            print("")
        while True:
            play_again = input("would you like to play again")
            if play_again == "yes":
                break
            elif play_again == "no":
                print("bye thanks for playing")
                break
            else:
                print("Invalid Choice Try Again")


class Settings:

    def __init__(self):
        self.AI_choice = AI_type1
        self.Player_set1 = Human
        self.Player_set2 = self.AI_choice
        self.n_rounds = 3
        self.n_games = 1

    def Settings(self):     # settings to control game enviroment
        while True:
            settings_menu = input(
                "[would you like to change the settings (yes or no)]"
                )
            if settings_menu == "yes":
                print("exit setting by typing exit")
                print("------------")
                print("settings")
                print("------------")
                while True:
                    self.n_rounds = input(
                        "[please enter the number of Rounds or type endless]"
                        )  # links to n_rounds below
                    if self.n_rounds == "endless":
                        self.n_rounds = 256
                        break
                    elif self.n_rounds not in letter:
                        break
                    elif "exit" in self.n_rounds:
                        print("...")
                        break
                    else:
                        print("Invalid Choice Try Again")
                while True:
                    self.n_games = input("[please enter the number of Games]")
                    if self.n_games not in letter:
                        break
                    elif "exit" in self.n_games:
                        print("...")
                        break
                    else:
                        print("Invalid Choice Try Again")
                while True:
                    self.Player_T1 = input(
                        "[please enter Player 1 (human or ai)]"
                        )
                    if self.Player_T1 in Hu:
                        print("Human it is")
                        self.Player_set1 = Human
                        break
                    elif self.Player_T1 in Ai:
                        print("ah our finest ai")
                        self.Player_set1 = self.AI_choice
                        break
                    elif "exit" in self.Player_T1:
                        print("...")
                        break
                    else:
                        print("Invalid Choice Try Again")
                while True:
                    self.Player_T2 = input(
                        "[please enter Player 2 (human or ai)]"
                        )
                    if self.Player_T2 in Hu:
                        print("Human it is")
                        self.Player_set2 = Human
                        break
                    elif self.Player_T2 in Ai:
                        print("ah our finest ai")
                        self.Player_set2 = self.AI_choice
                        break
                    elif "exit" in self.Player_T2:
                        print("...")
                        break
                    else:
                        print("Invalid Choice Try Again")
                while True:
                    self.adv_fet = input(
                        "[would you like to enter adv features (yes or no)]"
                        )
                    if self.adv_fet == "yes":
                        print("")
                        print("!!!make sure you know what your doing!!!")
                        print("-----------------")
                        print("advanced settings")
                        print("-----------------")
                        print("")
                        while True:
                            print("[select AI method of playing]")
                            print("1.random  2.always rock")
                            print("3.cycles RPS  4.copies your last move")
                            ai_type = input("[enter the number for ai type]")
                            if ai_type == "1":
                                self.AI_choice = AI_type1
                                print("ah very random")
                            elif ai_type == "2":
                                self.AI_choice = AI_type2
                                print("cant go wrong with just picking rock")
                            elif ai_type == "3":
                                self.AI_choice = AI_type4
                                print("nothing wrong with predictable moves")
                            elif ai_type == "4":
                                self.AI_choice = AI_type3
                                print("copy cat killer beautiful choice")
                            else:
                                print("Invalid Choice Try Again")
                            print("great lets begin our game")
                            if self.Player_T2 in Hu:
                                print("Human it is")
                                self.Player_set2 = Human
                            else:
                                self.Player_T2 in Ai
                                print("ah our finest ai")
                                self.Player_set2 = self.AI_choice
                            if self.Player_T1 in Hu:
                                print("Human it is")
                                self.Player_set1 = Human
                            else:
                                self.Player_T1 in Ai
                                print("ah our finest ai")
                                self.Player_set1 = self.AI_choice
                            game = Game(self.Player_set1(), self.Player_set2())
                            game.play_game(self.n_rounds, self.n_games)
                    elif self.adv_fet == "no":
                        print("great lets begin our game")
                        break
                    elif "exit" in self.adv_fet:
                        print("...")
                        break
                    else:
                        print("Invalid Choice Try Again")
                game = Game(self.Player_set1(), self.Player_set2())
                game.play_game(self.n_rounds, self.n_games)
            elif settings_menu == "no":
                game = Game(self.Player_set1(), self.Player_set2())
                game.play_game(self.n_rounds, self.n_games)
            elif "quit" in settings_menu:
                print("...")
                sys.exit(1)
            else:
                print("Invalid Choice Try Again")


if __name__ == '__main__':
    print("---------------------------------------------------")
    print("Welcome to Rock Paper Scissors by Jacob Underwood Enjoy :)")
    print("---------------------------------------------------")
    settings = Settings()
    settings.Settings()
