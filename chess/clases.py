from abc import ABC, abstractmethod

class Pieza(ABC):
    def __init__(self, color, tipo,fila,columna):
        self.color = color
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.imagen = pygame.image.load(os.path.join("images", f"{tipo}_{color}.png"))
        self.imagen = pygame.transform.scale(self.imagen, (TAMAÑO_CASILLA, TAMAÑO_CASILLA))
    

    @abstractmethod
    def posib(self):
        pass


    def mover(self):
        self.fila = fila
        self.columna = columna
        
    
class Rey(Pieza):
    def __init__(self, color,fila,columna):
        super().__init__(color, "Rey",fila,columna)
    def posib(self):
        posibles_posiciones = [[self.fila + 1, self.columna],[self.fila - 1, self.columna],[self.fila , self.columna +1],[self.fila, self.columna -1],[self.fila + 1, self.columna + 1],[self.fila + 1, self.columna - 1],[self.fila - 1, self.columna + 1],[self.fila - 1, self.columna - 1]]
        posiciones = []
        for i in posibles_posiciones:
            x = tablero.es_ocupado(i[0],i[1])
            if x is not False and x is not None:
                if x.color != self.color:
                    posiciones.append(i)
            elif x is None:
                posiciones.append(i)
        return posiciones

class Reina(Pieza):
    def __init__(self, color,fila,columna):
        super().__init__(color, "Reina",fila,columna)
    def posib(self):
        posibles_posiciones = []
        for i in range(1,8):
            posibles_posiciones.append([self.fila + i, self.columna])
            posibles_posiciones.append([self.fila - i, self.columna])
            posibles_posiciones.append([self.fila, self.columna + i])
            posibles_posiciones.append([self.fila, self.columna - i])
            posibles_posiciones.append([self.fila + i,self.columna + i])
            posibles_posiciones.append([self.fila + i,self.columna - i])
            posibles_posiciones.append([self.fila - i,self.columna + i])
            posibles_posiciones.append([self.fila - i,self.columna - i])

        posiciones = []
        for i in posibles_posiciones:
            x = tablero.es_ocupado(i[0], i[1])
            if x is not False and x is not None:
                if x.color != self.color:
                    posiciones.append(i)
            elif x is None:
                posiciones.append(i)
            print(posiciones)
        return posiciones

class Torre(Pieza):
    def __init__(self, color,fila,columna):
        super().__init__(color, "Torre",fila,columna)
    def posib(self):
        posibles_posiciones = []
        for i in range(1,8):
            posibles_posiciones.append([self.fila + i, self.columna])
            posibles_posiciones.append([self.fila - i, self.columna])
            posibles_posiciones.append([self.fila, self.columna + i])
            posibles_posiciones.append([self.fila, self.columna - i])
            
        posiciones = []
        for i in posibles_posiciones:
            x = tablero.es_ocupado(i[0], i[1])
            if x is not False and x is not None:
                if x.color != self.color:
                    posiciones.append(i)
            elif x is None:
                posiciones.append(i)
            print(posiciones)
        return posiciones

class Alfil(Pieza):
    def __init__(self, color,fila,columna):
        super().__init__(color, "Alfil",fila,columna)
    def posib(self):
        posibles_posiciones = []
        for i in range(1,8):
            posibles_posiciones.append([self.fila + i,self.columna + i])
            posibles_posiciones.append([self.fila + i,self.columna - i])
            posibles_posiciones.append([self.fila - i,self.columna + i])
            posibles_posiciones.append([self.fila - i,self.columna - i])

        posiciones = []
        for i in posibles_posiciones:
            x = tablero.es_ocupado(i[0], i[1])
            if x is not False and x is not None:
                if x.color != self.color:
                    posiciones.append(i)
            elif x is None:
                posiciones.append(i)
            print(posiciones)
        return posiciones

class Caballo(Pieza):
    def __init__(self, color,fila,columna):
        super().__init__(color, "Caballo",fila,columna)
    def posib(self):
        posibles_posiciones = [[self.fila - 2, self.columna - 1],[self.fila - 2, self.columna + 1],[self.fila - 1, self.columna - 2],[self.fila - 1, self.columna + 2],[self.fila + 2, self.columna - 1],[self.fila + 2, self.columna + 1],[self.fila + 1, self.columna - 2],[self.fila + 1, self.columna + 2]]

        posiciones = []
        for i in posibles_posiciones:
            x = tablero.es_ocupado(i[0], i[1])
            if x is not False and x is not None:
                if x.color != self.color:
                    posiciones.append(i)
            elif x is None:
                posiciones.append(i)
            

        return posiciones

class Peon(Pieza):
    def __init__(self, color,fila,columna):
        super().__init__(color, "Peon",fila,columna)
    def posib(self):
        posibles_posiciones = []
        if self.color == "blanco":
            if not tablero.es_ocupado(self.fila - 1, self.columna):
                posibles_posiciones.append([self.fila - 1, self.columna])
            if tablero.es_ocupado(self.fila - 1, self.columna - 1):
                x = tablero.es_ocupado(self.fila - 1, self.columna - 1)
                if x.color != self.color:
                    posibles_posiciones.append([self.fila - 1, self.columna - 1])
            if tablero.es_ocupado(self.fila - 1, self.columna + 1):
                x = tablero.es_ocupado(self.fila - 1, self.columna + 1)
                if x.color != self.color:
                    posibles_posiciones.append([self.fila - 1, self.columna + 1])
            if self.fila == 6:
                x = tablero.es_ocupado(self.fila - 2, self.columna)
                if x is None:
                    posibles_posiciones.append([self.fila -2, self.columna])
        else:
            if not tablero.es_ocupado(self.fila + 1, self.columna):
                posibles_posiciones.append([self.fila + 1, self.columna])
            if tablero.es_ocupado(self.fila + 1, self.columna + 1):
                x = tablero.es_ocupado(self.fila + 1, self.columna + 1)
                if x.color != self.color:
                    posibles_posiciones.append([self.fila + 1, self.columna + 1])
            if tablero.es_ocupado(self.fila + 1, self.columna - 1):
                x = tablero.es_ocupado(self.fila + 1, self.columna - 1)
                if x.color != self.color:
                    posibles_posiciones.append([self.fila + 1, self.columna - 1])
            if self.fila == 1:
                x = tablero.es_ocupado(self.fila + 2, self.columna)
                if x is None:
                    posibles_posiciones.append([self.fila + 2, self.columna])

        return posibles_posiciones


class Tablero:
    def __init__(self):
        self.tablero = [[None for _ in range(8)] for _ in range(8)]

    def es_ocupado(self, fila, columna):
        if fila >= 0 and fila <= 7 and columna >= 0 and columna <= 7:
            if self.tablero[fila][columna] is None:
                return None
            else:
                return self.tablero[fila][columna]
        else:
            return False 
    
    def limpiar(self,fila,columna):
        self.tablero[fila][columna] = None
    
    def __getitem__(self, index):
        return self.tablero[index]

    def __setitem__(self, index, value):
        self.tablero[index] = value