from os import system
import sys


class Board():
    def __init__(self):
        self.a = ["·","——","——","·","——","——","·"]
        self.b = ["| ","·","——","·","——","·"," |"]
        self.c = ["| ","| ","·","·","·"," |"," |"]
        self.d = ["·"," · ","·"," ","·"," · ","·"]
        self.e = ["| ","| ","·","·","·"," |"," |"]
        self.f = ["| ","·","——","·","——","·"," |"]
        self.g = ["·","——","——","·","——","——","·"]
        self.matrix = [self.a,self.b,self.c,self.d,self.e,self.f,self.g]
        self.checks = "0123456"
        self.PossibleMoves = ('00','03','06','11','13','15','22','23','24','30','31','32','34','35','36',
        '42','43','44','51','53','55','60','63','66')
        self.io = '◍'
        self.iop = "◌"
        self.ioo = '◍'
        self.iopp = "◌"

    def PrintBoard(self):
        r = 0
        for e in range(0,len(self.matrix)):
            print(r,end=" ")
            r+=1
            for i in range(0,len(self.matrix)):
                print(self.matrix[e][i],end=' ')
            print('')
        print("  "'0',' 1',' 2','3','4',' 5',' 6')
        
        
Board1 = Board()