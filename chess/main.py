import pygame
import sys
import os
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
        posiciones = []
        direcciones = [[1, 0], [-1, 0], [0, 1], [0, -1],[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for dir in direcciones:
            for i in range(1,8):
                f = self.fila + i * dir[0]
                c = self.columna + i * dir[1]
                x = tablero.es_ocupado(f,c)
                if isinstance(x,bool):
                    break
                elif x is None:
                    posiciones.append([f,c])
                else:
                    if x.color != self.color:
                        posiciones.append([f,c])
                    break
        return posiciones

class Torre(Pieza):
    def __init__(self, color,fila,columna):
        super().__init__(color, "Torre",fila,columna)
    def posib(self):
        posiciones = []
        direcciones = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dir in direcciones:
            for i in range(1,8):
                f = self.fila + i * dir[0]
                c = self.columna + i * dir[1]
                x = tablero.es_ocupado(f,c)
                if isinstance(x,bool):
                    break
                elif x is None:
                    posiciones.append([f,c])
                else:
                    if x.color != self.color:
                        posiciones.append([f,c])
                    break
        return posiciones

class Alfil(Pieza):
    def __init__(self, color,fila,columna):
        super().__init__(color, "Alfil",fila,columna)
    def posib(self):
        posiciones = []
        direcciones = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for dir in direcciones:
            for i in range(1,8):
                f = self.fila + i * dir[0]
                c = self.columna + i * dir[1]
                x = tablero.es_ocupado(f,c)
                if isinstance(x,bool):
                    break
                elif x is None:
                    posiciones.append([f,c])
                else:
                    if x.color != self.color:
                        posiciones.append([f,c])
                    break
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

pygame.init()

ANCHO_VENTANA = 640
ALTO_VENTANA = 640
TAMAÑO_CASILLA = ANCHO_VENTANA // 8
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Ajedrez")
icono = pygame.image.load("images/icono.png")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()

tablero = Tablero()

tablero[0][0] = Torre("negro", 0, 0)
tablero[0][1] = Caballo("negro", 0, 1)
tablero[0][2] = Alfil("negro", 0, 2)
tablero[0][3] = Reina("negro", 0, 3)
tablero[0][4] = Rey("negro", 0, 4)
tablero[0][5] = Alfil("negro", 0, 5)
tablero[0][6] = Caballo("negro", 0, 6)
tablero[0][7] = Torre("negro", 0, 7)
for i in range(8):
    tablero[1][i] = Peon("negro", 1, i)

tablero[7][0] = Torre("blanco", 7, 0)
tablero[7][1] = Caballo("blanco", 7, 1)
tablero[7][2] = Alfil("blanco", 7, 2)
tablero[7][3] = Reina("blanco", 7, 3)
tablero[7][4] = Rey("blanco", 7, 4)
tablero[7][5] = Alfil("blanco", 7, 5)
tablero[7][6] = Caballo("blanco", 7, 6)
tablero[7][7] = Torre("blanco", 7, 7)
for i in range(8):
    tablero[6][i] = Peon("blanco", 6, i)

posib = []

turno = "blanco"

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN: 
            x, y = evento.pos 
            fila = y // TAMAÑO_CASILLA 
            columna = x // TAMAÑO_CASILLA

            coordenadas = list()
            if posib != [] and posib is not None:
                for i in posib[0]:
                    coordenadas.append(i)
                for i in posib[1:]:
                    if i == [fila,columna]:
                        pieza = tablero.es_ocupado(coordenadas[0],coordenadas[1])
                        if pieza is not None:
                            if pieza.tipo == "Peon":
                                tablero[i[0]][i[1]] = Peon(pieza.color,i[0],i[1])
                            elif pieza.tipo == "Caballo":
                                tablero[i[0]][i[1]] = Caballo(pieza.color,i[0],i[1])
                            elif pieza.tipo == "Rey":
                                tablero[i[0]][i[1]] = Rey(pieza.color,i[0],i[1])
                            elif pieza.tipo == "Torre":
                                tablero[i[0]][i[1]] = Torre(pieza.color,i[0],i[1])
                            elif pieza.tipo == "Alfil":
                                tablero[i[0]][i[1]] = Alfil(pieza.color,i[0],i[1])
                            elif pieza.tipo == "Reina":
                                tablero[i[0]][i[1]] = Reina(pieza.color,i[0],i[1])
                            tablero.limpiar(coordenadas[0],coordenadas[1])
                            turno = "blanco" if turno == "negro" else "negro"
                            posib = []
                    
            if tablero.es_ocupado(fila,columna):
                pieza = tablero.es_ocupado(fila,columna)
                if pieza.color == turno:
                    posib = pieza.posib()
                    if posib != [] and posib is not None:
                        posib.insert(0, [fila, columna])
            else:
                print(f"Clic en casilla del tablero: ({fila}, {columna})")
                posib = []

    rey_blanco = False
    rey_negro = False
    for fila in range(8):
        for columna in range(8):
            color = (235, 235, 208) if (fila + columna) % 2 == 0 else (119, 148, 185)
            pygame.draw.rect(ventana, color, (columna * TAMAÑO_CASILLA, fila * TAMAÑO_CASILLA, TAMAÑO_CASILLA, TAMAÑO_CASILLA))
            pieza = tablero[fila][columna]
            if pieza:
                ventana.blit(pieza.imagen, (pieza.columna * TAMAÑO_CASILLA, pieza.fila * TAMAÑO_CASILLA))
            for i in posib[1:]:
                pygame.draw.circle(ventana,(128, 128, 128), (i[1] * TAMAÑO_CASILLA + TAMAÑO_CASILLA // 2, i[0] * TAMAÑO_CASILLA + TAMAÑO_CASILLA // 2), 10)

            x = tablero[fila][columna]
            if isinstance(x,Rey) and x.color == "blanco":
                rey_blanco = True
            elif isinstance(x,Rey) and x.color == "negro":
                rey_negro = True


    if rey_blanco == False:
        print("blancas han perdido")
        pygame.quit()
        sys.exit()
    elif rey_negro == False:
        print("las blancas han ganado")
        pygame.quit()
        sys.exit()
    pygame.display.flip()
    clock.tick(10) 

