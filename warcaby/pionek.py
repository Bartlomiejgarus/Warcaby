import pygame
from .ustawienia import WHITE, WielkoscKwadratu, GREY, BLUE


class Pionek:
    '''
    Klasa pionek ktora przechowuje wartosci o danym pionku
    '''
    ODKRAWEDZIKWADRATU = 15
    POZALINIA = 2

    def __init__(self, row, col, color):
        '''
        Konstruktor klasy pionek podajemy wartosc row i col w ktorych ma sie znajdowac i kolor jaki ma miec
        :param row: wartosc rzedu w ktorym jest pionek
        :param col: wartosc kolumn w ktorym jest pionek
        :param color: kolor jaki ma pionek
        '''
        self.row = row
        self.col = col
        self.color = color
        #bool czy dany pionek to krolowka
        self.krolowka = False
        self.x = 0
        self.y = 0
        self.oblicz_pozycje()

    def zrobkrolowke(self):
        '''
        Metoda zmienia pionka na krolowke
        '''
        self.krolowka = True

    def oblicz_pozycje(self):
        '''
        Oblicza pozycje dla pionka w ktorej sie znajduje
        '''
        self.x = WielkoscKwadratu * self.col + WielkoscKwadratu // 2
        self.y = WielkoscKwadratu * self.row + WielkoscKwadratu // 2

    def rysujpionka(self, win, czyJestWybrany):
        '''
        Metoda do rysowania pionka w oknie win
        :param win: okno w ktorym jest rysowany
        :param czyJestWybrany: gdy pionek jest wybrany przez gracza
        '''
        #rysowanie pionkow
        promien = WielkoscKwadratu // 2 - self.ODKRAWEDZIKWADRATU
        pygame.draw.circle(win, GREY, (self.x, self.y), promien)
        pygame.draw.circle(win, self.color, (self.x, self.y), promien+ self.POZALINIA)
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        #dodanie na ich nazw
        t = "B" if self.color == WHITE else "C"
        t = t + "d" if self.krolowka else t
        t = "[" + t + "]" if czyJestWybrany else t
        text = font.render(t, False, BLUE)
        win.blit(text, (self.x, self.y))

    def ruch(self, row, col):
        '''
        metoda do ruchu pionkiem
        :param row: nowa wartosc rzedow
        :param col: nowa wartosc kolumn
        :return:
        '''
        self.row = row
        self.col = col
        self.oblicz_pozycje()

