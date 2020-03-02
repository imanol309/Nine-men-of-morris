from os import system
class estetica:
    def piesas(self):
        print ("●●●●●●●●●")
        print("○○○○○○○○○")
class tablero:
    def __init__(self):
        self.a = ["·","——","——","·","——","——","·"]
        self.b = ["| ","·","——","·","——","·"," |"]
        self.c = ["| ","| ","·","·","·"," |"," |"]
        self.d = ["· ","· ","· ","","· ","·","·"]
        self.e = ["| ","| ","·","·","·"," |"," |"]
        self.f = ["| ","·","——","·","——","·"," |"]
        self.g = ["·","——","——","·","——","——","·"]
        self.matrix = [self.a,self.b,self.c,self.d,self.e,self.f,self.g]
        
    def imprimir(self):
        for e in range(0,len(self.matrix)):
            for i in range(0,len(self.matrix)):
                print(self.matrix[e][i],end=' ')
            print('')
        
class fichas(tablero):
    def jugadores(self):
        c_judador1 = 9
        c_judador2 = 9
        i = 0
        while i < 9:
            i+=1
            while c_judador1 + 1 > c_judador2:
                    lk = int(input('FILA DEL 1 JUGADOR:'))
                    lj= int(input('COLUNA DEL 1 JUGADOR:'))
                    self.matrix[lk][lj] = '●'
                    ficha1.imprimir()
                    system('cls')
                    estetica1.piesas()
                    ficha1.imprimir()
                    c_judador1-=1
                
            while c_judador2 > c_judador1:
                    lk = int(input('FILA DEL 2 JUGADOR:'))
                    lj= int(input('COLUNA DEL 2 JUGADOR:'))
                    self.matrix[lk][lj] = '○'
                    ficha1.imprimir()
                    system('cls')
                    estetica1.piesas()
                    ficha1.imprimir()
                    c_judador2-=1
#objetos
estetica1 = estetica()
tablero1 = tablero()
ficha1 = fichas()
# klk

#llamas
estetica1.piesas()
tablero1.imprimir()
ficha1.jugadores()
ficha1.imprimir()