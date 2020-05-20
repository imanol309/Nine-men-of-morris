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
        self.jugadas_posibles = ('00','03','06','11','13','15','22','23','24','30','31','32','34','35','36','42','43','44','51','53','55','60','63','66')
    def imprimir(self):
        r = 0
        for e in range(0,len(self.matrix)):
            print(r,end=" ")
            r+=1
            for i in range(0,len(self.matrix)):
                print(self.matrix[e][i],end=' ')
            print('')
        print("  "'0',' 1',' 2','3','4',' 5',' 6')
l = '●' or '○'
print(l)
class fichas(tablero): 
    def piezas_en_el_tablero(self,jugador1,nombre_jugador,po):
        self.lk = input('FILA DE : ' + nombre_jugador)
        self.lj= input('COLUNA DE : '+ nombre_jugador)
        if (self.lk not in self.verificacion or self.lj not in self.verificacion or 
            self.lk == '' or self.lj == '' or self.lk == '\n' and self.lk == '\n'):
            print('ESTA JUGADA ES INVALIDA')
            ficha1.piezas_en_el_tablero(jugador1,nombre_jugador,po) 
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
                
            else:
                print('JUGADA INVALIDA')
                ficha1.piezas_en_el_tablero(jugador1,nombre_jugador,po) 

    def verificaciones_de_eliminar(self,nombre2,ficha2,ip,l,ls,hj):
        s = self.matrix
        self.Fila_de_tres1 =  [[[s[0][0] == l],[s[0][3] == l],[s[0][6] == l]],
                                [[s[1][1] == l],[s[1][3] == l],[s[1][5] == l]],
                                [[s[2][2] == l],[s[2][3] == l],[s[2][4] == l]],
                                [[s[3][0] == l],[s[3][1] == l],[s[3][2] == l]],
                                [[s[3][4] == l],[s[3][5] == l],[s[3][6] == l]],
                                [[s[4][2] == l],[s[4][3] == l],[s[4][4] == l]],
                                [[s[5][1] == l],[s[5][3] == l],[s[5][5] == l]],
                                [[s[6][0] == l],[s[6][3] == l],[s[6][6] == l]],
                                [[s[0][0] == l],[s[3][0] == l],[s[6][0] == l]],
                                [[s[1][1] == l],[s[3][1] == l],[s[5][1] == l]],
                                [[s[2][2] == l],[s[3][2] == l],[s[4][2] == l]],
                                [[s[0][3] == l],[s[1][3] == l],[s[2][3] == l]],
                                [[s[4][3] == l],[s[5][3] == l],[s[6][3] == l]],
                                [[s[2][4] == l],[s[3][4] == l],[s[4][4] == l]],
                                [[s[1][5] == l],[s[3][5] == l],[s[5][5] == l]],
                                [[s[0][6] == l],[s[3][6] == l],[s[6][6] == l]]]
        if l == '●':
            for fila in self.Fila_de_tres1:
                if [fila[0], fila[1], fila[2]]== [[True], [True], [True]]:
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,'○',ml)
            else:
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
        else:
            if l == '○':
                for fila in self.Fila_de_tres1:
                    if [fila[0], fila[1], fila[2]]== [[True], [True], [True]]:
                        ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,'●',z)
                else:
                    ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
            
    def verificaciones(self,nombre2,ficha2,ip,l,ls,hj):
            print('juega ' + nombre2 + ' = ' + ficha2)
            self.ws = input('LA FILA DE '+ nombre2 + ' QUE TU QUIERES MOVER:')
            self.wa = input('LA COLUNA DE ' + nombre2 + ' QUE TU QUIERES MOVER:')
            if (self.ws not in self.verificacion or self.wa not in self.verificacion or 
                self.ws == '' or self.wa == '' or self.ws == '\n' and self.ws== '\n'):
                print('ESTA JUGADA ES INVALIDA')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
            else:
                self.t = self.ws + self.wa
                if self.t in self.jugadas_posibles:
                    if self.matrix[int(self.ws)][int(self.wa)] == ficha2 or self.matrix[int(self.ws)][int(self.wa)] == " " + ficha2 + " ":
                        print('ESTA PIESA SI ES TUYA')
                        ficha1.posiciones_de_movimientos(nombre2,ficha2,ip,l,ls,hj)
                    else:
                        print('ESTA FICHA NO ES TUYA')
                        ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                else:
                    print('ESTA POSICION NO EXISTE O NO ES PERMITIDAD')
                    ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
            
                
    def posiciones_de_movimientos(self,nombre2,ficha2,ip,l,ls,hj): 
        print('juega ' + nombre2 + ' = ' + ficha2)
        self.pl = input('A CUAL FILA LA QUIERES MOVER:')
        self.pls = input('A CUAL COLUNA LA QUIERES MOVER:') 
        p = (self.pl + self.pls)
        # Posicion de una linia #1
        if p == '2020':
            ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
            
        if self.t == '00' :
            if p == '03' or p == '30':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                
        if self.t == '11' :
            if p == '13' or p == '31':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj) 
                
        if self.t == '22' :
            if p == '23' or p == '32':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                    
        if self.t == '44' :
            if p == '43' or p == '34':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)

        if self.t == '55' :
            if p == '53' or p == '35':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                
        if self.t == '66' :
            if p == '63' or p == '36':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
        # Posicion de una linia #2
        if self.t == '06' :
            if p == '03' or p == '36':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                
        if self.t == '15' :
            if p == '13' or p == '35':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                
        if self.t == '24' :
            if p == '23' or p == '34':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                
        if self.t == '42' :
            if p == '32' or p == '43':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                
        if self.t == '51' :
            if p == '31' or p == '53':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)

        if self.t == '60' :
            if p == '30' or p == '63':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
        # Posiciones del centro 
        if self.t == '03' :
            if p == '00' or p == '13' or p == '06':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)

        if self.t == '13' :
            if p == '03' or p == '11' or p == '15' or p == '23':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                
        if self.t == '23' :
            if p == '13' or p == '22' or p == '24':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                
        if self.t == '43' :
            if p == '42' or p == '45' or p == '53':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj) 
        
        if self.t == '53' :
            if p == '51' or p == '43' or p == '55' or p == '63':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj) 
                
        if self.t == '63' :
            if p == '60' or p == '53' or p == '66':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
        # Posiciones del centro #2
        if self.t == '30' :
            if p == '00' or p == '60' or p == '31':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)  
        
        if self.t == '31' :
            if p == '30' or p == '11' or p == '51' or p == '32':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
        
        if self.t == '32' :
            if p == '31' or p == '42' or p == '22' :
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)    
                
        if self.t == '34' :
            if p == '24' or p == '44' or p == '35':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
        
        if self.t == '35' :
            if p == '34' or p == '15' or p == '36' or p == '55':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
        
        if self.t == '36' :
            if p == '06' or p == '35' or p == '66':
                ficha1.imprimidor(nombre2,ficha2,ip,l,ls,hj)
            else:
                print('Esta jugada no se puede')
                ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)
                
    def imprimidor(self,nombre2,ficha2,ip,l,ls,hj):
    
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
        else:
            print('ESTA POSICION NO SE PUEDE')
            ficha1.verificaciones(nombre2,ficha2,ip,l,ls,hj)

    def elimanar_enemigo(self,nombre2,ficha2,ip,l,ls,hj):
        self.qw = input('CUAL FILA DE '+ hj +' QUIERES ELIMINAR:')
        self.qwe = input ('CUAL COLUNA DE '+ hj + ' QUIERES ELIMINAR:')
        if (self.qw not in self.verificacion or self.qwe not in self.verificacion or 
            self.qw == '' or self.qwe == '' or self.qw == '\n' and self.qw == '\n'):
            print('ESTA JUGADA ES INVALIDA')
            ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj)
        else:
             if self.matrix[int(self.qw)][int(self.qwe)] == " " + '●' + " " or self.matrix[int(self.qw)][int(self.qwe)] ==  '●':
                if self.matrix[int(self.qw)][int(self.qwe)] == ls or self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " ":
                    if self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " ":
                        self.matrix[int(self.qw)][int(self.qwe)] = " · "
                    else:
                        self.matrix[int(self.qw)][int(self.qwe)] = "·"
                    system('cls')
                    print('SIGAN JUGADAS HASTA QUE QUEDEN 2 FICHAS')
                    ficha1.imprimir()
                    ficha1.verificaciones_de_eliminar(z,'●',100,'●','○',ml)
                else:
                    print('ESTA FICHA NO ES DE TU ENEMIGO')  
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj)
             else:
                if self.matrix[int(self.qw)][int(self.qwe)] == ls or self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " ":
                    if self.matrix[int(self.qw)][int(self.qwe)] == " " + ls + " ":
                        self.matrix[int(self.qw)][int(self.qwe)] = " · "
                    else:
                        self.matrix[int(self.qw)][int(self.qwe)] = "·"
                    system('cls')
                    print('SIGAN JUGADAS HASTA QUE QUEDEN 2 FICHAS')
                    ficha1.imprimir()
                    ficha1.verificaciones_de_eliminar(ml,'○',100,'○','●',z)
                else:
                    print('ESTA FICHA NO ES DE TU ENEMIGO')  
                    ficha1.elimanar_enemigo(nombre2,ficha2,ip,l,ls,hj)
class contadores():
    def contador_de_jugadas(self):
        c_jugador1 = 9
        c_jugador2 = 9
        i = 0
        while i < 3:
            i+=1
            while c_jugador1 + 1 >  c_jugador2:
                ficha1.piezas_en_el_tablero('●',z,9)
                c_jugador1-=1
            while  c_jugador2 > c_jugador1:
                ficha1.piezas_en_el_tablero('○',ml,9)
                c_jugador2-=1

    def contador_de_movimiento(self):
        m_jugador1 = 100
        m_jugador2 = 100
        p = 0
        while p < 100:
            p+=1
            while m_jugador1 +1 >  m_jugador2:
                ficha1.verificaciones_de_eliminar(z,'●',100,l,'○',ml)
                m_jugador1-=1
            while m_jugador2 > m_jugador1:
                ficha1.verificaciones_de_eliminar(ml,'○',100,l,'●',z)
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



