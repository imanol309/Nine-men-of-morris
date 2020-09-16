from os import system
import sys

z = input("Player's name1:")
ml = input("Player's name2:")
blanca = 0
negra1 = 0
c_jugador1 = 4
c_jugador2 = 4
system("cls")

class Estetica():

    def Piesas(self):
        global c_jugador1
        global c_jugador2  
        BolaBlanca = "●"
        BolaNegra = "○"
        u = c_jugador1 * BolaBlanca
        o = c_jugador2 * BolaNegra
        print ('Pieces of ' + z + " " + str(u))
        print('Pieces of ' + ml + " " + str(o))

class Tablero():
    
    def __init__(self):
        self.a = ["·","——","——","·","——","——","·"]
        self.b = ["| ","·","——","·","——","·"," |"]
        self.c = ["| ","| ","·","·","·"," |"," |"]
        self.d = ["·"," · ","·"," ","·"," · ","·"]
        self.e = ["| ","| ","·","·","·"," |"," |"]
        self.f = ["| ","·","——","·","——","·"," |"]
        self.g = ["·","——","——","·","——","——","·"]
        self.matrix = [self.a,self.b,self.c,self.d,self.e,self.f,self.g]
        self.verificacion = "0123456"
        self.jugadas_posibles = ('00','03','06','11','13','15','22','23','24','30','31','32','34','35','36',
        '42','43','44','51','53','55','60','63','66')
        self.io = '◍'
        self.iop = "◌"
        self.ioo = '◍'
        self.iopp = "◌"


    def Imprimir(self):
        r = 0
        for e in range(0,len(self.matrix)):
            print(r,end=" ")
            r+=1
            for i in range(0,len(self.matrix)):
                print(self.matrix[e][i],end=' ')
            print('')
        print("  "'0',' 1',' 2','3','4',' 5',' 6')
        
