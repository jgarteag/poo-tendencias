"""
Manejo y uso de funciones con matrices
autores: Juan Posada / Juan Guerrero
"""

class Matriz:
    __vector = [1, -1, 2, 3, -1, 2, 1, 0]
    __pos_x = 0
    __pos_y = 0

    def __init__(self, filas, columnas):
        """
        Constructor de la clase Matriz
        """
        self.__filas = filas
        self.__columnas = columnas
        self.__matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    def posicion_inicial_p(self, pos_x, pos_y):
        """
        Establecer la posición inicial de 'P' en la matriz
        """
        if 0 <= pos_x < self.__filas and 0 <= pos_y < self.__columnas:
            self.__pos_x = pos_x
            self.__pos_y = pos_y
            self.__matriz[pos_x][pos_y] = 'P'
        else:
            raise ValueError("Las posiciones se salen de la dimension de la matriz.")

    def imprimir_matriz(self):
        """
        Imprimir la matriz en consola
        """
        for i in self.__matriz:
            print(i)

    def mover_P(self):
        """
        Mover 'P' en la matriz según el vector de movimientos
        """
        for i, movimiento in enumerate(self.__vector):
            old_x, old_y = self.__pos_x, self.__pos_y  # Guardar la posición anterior
            if i % 2 == 0:  # Primera posición
                if movimiento > 0:  # Mover arriba
                    self.__pos_x = max(0, self.__pos_x - movimiento)
                    print(f'Movimiento {i+1}: Arriba {old_x - self.__pos_x} posiciones')
                elif movimiento < 0:  # Mover abajo
                    self.__pos_x = min(self.__filas - 1, self.__pos_x - movimiento)
                    print(f'Movimiento {i+1}: Abajo {self.__pos_x - old_x} posiciones')
            else:  # Segunda posición
                if movimiento > 0:  # Mover derecha
                    self.__pos_y = min(self.__columnas - 1, self.__pos_y + movimiento)
                    print(f'Movimiento {i+1}: Derecha {self.__pos_y - old_y} posiciones')
                elif movimiento < 0:  # Mover izquierda
                    self.__pos_y = max(0, self.__pos_y + movimiento)
                    print(f'Movimiento {i+1}: Izquierda {old_y - self.__pos_y} posiciones')

            # Actualizar la matriz
            self.__matriz[old_x][old_y] = 0  # Establecer la posición anterior a 0
            self.__matriz[self.__pos_x][self.__pos_y] = 'P'  # Mover 'P' a la nueva posición
            if i < len(self.__vector) - 1:  # No imprimir la matriz después del último movimiento
                self.imprimir_matriz()
                
    @staticmethod
    def pedir_filas_columnas():
        """
        Pedir al usuario las filas y columnas de la matriz
        """
        while True:
            try:
                filas = int(input("Filas: "))
                if filas <= 0:
                    print("Por favor, ingrese un número mayor que 0 para las filas.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número para las filas.")

        while True:
            try:
                columnas = int(input("Columnas: "))
                if columnas <= 0:
                    print("Por favor, ingrese un número mayor que 0 para las columnas.")
                    continue
                break
            except ValueError:
                print("Por favor, ingrese un número para las columnas.")

        return filas, columnas

filas, columnas = Matriz.pedir_filas_columnas()

mi_matriz = Matriz(filas, columnas)

while True:
    try:
        pos_x = int(input("posx: "))
        pos_y = int(input("posy: "))
        mi_matriz.posicion_inicial_p(pos_x, pos_y)
        break
    except ValueError:
        print("Valor incorrecto, intente de nuevo.")

mi_matriz.imprimir_matriz()
mi_matriz.mover_P()
