from os import system

class estetica:
    def piesas(self):
        print ('JUGADOR 1 =' " ●●●●●●●●●")
        print('JUGADOR 2 =' " ○○○○○○○○○")

z = input("Nombre del jugador1:")
e = input("Nombre del jugador2:")
system("cls")

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
    def piezas_en_el_tablero(self):
        c_judador1 = 9
        c_judador2 = 9
        i = 0
        while i < 1:
            i+=1
            while c_judador1 + 1 > c_judador2:
                    self.lk = input('FILA DE : ' + z)
                    self.lj= input('COLUNA DE : '+ z)
                    if (self.lk not in self.verificacion or self.lj not in self.verificacion or 
                        self.lk == '' and self.lk == '' or self.lk == '\n' and self.lk == '\n'):
                        print ('ESTA JUGADA ES INVALIDA')
                    else:
                        if self.matrix[int(self.lk)][int(self.lj)] == "·" or self.matrix[int(self.lk)][int(self.lj)] == " · ":
                            if self.matrix[int(self.lk)][int(self.lj)] == " · ":
                                self.matrix[int(self.lk)][int(self.lj)] = " " + '●' + " "
                            else:
                                self.matrix[int(self.lk)][int(self.lj)] = '●'
                            #llamas
                            ficha1.imprimir()
                            system('cls')
                            estetica1.piesas()
                            ficha1.imprimir()
                            c_judador1-=1
                        else:
                            print('JUGADA INVALIDA')
                
            while c_judador2 > c_judador1:
                    self.lk = input('FILA DE: ' + e)
                    self.lj= input('COLUNA DE: ' + e)
                    if(self.lk not in self.verificacion or self.lj not in self.verificacion or
                    self.lk == ' ' and self.lk == ' ' or self.lk == '\n' and self.lk == '\n'):
                        print ('ESTA JUGADA ES INVALIDA')
                    else:
                        if self.matrix[int(self.lk)][int(self.lj)] == "·" or self.matrix[int(self.lk)][int(self.lj)] == " · ":
                            if self.matrix[int(self.lk)][int(self.lj)] == " · ":
                                self.matrix[int(self.lk)][int(self.lj)] = " " + '○' + " " 
                            else:
                                self.matrix[int(self.lk)][int(self.lj)] = '○'
                            #llamas
                            ficha1.imprimir()
                            system('cls')
                            estetica1.piesas()
                            ficha1.imprimir()
                            c_judador2-=1
                        else:
                            print('JUGADA INVALIDAD')

    def movimientos(self):
        print('juega ' + z + ' = ●')
        self.ws = input('LA FILA DE '+ z + ' QUE TU QUIERES MOVER:')
        self.wa = input('LA COLUNA DE ' + z + ' QUE TU QUIERES MOVER:')
        # if self.matrix[int(self.ws)][int(self.wa)] == self.matrix[int(0)][int(0)]:
        #     self.matrix[int(self.ws)][int(self.wa)] = "·"
        #     print('SOLO TIENE DOS JUGADAS = 0,3 O 3,0')
        #     ws = int(input('cual fila quieres'))
        #     wa = int(input('cual coluna quieres '))
        #     if ws == 0 and wa == 3 or ws == 3 and wa == 0:
        #         if self.matrix[int(ws)][int(wa)] == "·" or self.matrix[int(ws)][int(wa)] == " · ":
        #             self.matrix[int(ws)][int(wa)] = '●'
        #             system('cls')
        #             ficha1.imprimir()
        #         else:
        #             print('ESTA POSICION NO SE PUEDE')
        #     else:
        #         print('ESTA POSICION NO SE PUEDE')
        # else:
        #     print('ESTA POSICION NO SE PUEDE')
            
        if self.matrix[int(self.ws)][int(self.wa)] == self.matrix[int(3)][int(0)]:
            self.matrix[int(self.ws)][int(self.wa)] = "·"
            print('SOLO TIENES ESTAS JUGADAS = 0,0 O 3,1 O 6,0')
            ws = int(input('cual fila quieres'))
            wa = int(input('cual coluna quieres '))
            if ws == 0 and wa == 0 or ws == 3 and wa == 1 or ws == 6 and wa == 0:
                if self.matrix[int(ws)][int(wa)] == "·" or self.matrix[int(ws)][int(wa)] == " · ":
                    self.matrix[int(ws)][int(wa)] = '●'
                    system('cls')
                    ficha1.imprimir()
                else:
                    print('ESTA POSICION NO SE PUEDE')
            else:
                print('ESTA POSICION NO SE PUEDE')
        else:
            print('ESTA POSICION NO SE PUEDE')

    # def Moviemientos_de_las_piezas(self):
    #     contador_player1 = 20
    #     contador_player2 = 20
    #     contador = 0
    #     while contador < 4:
    #         contador+=1
    #         while contador_player1 + 1 > contador_player2:
    #             ws = input('LA FILA DEL JUGADOR 1 QUE TU QUIERES MOVER:')
    #             wa = input('LA COLUNA DEL JUGADOR 1 QUE TU QUIERES MOVER:')
    #             if ws not in self.verificacion or wa not in self.verificacion or ws == ' ' and wa == ' ' or ws == '\n' or wa == '\n':
    #                 print('ESTA PIEZA NO ES TUYA O NO ES PERMITIDAD')
    #             else:
    #                 if self.matrix[int(ws)][int(wa)] == '●' or self.matrix[int(ws)][int(wa)] == ' ● ':
    #                     print('ESTA PIEZA NO ES TUYA O NO ES PERMITIDAD')
    #                 else:
    #                     if ws not in self.verificacion or wa not in self.verificacion or ws == ' ' and wa == ' ' or ws == '\n' or wa == '\n':
    #                         print('ESTA PIEZA NO ES TUYA ')
    #                     else:
    #                         if self.matrix[int(ws)][int(wa)] == "·" or self.matrix[int(ws)][int(wa)] == " · ":
    #                             print('ESTA POSICION NO ES PERMITIDA')
    #                         else:
    #                             print('ESTA PIEZA SI ES TU YA')
    #                             self.matrix[int(ws)][int(wa)] = "·"
    #                             ws= input('LA FILA DEL JUGADOR 1 A DONDE QUIERES MOVER:')
    #                             wa = input('LA COLUNA DEL JUGADOR 1 A DONDE QUIERES MOVER:')
    #                             if self.matrix[int(ws)][int(wa)] == "·" or self.matrix[int(ws)][int(wa)] == " · ":
    #                                 if self.matrix[int(ws)][int(wa)] == " · ":
    #                                     self.matrix[int(ws)][int(wa)] = " " + "○" + " "
    #                                 else:
    #                                     self.matrix[int(ws)][int(wa)] = "○"
    #                                 ficha1.imprimir()
    #                                 system('cls')
    #                                 ficha1.imprimir()
    #                                 contador_player1-=1
    #                             else:
    #                                 print('ESTA PIEZA NO ES TU YA')
    #         while contador_player2 > contador_player1:
    #             ws = input('LA FILA DEL JUGADOR 2 QUE TU QUIERES MOVER:')
    #             wa = input('LA COLUNA DEL JUGADOR 2 QUE TU QUIERES MOVER:')
    #             if ws not in self.verificacion or wa not in self.verificacion or ws == ' ' and wa == ' ' or ws == '\n' or wa == '\n':
    #                 print('ESTA PIEZA NO ES TUYA O NO ES PERMITIDAD')
    #             else:
    #                 if self.matrix[int(ws)][int(wa)] == '○' or self.matrix[int(ws)][int(wa)] == " ○ ":
    #                     print('ESTA PIEZA NO ES TUYA O NO ES PERMITIDAD')
    #                 else:
    #                     if ws not in self.verificacion or wa not in self.verificacion or ws == ' ' and wa == ' ' or ws == '\n' or wa == '\n':
    #                         print('ESTA PIEZA NO ES TUYA ')
    #                     else:
    #                         if self.matrix[int(ws)][int(wa)] == "·" or self.matrix[int(ws)][int(wa)] == " · ":
    #                             print('ESTA POSICION NO ES PERMITIDA')
    #                         else:
    #                             print('ESTA PIEZA SI ES TU YA')
    #                             self.matrix[int(ws)][int(wa)] = "·"
    #                             ws= input('LA FILA DEL JUGADOR 2 A DONDE QUIERES MOVER:')
    #                             wa = input('LA COLUNA DEL JUGADOR 2 A DONDE QUIERES MOVER:')
    #                             if self.matrix[int(ws)][int(wa)] == "·" or self.matrix[int(ws)][int(wa)] == " · ":
    #                                 if self.matrix[int(ws)][int(wa)] ==  " · ":
    #                                     self.matrix[int(ws)][int(wa)] = " " + '●' + " "
    #                                 else:
    #                                     self.matrix[int(ws)][int(wa)] = '●'
    #                                     # self.matrix[int(ws)][int(wa)] = "·"
    #                                 ficha1.imprimir()
    #                                 system('cls')
    #                                 ficha1.imprimir()
    #                                 contador_player2-=1 
    #                             else:
    #                                 print('ESTA PIEZA NO ES TU YA')
                                    
#objetos

estetica1 = estetica()
tablero1 = tablero()
ficha1 = fichas()
#llamas

estetica1.piesas()
tablero1.imprimir()
ficha1.piezas_en_el_tablero()
ficha1.movimientos()
# ficha1.Moviemientos_de_las_piezas()


