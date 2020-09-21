from os import system
import sys

TokensRemovedWhite = 0
TokensRemovedBlack = 0
TokensPlayer1 = 9
TokensPlayer2 = 9
PlayerName1 = input("Player's name1:")
PlayerName2 = input("Player's name2:")
system("cls")


class GameAesthetics():
    
    def PrinttheCards(self):
        global TokensPlayer1
        global TokensPlayer2  
        BallsOfWhite = "●"
        BallsOfBlack = "○"
        u1 = (BallsOfWhite * TokensPlayer1)
        o1 = (BallsOfBlack * TokensPlayer2)
        print('Pieces of ' + PlayerName1 + " " + str(u1))
        print('Pieces of ' + PlayerName2 + " " + str(o1))

GameAesthetics1 = GameAesthetics()