import pygame
from .ustawienia import WHITE, SQUARE_SIZE, GREY


class Pionek:
    PADDNIG = 15
    POZALINIA = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.krolowka = False
        self.x = 0
        self.y = 0
        self.oblicz_pozycje()

    def zrobkrolowke(self):
        self.krolowka = True

    def oblicz_pozycje(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def rysujpionka(self, win):
        radious = SQUARE_SIZE//2 - self.PADDNIG
        pygame.draw.circle(win, GREY, (self.x, self.y), radious)
        pygame.draw.circle(win, self.color, (self.x, self.y), radious+ self.POZALINIA)

    def __repr__(self):
        return str(self.color)

    #Funkcja do ruchu pionkiem
    def ruch(self, row, col):
        self.row = row
        self.col = col
        self.oblicz_pozycje()

