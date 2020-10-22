from os import system
from GameAesthetics import *
from Records import *
from Board import *
import sys

class Accountant(Board):
     
    def PlayCounter(self):
        global TokensPlayer1
        global TokensPlayer2      
        i = 0 
        while i < 9:
            i+=1
            while TokensPlayer1 + 1 > TokensPlayer2:
                Records1.PrintTokensOnBoard('●',PlayerName1,9,'●','○',PlayerName2,self.io)
                TokensPlayer1-=1
            while  TokensPlayer2 > TokensPlayer1:
                Records1.PrintTokensOnBoard('○',PlayerName2,9,'○','●',PlayerName1,self.iop)
                TokensPlayer2-=1

    def MovementCounter(self):
        global TokensRemovedWhite
        global TokensRemovedBlack
        m_PlayersTokens = 100
        m_jugador2 = 100
        p = 0
        if TokensRemovedWhite >= 7 or TokensRemovedBlack >= 7:
            print("l")
            if TokensRemovedWhite >= 7:
                system("cls")
                print('CONGRATULATIONS YOU WON ' + PlayerName2)
                sys.exit()
            else:
                system("cls")
                print('CONGRATULATIONS YOU WON ' + PlayerName1)
                sys.exit()
        while p < 100:
            p+=1
            while m_PlayersTokens +1 >  m_jugador2:
                system("cls")
                Records1.PrintBoard()
                Records1.MovementsChecks(PlayerName1,'●',100,'●','○',PlayerName2,self.ioo)
                m_PlayersTokens-=1 
            while m_jugador2 > m_PlayersTokens:
                system("cls")
                Records1.PrintBoard()
                Records1.MovementsChecks(PlayerName2,'○',100,'○','●',PlayerName1,self.iopp)
                m_jugador2-=1

Accountant1 = Accountant()