class Fichas(Tablero):

    def Piezas_en_el_Tablero(self,jugador1,nombre_jugador,po,l1,enemigo,nl,pp):
        
        iop = input(nombre_jugador + " Enter the column and row: ")
        if len(iop) < 2 or len(iop) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Ficha1.Piezas_en_el_Tablero(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)
        self.lk = iop[0]
        self.lj = iop[1]
        # self.lk = input('ROW OF : ' + nombre_jugador)
        # self.lj= input('COLUNA OF : '+ nombre_jugador)
        if (self.lk not in self.verificacion or self.lj not in self.verificacion or 
            self.lk == '' or self.lj == '' or self.lk == '\n' and self.lj == '\n'):
            print('THIS PLAY IS INVALID')
            Ficha1.Piezas_en_el_Tablero(jugador1,nombre_jugador,po,l1,enemigo,nl,pp) 
        else:
            if self.matrix[int(self.lk)][int(self.lj)] == "·" or self.matrix[int(self.lk)][int(self.lj)] == " · ":
                if self.matrix[int(self.lk)][int(self.lj)] == " · ":
                    self.matrix[int(self.lk)][int(self.lj)] = " " + jugador1 + " "
                else:
                    self.matrix[int(self.lk)][int(self.lj)] = jugador1
                #llamadas
                Ficha1.Imprimir()
                system('cls')
                Estetica1.Piesas()
                Ficha1.Imprimir()
                if l1 == '●':
                    Ficha1.Eliminar(jugador1,nombre_jugador,po,l1,enemigo,nl,pp) 
                if l1 == '○':   
                    Ficha1.Eliminar(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)
            else:
                print('INVALID PLAY')
                Ficha1.Piezas_en_el_Tablero(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)

    def Eliminar(self,jugador1,nombre_jugador,po,l1,enemigo,nl,pp):
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
                    Ficha1.Elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)

    def Elimanar_enemigo2(self,jugador1,nombre_jugador,po,l1,enemigo,nl,pp):
        global blanca
        global negra1
        p = input("Enter the column and row you want to remove from: " + nl)
        if len(p) < 2 or len(p) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Ficha1.Elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)
        self.dr = p[0]
        self.dre = p[1]
        if (self.dr not in self.verificacion or self.dre not in self.verificacion or 
            self.dr == '' or self.dre == '' or self.dr == '\n' and self.dr == '\n'):
            print('THIS PLAY IS INVALID')
            Ficha1.Elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)
        else:
            if jugador1 == '●':
                bolita = self.iop
                color = blanca
            else:
                bolita = self.io
                color = negra1
            if (self.matrix[int(self.dr)][int(self.dre)] == bolita or self.matrix[int(self.dr)][int(self.dre)] == " " + bolita + " " 
            or self.matrix[int(self.dr)][int(self.dre)] == " " + enemigo + " " or self.matrix[int(self.dr)][int(self.dre)] == enemigo):
                if self.matrix[int(self.dr)][int(self.dre)] == " " + bolita + " " or self.matrix[int(self.dr)][int(self.dre)] == " " + enemigo + " ":
                    self.matrix[int(self.dr)][int(self.dre)] = " · "
                else:
                    self.matrix[int(self.dr)][int(self.dre)] = "·"
                system('cls')
                print('KEEP PLAYING UNTIL 2 TABS REMAIN')
                if enemigo == '○':
                    negra1 = negra1 + 1
                    color1 = negra1
                else:
                    blanca = blanca + 1
                    color1 = blanca
                if color == 6: 
                    Ficha1.Imprimir()
                    if jugador1 == '●':
                        Ficha1.Funcion_jugadores(z,'●',100,'●','○',ml,self.ioo)
                    else:
                        Ficha1.Funcion_jugadores(ml,'○',100,'○','●',z,self.iopp)
                else:                                                          
                    Ficha1.Imprimir()
            else:
                print('THIS SHEET IS NOT YOUR ENEMY')  
                Ficha1.Elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)


    def Verificaciones(self,nombre2,ficha2,ip,l,ls,hj,ppp):
        print('play ' + nombre2 + ' = ' + ficha2)
        i = input("the row and column "+ nombre2 +" you want to move:")
        if len(i) < 2 or len(i) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        self.ws = i[0]
        self.wa = i[1]
        # self.ws = input('THE ROW OF '+ nombre2 + ' WHAT DO YOU WANT TO MOVE:')
        # self.wa = input('THE COLUNA OF ' + nombre2 + ' WHAT DO YOU WANT TO MOVE:')
        if (self.ws not in self.verificacion or self.wa not in self.verificacion or 
            self.ws == '' or self.wa == '' or self.ws == '\n' and self.ws== '\n'):
            print('THIS PLAY IS INVALID')
            Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        else:
            self.t = self.ws + self.wa
            if ficha2 == '●':
                if self.t in self.jugadas_posibles:
                    if (self.matrix[int(self.ws)][int(self.wa)] == ficha2 or self.matrix[int(self.ws)][int(self.wa)] == " " + ficha2 + " " or
                        self.matrix[int(self.ws)][int(self.wa)] == self.ioo or self.matrix[int(self.ws)][int(self.wa)] == " " + self.ioo + " "):
                        self.io = ficha2
                        print('THIS FEET IF ITS YOURS')
                        Ficha1.Posiciones_de_movimientos(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('THIS FEET IF ITS YOURS')
                        Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    print('THIS POSITION DOES NOT EXIST OR IS NOT PERMITTED')
                    Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                if self.t in self.jugadas_posibles:
                    if (self.matrix[int(self.ws)][int(self.wa)] == ficha2 or self.matrix[int(self.ws)][int(self.wa)] == " " + ficha2 + " " or
                        self.matrix[int(self.ws)][int(self.wa)] == self.iopp or self.matrix[int(self.ws)][int(self.wa)] == " " + self.iopp + " "):
                        print('THIS FEET IF ITS YOURS')
                        self.iop == ficha2
                        Ficha1.Posiciones_de_movimientos(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('THIS SHEET IS NOT YOURS')
                        Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    print('THIS POSITION DOES NOT EXIST OR IS NOT PERMITTED')
                    Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)

    def Posiciones_de_movimientos(self,nombre2,ficha2,ip,l,ls,hj,ppp): 
        print('play ' + nombre2 + ' = ' + ficha2)
        e = input("Which row and column do you want to move it to:")
        if len(e) < 2 or len(e) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        self.pl = e[0]
        self.pls = e[1]
        p = (self.pl + self.pls)
        self.p = (self.pl + self.pls)
        if self.t == '00' :
            if p == '03' or p == '30':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '11' :
            if p == '13' or p == '31':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp) 
                
        if self.t == '22' :
            if p == '23' or p == '32':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                    
        if self.t == '44' :
            if p == '43' or p == '34':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)

        if self.t == '55' :
            if p == '53' or p == '35':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '66' :
            if p == '63' or p == '36':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        # Posicion de una linia #2
        if self.t == '06' :
            if p == '03' or p == '36':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '15' :
            if p == '13' or p == '35':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '24' :
            if p == '23' or p == '34':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '42' :
            if p == '32' or p == '43':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '51' :
            if p == '31' or p == '53':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)

        if self.t == '60' :
            if p == '30' or p == '63':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        # Posiciones del centro 
        if self.t == '03' :
            if p == '00' or p == '13' or p == '06':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)

        if self.t == '13' :
            if p == '03' or p == '11' or p == '15' or p == '23':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '23' :
            if p == '13' or p == '22' or p == '24':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '43' :
            if p == '42' or p == '45' or p == '53' or p == '44':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp) 
        
        if self.t == '53' :
            if p == '51' or p == '43' or p == '55' or p == '63':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp) 
                
        if self.t == '63' :
            if p == '60' or p == '53' or p == '66':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        # Posiciones del centro #2
        if self.t == '30' :
            if p == '00' or p == '60' or p == '31':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)  
        
        if self.t == '31' :
            if p == '30' or p == '11' or p == '51' or p == '32':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        
        if self.t == '32' :
            if p == '31' or p == '42' or p == '22' :
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)    
                
        if self.t == '34' :
            if p == '24' or p == '44' or p == '35':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        
        if self.t == '35' :
            if p == '34' or p == '15' or p == '36' or p == '55':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        
        if self.t == '36' :
            if p == '06' or p == '35' or p == '66':
                Ficha1.Imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('This move cannot')
                Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)

    def Imprimidor(self,nombre2,ficha2,ip,l,ls,hj,ppp):
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
                print('KEEP PLAYING UNTIL 2 TABS REMAIN')
                Ficha1.Imprimir()
                if l == '●':
                    Ficha1.Verificaciones_de_Eliminar(z,'●',100,'●','○',ml,self.ioo)
                else:
                    if l == '○':
                        Ficha1.Verificaciones_de_Eliminar(ml,'○',100,'○','●',z,self.iopp)
        else:
            print('THIS POSITION CANNOT BE')
            Ficha1.Verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)

    def Verificaciones_de_Eliminar(self,nombre2,ficha2,ip,l,ls,hj,ppp):
        global blanca
        global negra1
        
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
                    Ficha1.Elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)
                    
        else:
            if l == '●':
                    if negra1 == 6:
                        system('cls')
                        print('KEEP PLAYING UNTIL 2 TABS REMAIN')
                        Ficha1.Imprimir()
                        Ficha1.Funcion_jugadores(ml,'○',100,'○','●',z,self.iopp)
                    else:
                        system('cls')
                        print('KEEP PLAYING UNTIL 2 TABS REMAIN')
                        Ficha1.Imprimir()
                        Ficha1.Verificaciones(ml,'○',100,'○','●',z,self.iopp)
            else:
                    if blanca == 6:
                        system('cls')
                        print('KEEP PLAYING UNTIL 2 TABS REMAIN')
                        Ficha1.Imprimir()
                        Ficha1.Funcion_jugadores(z,'●',100,'●','○',ml,self.ioo)
                    else:
                        system('cls')
                        print('KEEP PLAYING UNTIL 2 TABS REMAIN')
                        Ficha1.Imprimir()
                        Ficha1.Verificaciones(z,'●',100,'●','○',ml,self.ioo)

    def Elimanar_enemigo(self,nombre2,ficha2,ip,l,ls,hj,ppp):
        global blanca
        global negra1
        o = input("Enter the column and row you want to remove from: " + hj)
        if len(o) < 2 or len(o) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Ficha1.Elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)
        self.qw = o[0]
        self.qwe = o[1]
        if (self.qw not in self.verificacion or self.qwe not in self.verificacion or 
            self.qw == '' or self.qwe == '' or self.qw == '\n' and self.qw == '\n'):
            print('THIS PLAY IS INVALID')
            Ficha1.Elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)
        else:
            if ls == '●':
                ls = '●'
                segundaficha =self.ioo
            else:
                if ls == '○':
                    ls == '○'
                    segundaficha = self.iopp
            if (self.matrix[int(self.qw)][int(self.qwe)] == ls or self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " "  
                or self.matrix[int(self.qw)][int(self.qwe)] ==  segundaficha or self.matrix[int(self.qw)][int(self.qwe)] ==  " " +segundaficha + " "):
                if self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " " or self.matrix[int(self.qw)][int(self.qwe)] == " " + segundaficha + " ":
                    self.matrix[int(self.qw)][int(self.qwe)] = " · "
                else:
                    self.matrix[int(self.qw)][int(self.qwe)] = "·"
                    if self.p == '31' or self.p == '35': 
                        self.matrix[int(self.pl)][int(self.pls)] =  " " + ppp + " " 
                    else:
                        self.matrix[int(self.pl)][int(self.pls)] = ppp
                    system('cls')
                    print('KEEP PLAYING UNTIL 2 TABS REMAIN')
                    Ficha1.Imprimir()
                    if ls == '○':
                        negra1 = negra1 + 1
                        color1 = negra1
                    else:
                        blanca = blanca + 1
                        color1 = blanca
                    if color1 == 2:
                        Contadores1.Contador_de_movimiento()
                    else:  
                        if color1 == 6:
                            if ls == '○':
                                print('YOU HAVE 3 TABS YOU CAN MOVE WHERE YOU WANT')
                                Ficha1.Funcion_jugadores(ml,'○',100,'○','●',z,self.iopp)
                            else:
                                print('YOU HAVE 3 TABS YOU CAN MOVE WHERE YOU WANT')
                                Ficha1.Funcion_jugadores(z,'●',100,'●','○',ml,self.ioo)
                        else:
                            if ls == '○':
                                Ficha1.Verificaciones(ml,'○',100,'○','●',z,self.iopp)
                            else:
                                Ficha1.Verificaciones(z,'●',100,'●','○',ml,self.ioo)
            else:
                print('THIS SHEET IS NOT YOUR ENEMY')  
                Ficha1.Elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)

    def Funcion_jugadores(self,nombre2,ficha2,ip,l,ls,hj,ppp):      
        print('play ' + nombre2 + ' = ' + ficha2)
        t = input("the row and column "+ nombre2 +" you want to move:")
        if len(t) < 2 or len(t) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Ficha1.Funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
        self.wss = t[0]
        self.waa = t[1]
        if (self.wss not in self.verificacion or self.waa not in self.verificacion or 
            self.wss == '' or self.waa == '' or self.wss == '\n' and self.wss== '\n'):
            print('THIS PLAY IS INVALID')
            Ficha1.Funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
        else:
            self.t = self.wss + self.waa
            if ficha2 == '●':
                if self.t in self.jugadas_posibles:
                    if (self.matrix[int(self.wss)][int(self.waa)] == ficha2 or self.matrix[int(self.wss)][int(self.waa)] == " " + ficha2 + " " or
                        self.matrix[int(self.wss)][int(self.waa)] == self.ioo or self.matrix[int(self.wss)][int(self.waa)] == " " + self.ioo + " "):
                        self.io = ficha2
                        
                        print('THIS FEET IF ITS YOURS')
                        Ficha1.Imprimir_de_tres(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('THIS SHEET IS NOT YOURS')
                        Ficha1.Funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    print('THIS POSITION DOES NOT EXIST OR IS NOT PERMITTED')
                    Ficha1.Funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                if self.t in self.jugadas_posibles:
                    if (self.matrix[int(self.wss)][int(self.waa)] == ficha2 or self.matrix[int(self.wss)][int(self.waa)] == " " + ficha2 + " " or
                        self.matrix[int(self.wss)][int(self.waa)] == self.iopp or self.matrix[int(self.wss)][int(self.waa)] == " " + self.iopp + " "):
                        print('THIS FEET IF ITS YOURS')
                        self.iop == ficha2
                        Ficha1.Imprimir_de_tres(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('THIS SHEET IS NOT YOURS')
                        Ficha1.Funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    print('THIS POSITION DOES NOT EXIST OR IS NOT PERMITTED')
                    Ficha1.Funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)

    def Imprimir_de_tres(self,nombre2,ficha2,ip,l,ls,hj,ppp): 
        q = input("Which row and column do you want to move it to:")
        if len(q) < 2 or len(q) > 2 :
            print("Please enter two numbers 'columns and rows' ")
            Ficha1.Funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
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
                print('KEEP PLAYING UNTIL 2 TABS REMAIN')
                Ficha1.Imprimir()
                if l == '●':
                    Ficha1.Verificaciones_de_Eliminar(z,'●',100,'●','○',ml,self.ioo)
                else:
                    if l == '○':
                        Ficha1.Verificaciones_de_Eliminar(ml,'○',100,'○','●',z,self.iopp)

class Contadores(Tablero):
    def Contador_de_jugadas(self):
        global c_jugador1
        global c_jugador2      
        i = 0 
        while i < 4:
            i+=1
            while c_jugador1 + 1 >  c_jugador2:
                Ficha1.Piezas_en_el_Tablero('●',z,4,'●','○',ml,self.io)
                c_jugador1-=1
            while  c_jugador2 > c_jugador1:
                Ficha1.Piezas_en_el_Tablero('○',ml,4,'○','●',z,self.iop)
                c_jugador2-=1

    def Contador_de_movimiento(self):
        global blanca
        global negra1
        m_jugador1 = 100
        m_jugador2 = 100
        p = 0
        if blanca >= 2 or negra1 >= 2:
            print("l")
            if blanca >= 2:
                system("cls")
                print('CONGRATULATIONS YOU WON ' + ml)
                sys.exit()
            else:
                system("cls")
                print('CONGRATULATIONS YOU WON ' + z)
                sys.exit()
                
        while p < 100:
            p+=1
            while m_jugador1 +1 >  m_jugador2:
                Ficha1.Verificaciones(z,'●',100,'●','○',ml,self.ioo)
                m_jugador1-=1 
            while m_jugador2 > m_jugador1:
                Ficha1.Verificaciones(ml,'○',100,'○','●',z,self.iopp)
                m_jugador2-=1

Estetica1 = Estetica()
Tablero1 = Tablero()
Ficha1 = Fichas()
Contadores1 = Contadores()

Estetica1.Piesas()
Tablero1.Imprimir()
Contadores1.Contador_de_jugadas()
Contadores1.Contador_de_movimiento()