from os import system
z = input("Nombre del jugador1:")
ml = input("Nombre del jugador2:")
system("cls")

class estetica():
    def piesas(self):
        print ('PIESAS DE ' + z +" = ●●●●●●●●●")
        print('PIESAS DE ' + ml +" = ○○○○○○○○○")

class tablero():
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
        self.numero_blanca = 0
        self.numero_negra = 0
    def imprimir(self):
        r = 0
        for e in range(0,len(self.matrix)):
            print(r,end=" ")
            r+=1
            for i in range(0,len(self.matrix)):
                print(self.matrix[e][i],end=' ')
            print('')
        print("  "'0',' 1',' 2','3','4',' 5',' 6')
        
class fichas(tablero): 
    def piezas_en_el_tablero(self,jugador1,nombre_jugador,po,l1,enemigo,nl,pp):
        self.lk = input('FILA DE : ' + nombre_jugador)
        self.lj= input('COLUNA DE : '+ nombre_jugador)
        if (self.lk not in self.verificacion or self.lj not in self.verificacion or 
            self.lk == '' or self.lj == '' or self.lk == '\n' and self.lj == '\n'):
            print('ESTA JUGADA ES INVALIDA')
            ficha1.piezas_en_el_tablero(jugador1,nombre_jugador,po,l1,enemigo,nl,pp) 
        else:
            if self.matrix[int(self.lk)][int(self.lj)] == "·" or self.matrix[int(self.lk)][int(self.lj)] == " · ":
                if self.matrix[int(self.lk)][int(self.lj)] == " · ":
                    self.matrix[int(self.lk)][int(self.lj)] = " " + jugador1 + " "
                else:
                    self.matrix[int(self.lk)][int(self.lj)] = jugador1
                #llamadas
                ficha1.imprimir()
                system('cls')
                estetica1.piesas()
                ficha1.imprimir()
                if l1 == '●':
                    ficha1.eliminar(jugador1,nombre_jugador,po,l1,enemigo,nl,pp) 
                if l1 == '○':   
                    ficha1.eliminar(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)
            else:
                print('JUGADA INVALIDA')
                ficha1.piezas_en_el_tablero(jugador1,nombre_jugador,po,l1,enemigo,nl,pp) 
                
    def eliminar(self,jugador1,nombre_jugador,po,l1,enemigo,nl,pp):
            o1 = self.matrix    
            # self.Fia =[o1[0][0]],[o1[0][3]],[o1[0][6]]
            # print(self.Fia)        
            self.F =[[[o1[0][0]],[o1[0][3]],[o1[0][6]]],
                        [[o1[1][1]],[o1[1][3]],[o1[1][5]]],
                        [[o1[2][2]],[o1[2][3]],[o1[2][4]]],
                        [[o1[3][0]],[o1[3][1]],[o1[3][2]]],
                        [[o1[3][4]],[o1[3][5]],[o1[3][6]]],
                        [[o1[4][2]],[o1[4][3]],[o1[4][4]]],
                        [[o1[5][1]],[o1[5][3]],[o1[5][5]]],
                        [[o1[6][0]],[o1[6][3]],[o1[6][6]]],
                        [[o1[0][0]],[o1[3][0]],[o1[6][0]]],
                        [[o1[1][1]],[o1[3][1]],[o1[5][1]]],
                        [[o1[2][2]],[o1[3][2]],[o1[4][2]]],
                        [[o1[0][3]],[o1[1][3]],[o1[2][3]]],
                        [[o1[4][3]],[o1[5][3]],[o1[6][3]]],
                        [[o1[2][4]],[o1[3][4]],[o1[4][4]]],
                        [[o1[1][5]],[o1[3][5]],[o1[5][5]]],
                        [[o1[0][6]],[o1[3][6]],[o1[6][6]]]]
            
            # if o1[int[self.lk]][int[self.lj]] != "·" or o1[int[self.lk]][int[self.lj]] != " · ":
            if l1 == '●' or l1 == '○': 
                self.fila2 = [[l1], [l1], [l1]]
                self.fila4 = [[pp], [l1], [l1]]
                self.fila5 = [[l1], [pp], [l1]]
                self.fila6 = [[l1], [l1], [pp]]
                self.fila7 = [[l1], [pp], [pp]]
                self.fila8 = [[pp], [l1], [pp]]
                self.fila9 = [[pp], [pp], [l1]]
                print(pp)
                print(self.fila2)
                print(self.F[0])
                if (self.fila2 in self.F or self.fila4 in self.F or self.fila5 in self.F 
                    or self.fila6 in self.F or self.fila7 in self.F or self.fila8 in self.F or 
                    self.fila9 in self.F):
                    if (self.fila2 == self.F[0] or self.fila4 == self.F[0]
                        or self.fila5 == self.F[0] or self.fila6 == self.F[0]
                        or self.fila7 == self.F[0] or self.fila8 == self.F[0] or self.fila9 == self.F[0]):
                        o1[0][0] = pp
                        o1[0][3] = pp
                        o1[0][6] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)           
                    if (self.fila2 == self.F[1] or self.fila4 == self.F[1]
                        or self.fila5 == self.F[1] or self.fila6 == self.F[1]
                        or self.fila7 == self.F[1] or self.fila8 == self.F[1] or self.fila9 == self.F[1]):
                        o1[1][1] = pp 
                        o1[1][3] = pp 
                        o1[1][5] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)                                   
                    if (self.fila2 == self.F[2] or self.fila4 == self.F[2]
                        or self.fila5 == self.F[2] or self.fila6 == self.F[2]
                        or self.fila7 == self.F[2] or self.fila8 == self.F[2] or self.fila9 == self.F[2]):
                        o1[2][2] = pp 
                        o1[2][3] = pp 
                        o1[2][4] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)           
                    if (self.fila2 == self.F[3] or self.fila4 == self.F[3]
                        or self.fila5 == self.F[3] or self.fila6 == self.F[3]
                        or self.fila7 == self.F[3] or self.fila8 == self.F[3] or self.fila9 == self.F[3]):
                        o1[3][0] = pp 
                        o1[3][1] = pp 
                        o1[3][2] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)           
                    if (self.fila2 == self.F[4] or self.fila4 == self.F[4]
                        or self.fila5 == self.F[4] or self.fila6 == self.F[4]
                        or self.fila7 == self.F[4] or self.fila8 == self.F[4] or self.fila9 == self.F[4]):
                        o1[3][4] = pp 
                        o1[3][5] = pp 
                        o1[3][6] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)
                    if (self.fila2 == self.F[5] or self.fila4 == self.F[5]
                        or self.fila5 == self.F[5] or self.fila6 == self.F[5]
                        or self.fila7 == self.F[5] or self.fila8 == self.F[5] or self.fila9 == self.F[5]):
                        o1[4][2] = pp 
                        o1[4][3] = pp 
                        o1[4][4] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)           
                    if (self.fila2 == self.F[6] or self.fila4 == self.F[6]
                        or self.fila5 == self.F[6] or self.fila6 == self.F[6]
                        or self.fila7 == self.F[6] or self.fila8 == self.F[6] or self.fila9 == self.F[6]):
                        o1[5][1] = pp 
                        o1[5][3] = pp 
                        o1[5][5] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)           
                    if (self.fila2 == self.F[7] or self.fila4 == self.F[7]
                        or self.fila5 == self.F[7] or self.fila6 == self.F[7]
                        or self.fila7 == self.F[7] or self.fila8 == self.F[7] or self.fila9 == self.F[7]):
                        o1[6][0] = pp 
                        o1[6][3] = pp 
                        o1[6][6] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)       
                    if (self.fila2 == self.F[8] or self.fila4 == self.F[8]
                        or self.fila5 == self.F[8] or self.fila6 == self.F[8]
                        or self.fila7 == self.F[8] or self.fila8 == self.F[8] or self.fila9 == self.F[8]):
                        o1[0][0] = pp 
                        o1[3][0] = pp 
                        o1[6][0] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)           
                    if (self.fila2 == self.F[9] or self.fila4 == self.F[9]
                        or self.fila5 == self.F[9] or self.fila6 == self.F[9]
                        or self.fila7 == self.F[9] or self.fila8 == self.F[9] or self.fila9 == self.F[9]):
                        o1[1][1] = pp 
                        o1[3][1] = pp 
                        o1[5][1] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)           
                    if (self.fila2 == self.F[10] or self.fila4 == self.F[10]
                        or self.fila5 == self.F[10] or self.fila6 == self.F[10]
                        or self.fila7 == self.F[10] or self.fila8 == self.F[10] or self.fila9 == self.F[10]):
                        o1[2][2] = pp 
                        o1[3][2] = pp 
                        o1[4][2] = pp
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)       
                    if (self.fila2 == self.F[11] or self.fila4 == self.F[11]
                        or self.fila5 == self.F[11] or self.fila6 == self.F[11]
                        or self.fila7 == self.F[11] or self.fila8 == self.F[11] or self.fila9 == self.F[11]):
                        o1[0][3] = pp 
                        o1[1][3] = pp 
                        o1[2][3] = pp 
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)       
                    if (self.fila2 == self.F[12] or self.fila4 == self.F[12]
                        or self.fila5 == self.F[12] or self.fila6 == self.F[12]
                        or self.fila7 == self.F[12] or self.fila8 == self.F[12] or self.fila9 == self.F[12]):
                        o1[4][3] = pp 
                        o1[5][3] = pp 
                        o1[6][3] = pp 
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)       
                    if (self.fila2 == self.F[13] or self.fila4 == self.F[13]
                        or self.fila5 == self.F[13] or self.fila6 == self.F[13]
                        or self.fila7 == self.F[13] or self.fila8 == self.F[13] or self.fila9 == self.F[13]):
                        o1[2][4] = pp 
                        o1[3][4] = pp 
                        o1[4][4] = pp  
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)       
                    if (self.fila2 == self.F[14] or self.fila4 == self.F[14]
                        or self.fila5 == self.F[14] or self.fila6 == self.F[14]
                        or self.fila7 == self.F[14] or self.fila8 == self.F[14] or self.fila9 == self.F[14]):
                        o1[1][5] = pp 
                        o1[3][5] = pp 
                        o1[5][5] = pp 
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)           
                    if (self.fila2 == self.F[15] or self.fila4 == self.F[15]
                        or self.fila5 == self.F[15] or self.fila6 == self.F[15]
                        or self.fila7 == self.F[15] or self.fila8 == self.F[15] or self.fila9 == self.F[15]):
                        o1[0][6] = pp 
                        o1[3][6] = pp 
                        o1[6][6] = pp    
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)
           
    def elimanar_enemigo2(self,jugador1,nombre_jugador,po,l1,enemigo,nl,pp):
        self.dr = input('CUAL FILA DE '+ nl +' QUIERES ELIMINAR:')
        self.dre = input ('CUAL COLUNA DE '+ nl + ' QUIERES ELIMINAR:')
        if (self.dr not in self.verificacion or self.dre not in self.verificacion or 
            self.dr == '' or self.dre == '' or self.dr == '\n' and self.dr == '\n'):
            print('ESTA JUGADA ES INVALIDA')
            ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)
        else:
            if self.matrix[int(self.dr)][int(self.dre)] == enemigo or self.matrix[int(self.dr)][int(self.dre)] == " " + enemigo + " ":
                if self.matrix[int(self.dr)][int(self.dre)] == " " + enemigo + " ":
                    self.matrix[int(self.dr)][int(self.dre)] = " · "
                else:
                    self.matrix[int(self.dr)][int(self.dre)] = "·"
                system('cls')
                print('SIGAN JUGADAS HASTA QUE QUEDEN 2 FICHAS')
                ficha1.imprimir()
            else:
                if jugador1 == '●':
                    if self.matrix[int(self.dr)][int(self.dre)] == self.iop or self.matrix[int(self.dr)][int(self.dre)] == " " + self.iop + " ":
                        if self.matrix[int(self.dr)][int(self.dre)] == " " + self.iop + " ":
                            self.matrix[int(self.dr)][int(self.dre)] = " · "
                        else:
                            self.matrix[int(self.dr)][int(self.dre)] = "·"
                        system('cls')
                        print('SIGAN JUGADAS HASTA QUE QUEDEN 2 FICHAS')
                        self.numero_blanca = self.numero_blanca + 1
                        if self.numero_blanca == 6:
                            ficha1.funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
                        else:                                                          
                            ficha1.imprimir()
                    else:
                        print('ESTA FICHA NO ES DE TU ENEMIGO')  
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)
                else:
                    if self.matrix[int(self.dr)][int(self.dre)] == self.io or self.matrix[int(self.dr)][int(self.dre)] == " " + self.io + " ":
                        if self.matrix[int(self.dr)][int(self.dre)] == " " + self.io + " ":
                            self.matrix[int(self.dr)][int(self.dre)] = " · "
                        else:
                            self.matrix[int(self.dr)][int(self.dre)] = "·"
                        system('cls')
                        print('SIGAN JUGADAS HASTA QUE QUEDEN 2 FICHAS')
                        self.numero_negra = self.numero_negra + 1
                        if self.numero_negra == 6:
                            ficha1.funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
                        else:                                                          
                            ficha1.imprimir()
                    else:
                        print('ESTA FICHA NO ES DE TU ENEMIGO')  
                        ficha1.elimanar_enemigo2(jugador1,nombre_jugador,po,l1,enemigo,nl,pp)

