# from os import system
# from Estructura import tablero
# from Estructura import estetica
# from movimientos import movimientos
# class fichas(tablero):
#     def jugadores(self):
#         c_judador1 = 9
#         c_judador2 = 9
#         i = 0
#         while i < 9:
#             i+=1
#             while c_judador1 + 1 > c_judador2:
#                     lk = input('FILA DEL 1 JUGADOR:')
#                     lj= input('COLUNA DEL 1 JUGADOR:')
#                     if lk not in self.verificacion or lj not in self.verificacion or lk == '' and lk == '' or lk == '\n' and lk == '\n':
#                         print ('ESTA JUGADA ES INVALIDA')
#                     else:
#                         if self.matrix[int(lk)][int(lj)] == "·" or self.matrix[int(lk)][int(lj)] == " · ":
#                             if self.matrix[int(lk)][int(lj)] == " · ":
#                                 self.matrix[int(lk)][int(lj)] = " " + '●' + " "
#                             else:
#                                 self.matrix[int(lk)][int(lj)] = '●'
#                             ficha1.imprimir()
#                             system('cls')
#                             estetica1.piesas()
#                             ficha1.imprimir()
#                             c_judador1-=1
#                         else:
#                             print('JUGADA INVALIDA')
                
#             while c_judador2 > c_judador1:
#                     lk = input('FILA DEL 2 JUGADOR:')
#                     lj= input('COLUNA DEL 2 JUGADOR:')
#                     if lk not in self.verificacion or lj not in self.verificacion or lk == ' ' and lk == ' ' or lk == '\n' and lk == '\n':
#                         print ('ESTA JUGADA ES INVALIDA')
#                     else:
#                         if self.matrix[int(lk)][int(lj)] == "·" or self.matrix[int(lk)][int(lj)] == " · ":
#                             if self.matrix[int(lk)][int(lj)] == " · ":
#                                 self.matrix[int(lk)][int(lj)] = " " + '○' + " " 
#                             else:
#                                 self.matrix[int(lk)][int(lj)] = '○'
#                             ficha1.imprimir()
#                             system('cls')
#                             estetica1.piesas()
#                             ficha1.imprimir()
#                             c_judador2-=1
#                         else:
#                             print('JUGADA INVALIDAD')
                            
            
# estetica1 = estetica()
# tablero1 = tablero()
# ficha1 = fichas()
#llamas
# estetica1.piesas()
# tablero1.imprimir()
# ficha1.jugadores() 
