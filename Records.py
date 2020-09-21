from os import system
from GameAesthetics import *
from Board import *
from Accountant import *
import sys

class Records(Board):
    
    def PrintTokensOnBoard(self,PlayersTokens,PlayersName,po,l1,enemigo,nl,pp):
    
        iop = input(PlayersName + " Enter the column and row: ")
        if len(iop) < 2 or len(iop) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Records1.PrintTokensOnBoard(PlayersTokens,PlayersName,po,l1,enemigo,nl,pp)
        self.lk = iop[0]
        self.lj = iop[1]
        if (self.lk not in self.checks or self.lj not in self.checks or 
            self.lk == '' or self.lj == '' or self.lk == '\n' and self.lj == '\n'):
            print('This Play is invalid')
            Records1.PrintTokensOnBoard(PlayersTokens,PlayersName,po,l1,enemigo,nl,pp) 
        else:
            if self.matrix[int(self.lk)][int(self.lj)] == "·" or self.matrix[int(self.lk)][int(self.lj)] == " · ":
                if self.matrix[int(self.lk)][int(self.lj)] == " · ":
                    self.matrix[int(self.lk)][int(self.lj)] = " " + PlayersTokens + " "
                else:
                    self.matrix[int(self.lk)][int(self.lj)] = PlayersTokens
                #llamadas
                Records1.PrintBoard()
                system('cls')
                GameAesthetics1.PrinttheCards()
                Records1.PrintBoard()
                if l1 == '●':
                    Records1.Remove(PlayersTokens,PlayersName,po,l1,enemigo,nl,pp) 
                if l1 == '○':   
                    Records1.Remove(PlayersTokens,PlayersName,po,l1,enemigo,nl,pp)
            else:
                print('Invalid play')
                Records1.PrintTokensOnBoard(PlayersTokens,PlayersName,po,l1,enemigo,nl,pp)

    def Remove(self,PlayersTokens,PlayersName,po,l1,enemigo,nl,pp):
        o1 = self.matrix     
        self.F =   [[[0,0], [0,3], [0,6]],
                    [[1,1], [1,3], [1,5]],
                    [[2,2], [2,3], [2,4]],
                    [[3,0], [3,1], [3,2]],
                    [[3,4], [3,5], [3,6]],
                    [[4,2], [4,3], [4,4]],
                    [[5,1], [5,3], [5,5]],
                    [[6,0], [6,3], [6,6]],
                    [[0,0], [3,0], [6,0]],
                    [[1,1], [3,1], [5,1]],
                    [[2,2], [3,2], [4,2]],
                    [[0,3], [1,3], [2,3]],
                    [[4,3], [5,3], [6,3]],
                    [[2,4], [3,4], [4,4]],
                    [[1,5], [3,5], [5,5]],
                    [[0,6], [3,6], [6,6]]]

        self.fila2 = [[l1], [l1], [l1]]
        self.fila4 = [[pp], [l1], [l1]]
        self.fila5 = [[l1], [pp], [l1]]
        self.fila6 = [[l1], [l1], [pp]]
        self.fila7 = [[l1], [pp], [pp]]
        self.fila8 = [[pp], [l1], [pp]]
        self.fila9 = [[pp], [pp], [l1]]
        
        Se_puede = [
            self.fila2,
            self.fila4,
            self.fila5,
            self.fila6,
            self.fila7,
            self.fila8,
            self.fila9
        ]

        for r in self.F:
            for t in Se_puede:
                if t == [[o1[r[0][0]][r[0][1]]], [o1[r[1][0]][r[1][1]]], [o1[r[2][0]][r[2][1]]]]:
                    o1[r[0][0]][r[0][1]] = pp
                    o1[r[1][0]][r[1][1]] = pp
                    o1[r[2][0]][r[2][1]] = pp
                    Records1.EliminateEnemy1(PlayersTokens,PlayersName,po,l1,enemigo,nl,pp)

    def EliminateEnemy1(self,PlayersTokens,PlayersName,po,l1,enemigo,nl,pp):
        global TokensRemovedWhite
        global TokensRemovedBlack
        p = input("Enter the column and row you want to remove from: " + nl)
        if len(p) < 2 or len(p) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Records1.EliminateEnemy1(PlayersTokens,PlayersName,po,l1,enemigo,nl,pp)
        self.dr = p[0]
        self.dre = p[1]
        if (self.dr not in self.checks or self.dre not in self.checks or 
            self.dr == '' or self.dre == '' or self.dr == '\n' and self.dr == '\n'):
            print('This Play is invalid')
            Records1.EliminateEnemy1(PlayersTokens,PlayersName,po,l1,enemigo,nl,pp)
        else:
            if PlayersTokens == '●':
                bolita = self.iop
                color = TokensRemovedWhite
            else:
                bolita = self.io
                color = TokensRemovedBlack
            if (self.matrix[int(self.dr)][int(self.dre)] == bolita or self.matrix[int(self.dr)][int(self.dre)] == " " + bolita + " " 
            or self.matrix[int(self.dr)][int(self.dre)] == " " + enemigo + " " or self.matrix[int(self.dr)][int(self.dre)] == enemigo):
                if self.matrix[int(self.dr)][int(self.dre)] == " " + bolita + " " or self.matrix[int(self.dr)][int(self.dre)] == " " + enemigo + " ":
                    self.matrix[int(self.dr)][int(self.dre)] = " · "
                else:
                    self.matrix[int(self.dr)][int(self.dre)] = "·"
                system('cls')
                print('Keep playing until 2 tabs remain')
                if enemigo == '○':
                    TokensRemovedBlack = TokensRemovedBlack + 1
                    color1 = TokensRemovedBlack
                else:
                    TokensRemovedWhite = TokensRemovedWhite + 1
                    color1 = TokensRemovedWhite
                if color == 6: 
                    Records1.PrintBoard()
                    if PlayersTokens == '●':
                        Records1.FeatureForThreeChipPlayers(PlayerName1,'●',100,'●','○',PlayerName2,self.ioo)
                    else:
                        Records1.FeatureForThreeChipPlayers(PlayerName2,'○',100,'○','●',PlayerName1,self.iopp)
                else:                                                          
                    Records1.PrintBoard()
            else:
                print('This sheet is not your enemy')  
                Records1.EliminateEnemy1(PlayersTokens,PlayersName,po,l1,enemigo,nl,pp)


    def MovementsChecks(self,nombre2,ficha2,ip,l,ls,hj,ppp):
        
        print('play ' + nombre2 + ' = ' + ficha2)
        i = input("the row and column "+ nombre2 +" you want to move:")
        if len(i) < 2 or len(i) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
        self.ws = i[0]
        self.wa = i[1]
        if (self.ws not in self.checks or self.wa not in self.checks or 
            self.ws == '' or self.wa == '' or self.ws == '\n' and self.ws== '\n'):
            print('This Play is invalid')
            Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
        else:
            self.t = self.ws + self.wa
            if ficha2 == '●':
                if self.t in self.PossibleMoves:
                    if (self.matrix[int(self.ws)][int(self.wa)] == ficha2 or self.matrix[int(self.ws)][int(self.wa)] == " " + ficha2 + " " or
                        self.matrix[int(self.ws)][int(self.wa)] == self.ioo or self.matrix[int(self.ws)][int(self.wa)] == " " + self.ioo + " "):
                        self.io = ficha2
                        print('TThis feet if its yours')
                        Records1.PositionsToMove(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('TThis feet if its yours')
                        Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    print('This position does not exist or is not permitted')
                    Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                if self.t in self.PossibleMoves:
                    if (self.matrix[int(self.ws)][int(self.wa)] == ficha2 or self.matrix[int(self.ws)][int(self.wa)] == " " + ficha2 + " " or
                        self.matrix[int(self.ws)][int(self.wa)] == self.iopp or self.matrix[int(self.ws)][int(self.wa)] == " " + self.iopp + " "):
                        print('TThis feet if its yours')
                        self.iop == ficha2
                        Records1.PositionsToMove(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('This sheet is not yours')
                        Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    print('This position does not exist or is not permitted')
                    Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)

    def PositionsToMove(self,nombre2,ficha2,ip,l,ls,hj,ppp): 
        print('play ' + nombre2 + ' = ' + ficha2)
        e = input("Which row and column do you want to move it to:")
        if len(e) < 2 or len(e) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
        self.pl = e[0]
        self.pls = e[1]
        p = (self.pl + self.pls)
        self.p = (self.pl + self.pls)
        if self.t == '00' :
            if p == '03' or p == '30':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '11' :
            if p == '13' or p == '31':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp) 
                
        if self.t == '22' :
            if p == '23' or p == '32':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                    
        if self.t == '44' :
            if p == '43' or p == '34':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)

        if self.t == '55' :
            if p == '53' or p == '35':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '66' :
            if p == '63' or p == '36':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
        # Posicion de una linia #2
        if self.t == '06' :
            if p == '03' or p == '36':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '15' :
            if p == '13' or p == '35':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '24' :
            if p == '23' or p == '34':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '42' :
            if p == '32' or p == '43':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '51' :
            if p == '31' or p == '53':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)

        if self.t == '60' :
            if p == '30' or p == '63':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
        # Posiciones del centro 
        if self.t == '03' :
            if p == '00' or p == '13' or p == '06':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)

        if self.t == '13' :
            if p == '03' or p == '11' or p == '15' or p == '23':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '23' :
            if p == '13' or p == '22' or p == '24':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '43' :
            if p == '42' or p == '45' or p == '53' or p == '44':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp) 
        
        if self.t == '53' :
            if p == '51' or p == '43' or p == '55' or p == '63':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp) 
                
        if self.t == '63' :
            if p == '60' or p == '53' or p == '66':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
        # Posiciones del centro #2
        if self.t == '30' :
            if p == '00' or p == '60' or p == '31':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)  
        
        if self.t == '31' :
            if p == '30' or p == '11' or p == '51' or p == '32':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
        
        if self.t == '32' :
            if p == '31' or p == '42' or p == '22' :
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)    
                
        if self.t == '34' :
            if p == '24' or p == '44' or p == '35':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
        
        if self.t == '35' :
            if p == '34' or p == '15' or p == '36' or p == '55':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)
        
        if self.t == '36' :
            if p == '06' or p == '35' or p == '66':
                Records1.PlayPrinter(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)

    def PlayPrinter(self,nombre2,ficha2,ip,l,ls,hj,ppp):
        if self.matrix[int(self.pl)][int(self.pls)] == "·" or self.matrix[int(self.pl)][int(self.pls)] == " · ":
                if self.matrix[int(self.pl)][int(self.pls)] == " · ":
                    if self.t == '31' or self.t == '35': 
                        self.matrix[int(self.ws)][int(self.wa)] = " · "
                    else:
                        self.matrix[int(self.ws)][int(self.wa)] = "·"
                    self.matrix[int(self.pl)][int(self.pls)] = " " + ficha2 + " "
                else:
                    if self.t == '31' or self.t == '35': 
                        self.matrix[int(self.ws)][int(self.wa)] = " · "
                    else:
                        self.matrix[int(self.ws)][int(self.wa)] = "·"
                    self.matrix[int(self.pl)][int(self.pls)] = ficha2
                system('cls')  
                print('Keep playing until 2 tabs remain')
                Records1.PrintBoard()
                if l == '●':
                    Records1.Remove1(PlayerName1,'●',100,'●','○',PlayerName2,self.ioo)
                else:
                    if l == '○':
                        Records1.Remove1(PlayerName2,'○',100,'○','●',PlayerName1,self.iopp)
        else:
            print('This position cannot be')
            Records1.MovementsChecks(nombre2,ficha2,ip,l,ls,hj,ppp)

    def Remove1(self,nombre2,ficha2,ip,l,ls,hj,ppp):
        global TokensRemovedWhite
        global TokensRemovedBlack
        
        s = self.matrix     
        self.F =   [[[0,0], [0,3], [0,6]],
                    [[1,1], [1,3], [1,5]],
                    [[2,2], [2,3], [2,4]],
                    [[3,0], [3,1], [3,2]],
                    [[3,4], [3,5], [3,6]],
                    [[4,2], [4,3], [4,4]],
                    [[5,1], [5,3], [5,5]],
                    [[6,0], [6,3], [6,6]],
                    [[0,0], [3,0], [6,0]],
                    [[1,1], [3,1], [5,1]],
                    [[2,2], [3,2], [4,2]],
                    [[0,3], [1,3], [2,3]],
                    [[4,3], [5,3], [6,3]],
                    [[2,4], [3,4], [4,4]],
                    [[1,5], [3,5], [5,5]],
                    [[0,6], [3,6], [6,6]]]

        self.fila2 = [[l],  [l],   [l]]
        self.fila4 = [[ppp],[l],   [l]]
        self.fila5 = [[l],  [ppp], [l]]
        self.fila6 = [[l],  [l],   [ppp]]
        self.fila7 = [[l],  [ppp], [ppp]]
        self.fila8 = [[ppp],[l],   [ppp]]
        self.fila9 = [[ppp],[ppp], [l]]
        
        Se_puede = [
            self.fila2,
            self.fila4,
            self.fila5,
            self.fila6,
            self.fila7,
            self.fila8,
            self.fila9
        ]

        for r in self.F:
            for t in Se_puede:
                if t == [[s[r[0][0]][r[0][1]]], [s[r[1][0]][r[1][1]]], [s[r[2][0]][r[2][1]]]]:
                    s[r[0][0]][r[0][1]] = ppp
                    s[r[1][0]][r[1][1]] = ppp
                    s[r[2][0]][r[2][1]] = ppp
                    Records1.EliminateEnemy(nombre2,ficha2,ip,l,ls,hj,ppp)
                    
        else:
            if l == '●':
                    if TokensRemovedBlack == 6:
                        system('cls')
                        print('Keep playing until 2 tabs remain')
                        Records1.PrintBoard()
                        Records1.FeatureForThreeChipPlayers(PlayerName2,'○',100,'○','●',PlayerName1,self.iopp)
                    else:
                        system('cls')
                        print('Keep playing until 2 tabs remain')
                        Records1.PrintBoard()
                        Records1.MovementsChecks(PlayerName2,'○',100,'○','●',PlayerName1,self.iopp)
            else:
                    if TokensRemovedWhite == 6:
                        system('cls')
                        print('Keep playing until 2 tabs remain')
                        Records1.PrintBoard()
                        Records1.FeatureForThreeChipPlayers(PlayerName1,'●',100,'●','○',PlayerName2,self.ioo)
                    else:
                        system('cls')
                        print('Keep playing until 2 tabs remain')
                        Records1.PrintBoard()
                        Records1.MovementsChecks(PlayerName1,'●',100,'●','○',PlayerName2,self.ioo)

    def EliminateEnemy(self,nombre2,ficha2,ip,l,ls,hj,ppp):
        global TokensRemovedWhite
        global TokensRemovedBlack
        o = input("Enter the column and row you want to remove from: " + hj)
        if len(o) < 2 or len(o) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Records1.EliminateEnemy(nombre2,ficha2,ip,l,ls,hj,ppp)
        self.qw = o[0]
        self.qwe = o[1]
        if (self.qw not in self.checks or self.qwe not in self.checks or 
            self.qw == '' or self.qwe == '' or self.qw == '\n' and self.qw == '\n'):
            print('This Play is invalid')
            Records1.EliminateEnemy(nombre2,ficha2,ip,l,ls,hj,ppp)
        else:
            if ls == '●':
                ls = '●'
                segundaficha =self.ioo
            else:
                if ls == '○':
                    ls == '○'
                    segundaficha = self.iopp
            if (self.matrix[int(self.qw)][int(self.qwe)] == ls or self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " "  
                or self.matrix[int(self.qw)][int(self.qwe)] ==  segundaficha or 
                self.matrix[int(self.qw)][int(self.qwe)] ==  " " +segundaficha + " "):
                if self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " " or self.matrix[int(self.qw)][int(self.qwe)] == " " + segundaficha + " ":
                    self.matrix[int(self.qw)][int(self.qwe)] = " · "
                else:
                    self.matrix[int(self.qw)][int(self.qwe)] = "·"
                    if self.p == '31' or self.p == '35': 
                        self.matrix[int(self.pl)][int(self.pls)] =  " " + ppp + " " 
                    else:
                        self.matrix[int(self.pl)][int(self.pls)] = ppp
                    system('cls')
                    print('Keep playing until 2 tabs remain')
                    Records1.PrintBoard()
                    if ls == '○':
                        TokensRemovedBlack = TokensRemovedBlack + 1
                        color1 = TokensRemovedBlack
                    else:
                        TokensRemovedWhite = TokensRemovedWhite + 1
                        color1 = TokensRemovedWhite
                    if color1 == 7:
                        Accountant1.MovementCounter()
                    else:  
                        if color1 == 6:
                            if ls == '○':
                                print('you have 3 tabs you can move where you want')
                                Records1.FeatureForThreeChipPlayers(PlayerName2,'○',100,'○','●',PlayerName1,self.iopp)
                            else:
                                print('you have 3 tabs you can move where you want')
                                Records1.FeatureForThreeChipPlayers(PlayerName1,'●',100,'●','○',PlayerName2,self.ioo)
                        else:
                            if ls == '○':
                                Records1.MovementsChecks(PlayerName2,'○',100,'○','●',PlayerName1,self.iopp)
                            else:
                                Records1.MovementsChecks(PlayerName1,'●',100,'●','○',PlayerName2,self.ioo)
            else:
                print('This sheet is not your enemy')  
                Records1.EliminateEnemy(nombre2,ficha2,ip,l,ls,hj,ppp)

    def FeatureForThreeChipPlayers(self,nombre2,ficha2,ip,l,ls,hj,ppp):      
        print('play ' + nombre2 + ' = ' + ficha2)
        t = input("the row and column "+ nombre2 +" you want to move:")
        if len(t) < 2 or len(t) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Records1.FeatureForThreeChipPlayers(nombre2,ficha2,ip,l,ls,hj,ppp)
        self.wss = t[0]
        self.waa = t[1]
        if (self.wss not in self.checks or self.waa not in self.checks or 
            self.wss == '' or self.waa == '' or self.wss == '\n' and self.wss== '\n'):
            print('This Play is invalid')
            Records1.FeatureForThreeChipPlayers(nombre2,ficha2,ip,l,ls,hj,ppp)
        else:
            self.t = self.wss + self.waa
            if ficha2 == '●':
                if self.t in self.PossibleMoves:
                    if (self.matrix[int(self.wss)][int(self.waa)] == ficha2 or self.matrix[int(self.wss)][int(self.waa)] == " " + ficha2 + " " or
                        self.matrix[int(self.wss)][int(self.waa)] == self.ioo or 
                        self.matrix[int(self.wss)][int(self.waa)] == " " + self.ioo + " "):
                        self.io = ficha2
                        print('TThis feet if its yours')
                        Records1.ThreeTabPrimer(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('This sheet is not yours')
                        Records1.FeatureForThreeChipPlayers(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    print('This position does not exist or is not permitted')
                    Records1.FeatureForThreeChipPlayers(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                if self.t in self.PossibleMoves:
                    if (self.matrix[int(self.wss)][int(self.waa)] == ficha2 or self.matrix[int(self.wss)][int(self.waa)] == " " + ficha2 + " " or
                        self.matrix[int(self.wss)][int(self.waa)] == self.iopp or self.matrix[int(self.wss)][int(self.waa)] == " " + self.iopp + " "):
                        print('TThis feet if its yours')
                        self.iop == ficha2
                        Records1.ThreeTabPrimer(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('This sheet is not yours')
                        Records1.FeatureForThreeChipPlayers(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    print('This position does not exist or is not permitted')
                    Records1.FeatureForThreeChipPlayers(nombre2,ficha2,ip,l,ls,hj,ppp)

    def ThreeTabPrimer(self,nombre2,ficha2,ip,l,ls,hj,ppp): 
        q = input("Which row and column do you want to move it to:")
        if len(q) < 2 or len(q) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Records1.FeatureForThreeChipPlayers(nombre2,ficha2,ip,l,ls,hj,ppp)
        self.pll = q[0]
        self.pls = q[1]
        if self.matrix[int(self.pll)][int(self.plss)] == "·" or self.matrix[int(self.pll)][int(self.plss)] == " · ":
                if self.matrix[int(self.pll)][int(self.plss)] == " · ":
                    if self.t == '31' or self.t == '35': 
                        self.matrix[int(self.wss)][int(self.waa)] = " · "
                    else:
                        self.matrix[int(self.wss)][int(self.waa)] = "·"
                    self.matrix[int(self.pll)][int(self.plss)] = " " + ficha2 + " "
                else:
                    if self.t == '31' or self.t == '35': 
                        self.matrix[int(self.wss)][int(self.waa)] = " · "
                    else:
                        self.matrix[int(self.wss)][int(self.waa)] = "·"
                    self.matrix[int(self.pll)][int(self.plss)] = ficha2
                system('cls')  
                print('Keep playing until 2 tabs remain')
                Records1.PrintBoard()
                if l == '●':
                    Records1.Remove1(PlayerName1,'●',100,'●','○',PlayerName2,self.ioo)
                else:
                    if l == '○':
                        Records1.Remove1(PlayerName2,'○',100,'○','●',PlayerName1,self.iopp)


Records1 = Records()