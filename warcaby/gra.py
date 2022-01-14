import pygame
from .szachownica import Szachownica
from .ustawienia import WHITE, BLACKGREY, BLUE, SQUARE_SIZE


class Gra:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.szachownica.rysuj(self.win)
        self.rysujDozwolneRuchy(self.dozwoloneruchy)
        pygame.display.update()

    def _init(self):
        self.wybrana = None
        self.szachownica = Szachownica()
        self.tura = WHITE
        self.dozwoloneruchy = {}

    def reset(self):
        self._init()

    def wybierz(self, row, col):
        if self.wybrana:
            wynik = self._ruch(row, col)
            if not wynik:
                self.wybrana = None
                self.wybierz(row, col)

        pionek = self.szachownica.dajpionka(row, col)
        if pionek != 0 and pionek.color == self.tura:
            self.wybrana = pionek
            self.dozwoloneruchy = self.szachownica.dajdozwoloneruchy(pionek)
            return True

        return False



    def _ruch(self, row, col):
        pionek = self.szachownica.dajpionka(row, col)
        if self.wybrana and pionek == 0 and (row,col) in self.dozwoloneruchy:
            self.szachownica.ruch(self.wybrana, row, col)
            pomin = self.dozwoloneruchy[(row, col)]
            if pomin:
                self.szachownica.remove(pomin)
            self.zmienTure()
        else:
            return False
        return True

    def rysujDozwolneRuchy(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def zmienTure(self):
        self.dozwoloneruchy = {}
        if self.tura == WHITE:
            self.tura = BLACKGREY
        else:
            self.tura = WHITE