#ESTA PARTE ES SOBRE LAS FUNCIONES DE MOVIMIENTOS DEL JUEGO Y ALGUNAS DE ELIMINACION.

    def verificaciones(self,nombre2,ficha2,ip,l,ls,hj,ppp):
            print('juega ' + nombre2 + ' = ' + ficha2)
            self.ws = input('LA FILA DE '+ nombre2 + ' QUE TU QUIERES MOVER:')
            self.wa = input('LA COLUNA DE ' + nombre2 + ' QUE TU QUIERES MOVER:')
            if (self.ws not in self.verificacion or self.wa not in self.verificacion or 
                self.ws == '' or self.wa == '' or self.ws == '\n' and self.ws== '\n'):
                print('ESTA JUGADA ES INVALIDA')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                self.t = self.ws + self.wa
                if ficha2 == '●':
                    if self.t in self.jugadas_posibles:
                        if (self.matrix[int(self.ws)][int(self.wa)] == ficha2 or self.matrix[int(self.ws)][int(self.wa)] == " " + ficha2 + " " or
                            self.matrix[int(self.ws)][int(self.wa)] == self.ioo or self.matrix[int(self.ws)][int(self.wa)] == " " + self.ioo + " "):
                            self.io = ficha2
                            print('ESTA PIESA SI ES TUYA')
                            ficha1.posiciones_de_movimientos(nombre2,ficha2,ip,l,ls,hj,ppp)
                        else:
                            print('ESTA FICHA NO ES TUYA')
                            ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('ESTA POSICION NO EXISTE O NO ES PERMITIDAD')
                        ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    if self.t in self.jugadas_posibles:
                       if (self.matrix[int(self.ws)][int(self.wa)] == ficha2 or self.matrix[int(self.ws)][int(self.wa)] == " " + ficha2 + " " or
                            self.matrix[int(self.ws)][int(self.wa)] == self.iopp or self.matrix[int(self.ws)][int(self.wa)] == " " + self.iopp + " "):
                            print('ESTA PIESA SI ES TUYA')
                            self.iop == ficha2
                            ficha1.posiciones_de_movimientos(nombre2,ficha2,ip,l,ls,hj,ppp)
                       else:
                            print('ESTA FICHA NO ES TUYA')
                            ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('ESTA POSICION NO EXISTE O NO ES PERMITIDAD')
                        ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                        
    def posiciones_de_movimientos(self,nombre2,ficha2,ip,l,ls,hj,ppp): 
        print('juega ' + nombre2 + ' = ' + ficha2)
        self.pl = input('A CUAL FILA LA QUIERES MOVER:')
        self.pls = input('A CUAL COLUNA LA QUIERES MOVER:') 
        p = (self.pl + self.pls)
        self.p = (self.pl + self.pls)
        # Posicion de una linia #1
        if p == '2020':
            ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
            
        if self.t == '00' :
            if p == '03' or p == '30':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '11' :
            if p == '13' or p == '31':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp) 
                
        if self.t == '22' :
            if p == '23' or p == '32':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                    
        if self.t == '44' :
            if p == '43' or p == '34':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)

        if self.t == '55' :
            if p == '53' or p == '35':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '66' :
            if p == '63' or p == '36':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        # Posicion de una linia #2
        if self.t == '06' :
            if p == '03' or p == '36':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '15' :
            if p == '13' or p == '35':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '24' :
            if p == '23' or p == '34':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '42' :
            if p == '32' or p == '43':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '51' :
            if p == '31' or p == '53':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)

        if self.t == '60' :
            if p == '30' or p == '63':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        # Posiciones del centro 
        if self.t == '03' :
            if p == '00' or p == '13' or p == '06':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)

        if self.t == '13' :
            if p == '03' or p == '11' or p == '15' or p == '23':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '23' :
            if p == '13' or p == '22' or p == '24':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
        if self.t == '43' :
            if p == '42' or p == '45' or p == '53' or p == '44':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp) 
        
        if self.t == '53' :
            if p == '51' or p == '43' or p == '55' or p == '63':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp) 
                
        if self.t == '63' :
            if p == '60' or p == '53' or p == '66':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        # Posiciones del centro #2
        if self.t == '30' :
            if p == '00' or p == '60' or p == '31':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)  
        
        if self.t == '31' :
            if p == '30' or p == '11' or p == '51' or p == '32':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        
        if self.t == '32' :
            if p == '31' or p == '42' or p == '22' :
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)    
                
        if self.t == '34' :
            if p == '24' or p == '44' or p == '35':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        
        if self.t == '35' :
            if p == '34' or p == '15' or p == '36' or p == '55':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
        
        if self.t == '36' :
            if p == '06' or p == '35' or p == '66':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
                
    def imprimidor(self,nombre2,ficha2,ip,l,ls,hj,ppp):
        
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
                print('SIGUAN JUGADAS HASTA QUE QUEDEN 2 FICHAS')
                ficha1.imprimir()
                # ficha1.funcion_ganadora(nombre2,ficha2,ip,l,ls,hj,ppp)
                if l == '●':
                    ficha1.verificaciones_de_eliminar(z,'●',100,'●','○',ml,self.ioo)
                else:
                   if l == '○':
                        ficha1.verificaciones_de_eliminar(ml,'○',100,'○','●',z,self.iopp)
        else:
            print('ESTA POSICION NO SE PUEDE')
            ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj,ppp)
            
            
    def verificaciones_de_eliminar(self,nombre2,ficha2,ip,l,ls,hj,ppp):
        s = self.matrix
        self.F =[[[s[0][0]],[s[0][3]],[s[0][6]]],
                [[s[1][1]],[s[1][3]],[s[1][5]]],
                [[s[2][2]],[s[2][3]],[s[2][4]]],
                [[s[3][0]],[s[3][1]],[s[3][2]]],
                [[s[3][4]],[s[3][5]],[s[3][6]]],
                [[s[4][2]],[s[4][3]],[s[4][4]]],
                [[s[5][1]],[s[5][3]],[s[5][5]]],
                [[s[6][0]],[s[6][3]],[s[6][6]]],
                [[s[0][0]],[s[3][0]],[s[6][0]]],
                [[s[1][1]],[s[3][1]],[s[5][1]]],
                [[s[2][2]],[s[3][2]],[s[4][2]]],
                [[s[0][3]],[s[1][3]],[s[2][3]]],
                [[s[4][3]],[s[5][3]],[s[6][3]]],
                [[s[2][4]],[s[3][4]],[s[4][4]]],
                [[s[1][5]],[s[3][5]],[s[5][5]]],
                [[s[0][6]],[s[3][6]],[s[6][6]]]]

        self.fila2 = [[l], [l], [l]]
        self.fila4 = [[ppp], [l], [l]]
        self.fila5 = [[l], [ppp], [l]]
        self.fila6 = [[l], [l], [ppp]]
        self.fila7 = [[l], [ppp], [ppp]]
        self.fila8 = [[ppp], [l], [ppp]]
        self.fila9 = [[ppp], [ppp], [l]]
        print(ppp)
        if (self.fila2 in self.F or self.fila4 in self.F or self.fila5 in self.F 
            or self.fila6 in self.F or self.fila7 in self.F or self.fila8 in self.F or 
            self.fila9 in self.F):
            if (self.fila2 == self.F[0] or self.fila4 == self.F[0]
                or self.fila5 == self.F[0] or self.fila6 == self.F[0]
                or self.fila7 == self.F[0] or self.fila8 == self.F[0] or self.fila9 == self.F[0]):
                    s[0][0] = ppp
                    s[0][3] = ppp
                    s[0][6] = ppp
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)           
            if (self.fila2 == self.F[1] or self.fila4 == self.F[1]
                or self.fila5 == self.F[1] or self.fila6 == self.F[1]
                or self.fila7 == self.F[1] or self.fila8 == self.F[1] or self.fila9 == self.F[1]):
                    s[1][1] = ppp
                    s[1][3] = ppp 
                    s[1][5] = ppp
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)                                   
            if (self.fila2 == self.F[2] or self.fila4 == self.F[2]
                or self.fila5 == self.F[2] or self.fila6 == self.F[2]
                or self.fila7 == self.F[2] or self.fila8 == self.F[2] or self.fila9 == self.F[2]):
                    s[2][2] = ppp 
                    s[2][3] = ppp 
                    s[2][4] = ppp
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)        
            if (self.fila2 == self.F[4] or self.fila4 == self.F[4]
                or self.fila5 == self.F[4] or self.fila6 == self.F[4]
                or self.fila7 == self.F[4] or self.fila8 == self.F[4] or self.fila9 == self.F[4]):
                    s[3][4] = ppp 
                    s[3][5] = ppp 
                    s[3][6] = ppp
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)
            if (self.fila2 == self.F[5] or self.fila4 == self.F[5]
                or self.fila5 == self.F[5] or self.fila6 == self.F[5]
                or self.fila7 == self.F[5] or self.fila8 == self.F[5] or self.fila9 == self.F[5]):
                    s[4][2] = ppp 
                    s[4][3] = ppp 
                    s[4][4] = ppp
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)           
            if (self.fila2 == self.F[6] or self.fila4 == self.F[6]
                or self.fila5 == self.F[6] or self.fila6 == self.F[6]
                or self.fila7 == self.F[6] or self.fila8 == self.F[6] or self.fila9 == self.F[6]):
                    s[5][1] = ppp 
                    s[5][3] = ppp 
                    s[5][5] = ppp
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)           
            if (self.fila2 == self.F[7] or self.fila4 == self.F[7]
                or self.fila5 == self.F[7] or self.fila6 == self.F[7]
                or self.fila7 == self.F[7] or self.fila8 == self.F[7] or self.fila9 == self.F[7]):
                    s[6][0] = ppp
                    s[6][3] = ppp 
                    s[6][6] = ppp
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)       
            if (self.fila2 == self.F[8] or self.fila4 == self.F[8]
                or self.fila5 == self.F[8] or self.fila6 == self.F[8]
                or self.fila7 == self.F[8] or self.fila8 == self.F[8] or self.fila9 == self.F[8]):
                    s[0][0] = ppp 
                    s[3][0] = ppp 
                    s[6][0] = ppp
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)              
            if (self.fila2 == self.F[9] or self.fila4 == self.F[9]
                or self.fila5 == self.F[9] or self.fila6 == self.F[9]
                or self.fila7 == self.F[9] or self.fila8 == self.F[9] or self.fila9 == self.F[9]):
                    s[1][1] = ppp 
                    s[3][1] = ppp 
                    s[5][1] = ppp
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)           
            if (self.fila2 == self.F[10] or self.fila4 == self.F[10]
                or self.fila5 == self.F[10] or self.fila6 == self.F[10]
                or self.fila7 == self.F[10] or self.fila8 == self.F[10] or self.fila9 == self.F[10]):
                    s[2][2] = ppp 
                    s[3][2] = ppp 
                    s[4][2] = ppp
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)       
            if (self.fila2 == self.F[11] or self.fila4 == self.F[11]
                or self.fila5 == self.F[11] or self.fila6 == self.F[11]
                or self.fila7 == self.F[11] or self.fila8 == self.F[11] or self.fila9 == self.F[11]):
                    s[0][3] = ppp 
                    s[1][3] = ppp 
                    s[2][3] = ppp 
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)       
            if (self.fila2 == self.F[12] or self.fila4 == self.F[12]
                or self.fila5 == self.F[12] or self.fila6 == self.F[12]
                or self.fila7 == self.F[12] or self.fila8 == self.F[12] or self.fila9 == self.F[12]):
                    s[4][3] = ppp 
                    s[5][3] = ppp 
                    s[6][3] = ppp 
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)       
            if (self.fila2 == self.F[13] or self.fila4 == self.F[13]
                or self.fila5 == self.F[13] or self.fila6 == self.F[13]
                or self.fila7 == self.F[13] or self.fila8 == self.F[13] or self.fila9 == self.F[13]):
                    s[2][4] = ppp 
                    s[3][4] = ppp 
                    s[4][4] = ppp  
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)      
            if (self.fila2 == self.F[14] or self.fila4 == self.F[14]
                or self.fila5 == self.F[14] or self.fila6 == self.F[14]
                or self.fila7 == self.F[14] or self.fila8 == self.F[14] or self.fila9 == self.F[14]):
                    s[1][5] = ppp 
                    s[3][5] = ppp 
                    s[5][5] = ppp 
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)          
            if (self.fila2 == self.F[15] or self.fila4 == self.F[15]
                or self.fila5 == self.F[15] or self.fila6 == self.F[15]
                or self.fila7 == self.F[15] or self.fila8 == self.F[15] or self.fila9 == self.F[15]):
                    s[0][6] = ppp 
                    s[3][6] = ppp 
                    s[6][6] = ppp    
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)
        else:
            if l == '●':
                if self.numero_negra == 1:
                    ficha1.funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    ficha1.verificaciones(ml,'○',100,'○','●',z,self.iopp)
            else:
                if self.numero_blanca == 1:
                    ficha1.funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    ficha1.verificaciones(z,'●',100,'●','○',ml,self.ioo)

    def elimanar_enemigo(self,nombre2,ficha2,ip,l,ls,hj,ppp):
        self.qw = input('CUAL FILA DE '+ hj +' QUIERES ELIMINAR:')
        self.qwe = input ('CUAL COLUNA DE '+ hj + ' QUIERES ELIMINAR:')
        if (self.qw not in self.verificacion or self.qwe not in self.verificacion or 
            self.qw == '' or self.qwe == '' or self.qw == '\n' and self.qw == '\n'):
            print('ESTA JUGADA ES INVALIDA')
            ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)
        else:
             if (self.matrix[int(self.qw)][int(self.qwe)] == " " + '●' + " " or self.matrix[int(self.qw)][int(self.qwe)] ==  '●' 
                 or self.matrix[int(self.qw)][int(self.qwe)] ==  self.ioo or self.matrix[int(self.qw)][int(self.qwe)] ==  " " + self.ioo + " "):
                if (self.matrix[int(self.qw)][int(self.qwe)] == ls or self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " "  
                    or self.matrix[int(self.qw)][int(self.qwe)] ==  self.ioo or self.matrix[int(self.qw)][int(self.qwe)] ==  " " + self.ioo + " "):
                    if self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " " or self.matrix[int(self.qw)][int(self.qwe)] == " " + self.ioo + " ":
                        self.matrix[int(self.qw)][int(self.qwe)] = " · "
                    else:
                        self.matrix[int(self.qw)][int(self.qwe)] = "·"
                        if l == '●':
                            if self.p == '31' or self.p == '35': 
                                self.matrix[int(self.pl)][int(self.pls)] =  " " + self.ioo + " " 
                            else:
                                self.matrix[int(self.pl)][int(self.pls)] = self.ioo
                        else:
                            if self.p == '31' or self.p == '35': 
                                self.matrix[int(self.pl)][int(self.pls)] =  " " + self.iopp + " " 
                            else:
                                self.matrix[int(self.pl)][int(self.pls)] = self.iopp
                        system('cls')
                        print('SIGAN JUGADAS HASTA QUE QUEDEN 2 FICHAS')
                        self.numero_blanca = self.numero_blanca + 1
                        if self.numero_blanca == 1:
                            print('TE QUEDA 3 FICHAS PUEDES MOVERTE DONDE QUIERAS')
                            ficha1.imprimir()
                            ficha1.funcion_jugadores(z,'●',100,'●','○',ml,self.ioo)
                        else:                                                          
                            ficha1.imprimir()
                            ficha1.verificaciones(z,'●',100,'●','○',ml,self.ioo)
                else:
                    print('ESTA FICHA NO ES DE TU ENEMIGO')  
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)
             else:
                if (self.matrix[int(self.qw)][int(self.qwe)] == ls or self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " "  
                    or self.matrix[int(self.qw)][int(self.qwe)] ==  self.iopp or self.matrix[int(self.qw)][int(self.qwe)] ==  " " + self.iopp + " "):
                    if self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " " or self.matrix[int(self.qw)][int(self.qwe)] == " " + self.iop + " ":
                        self.matrix[int(self.qw)][int(self.qwe)] = " · "
                    else:
                        self.matrix[int(self.qw)][int(self.qwe)] = "·"
                        if l == '●':
                            if self.p == '31' or self.p == '35': 
                                self.matrix[int(self.pl)][int(self.pls)] =  " " + self.ioo + " " 
                            else:
                                self.matrix[int(self.pl)][int(self.pls)] = self.ioo
                        else:
                            if self.p == '31' or self.p == '35': 
                                self.matrix[int(self.pl)][int(self.pls)] =  " " + self.iopp + " " 
                            else:
                                self.matrix[int(self.pl)][int(self.pls)] = self.iopp
                        system('cls')
                        print('SIGAN JUGADAS HASTA QUE QUEDEN 2 FICHAS')
                        self.numero_negra = self.numero_negra + 1
                        if self.numero_negra == 1:
                            ficha1.imprimir()
                            print('TE QUEDA 3 FICHAS PUEDES MOVERTE DONDE QUIERAS')
                            ficha1.funcion_jugadores(ml,'○',100,'○','●',z,self.iopp)
                        else:                                                          
                            ficha1.imprimir()
                            ficha1.verificaciones(ml,'○',100,'○','●',z,self.iopp)
                else:
                    print('ESTA FICHA NO ES DE TU ENEMIGO')  
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj,ppp)

    def funcion_jugadores(self,nombre2,ficha2,ip,l,ls,hj,ppp):      
        print('juega ' + nombre2 + ' = ' + ficha2)
        self.wss = input('LA FILA DE '+ nombre2 + ' QUE TU QUIERES MOVER:')
        self.waa = input('LA COLUNA DE ' + nombre2 + ' QUE TU QUIERES MOVER:')
        if (self.wss not in self.verificacion or self.waa not in self.verificacion or 
            self.wss == '' or self.waa == '' or self.wss == '\n' and self.wss== '\n'):
            print('ESTA JUGADA ES INVALIDA')
            ficha1.funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
        else:
            self.t = self.wss + self.waa
            if ficha2 == '●':
                if self.t in self.jugadas_posibles:
                    if (self.matrix[int(self.wss)][int(self.waa)] == ficha2 or self.matrix[int(self.wss)][int(self.waa)] == " " + ficha2 + " " or
                        self.matrix[int(self.wss)][int(self.waa)] == self.ioo or self.matrix[int(self.wss)][int(self.waa)] == " " + self.ioo + " "):
                        self.io = ficha2
                        
                        print('ESTA PIESA SI ES TUYA')
                        ficha1.imprimir_de_tres(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('ESTA FICHA NO ES TUYA')
                        ficha1.funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    print('ESTA POSICION NO EXISTE O NO ES PERMITIDAD')
                    ficha1.funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
            else:
                if self.t in self.jugadas_posibles:
                    if (self.matrix[int(self.wss)][int(self.waa)] == ficha2 or self.matrix[int(self.wss)][int(self.waa)] == " " + ficha2 + " " or
                        self.matrix[int(self.wss)][int(self.waa)] == self.iopp or self.matrix[int(self.wss)][int(self.waa)] == " " + self.iopp + " "):
                        print('ESTA PIESA SI ES TUYA')
                        self.iop == ficha2
                        ficha1.imprimir_de_tres(nombre2,ficha2,ip,l,ls,hj,ppp)
                    else:
                        print('ESTA FICHA NO ES TUYA')
                        ficha1.funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
                else:
                    print('ESTA POSICION NO EXISTE O NO ES PERMITIDAD')
                    ficha1.funcion_jugadores(nombre2,ficha2,ip,l,ls,hj,ppp)
    def imprimir_de_tres(self,nombre2,ficha2,ip,l,ls,hj,ppp): 
         
        self.pll = input('A CUAL FILA LA QUIERES MOVER:')
        self.plss = input('A CUAL COLUNA LA QUIERES MOVER:') 
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
                print('SIGUAN JUGADAS HASTA QUE QUEDEN 2 FICHAS')
                ficha1.imprimir()
                # ficha1.funcion_ganadora(nombre2,ficha2,ip,l,ls,hj,ppp)
                if l == '●':
                    ficha1.verificaciones_de_eliminar(z,'●',100,'●','○',ml,self.ioo)
                else:
                   if l == '○':
                        ficha1.verificaciones_de_eliminar(ml,'○',100,'○','●',z,self.iopp)     
            
class contadores(tablero):
    def contador_de_jugadas(self):
        c_jugador1 = 9
        c_jugador2 = 9
        i = 0
        while i < 4:
            i+=1
            while c_jugador1 + 1 >  c_jugador2:
                ficha1.piezas_en_el_tablero('●',z,9,'●','○',ml,self.io)
                c_jugador1-=1
            while  c_jugador2 > c_jugador1:
                ficha1.piezas_en_el_tablero('○',ml,9,'○','●',z,self.iop)
                c_jugador2-=1

    def contador_de_movimiento(self):
        m_jugador1 = 100
        m_jugador2 = 100
        p = 0
        while p < 100:
            p+=1
            while m_jugador1 +1 >  m_jugador2:
                ficha1.verificaciones(z,'●',100,'●','○',ml,self.ioo)
                m_jugador1-=1
            while m_jugador2 > m_jugador1:
                ficha1.verificaciones(ml,'○',100,'○','●',z,self.iopp)
                m_jugador2-=1




# objetos
estetica1 = estetica()
tablero1 = tablero()
ficha1 = fichas()
contadores1 = contadores()

#llamadas
estetica1.piesas()
tablero1.imprimir()
contadores1.contador_de_jugadas()
contadores1.contador_de_movimiento()



