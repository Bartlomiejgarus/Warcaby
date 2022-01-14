import pygame
from .ustawienia import BLACK, ROWS, COLS, GREEN, SQUARE_SIZE, WHITE,BLACKGREY
from .pionek import Pionek

#Klasa do tworzenia i rysowania obiektow na planszy
class Szachownica:
    def __init__(self):
        self.szachownica = []
        self.Wybrana = None
        self.iloscbialych = self.iloscczarnych = 12
        self.tworz_szachownice()

    #Funkcja rysująca kwadraty na szachownicy
    def rysuj_kwadraty(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, GREEN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    #Funkcja ustawajaca
    def tworz_szachownice(self):
        for row in range(ROWS):
            self.szachownica.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1)%2):
                    if row < 3:
                        self.szachownica[row].append(Pionek(row, col, BLACKGREY))
                    elif row > 4:
                        self.szachownica[row].append(Pionek(row, col, WHITE))
                    else:
                        self.szachownica[row].append(0)
                else:
                    self.szachownica[row].append(0)


    def dajpionka(self, row, col):
        return self.szachownica[row][col]

    #Funkcja do ruchu
    def ruch(self, pionek, row, col):
        self.szachownica[pionek.row][pionek.col], self.szachownica[row][col] =  self.szachownica[row][col], self.szachownica[pionek.row][pionek.col]
        pionek.ruch(row,col)

        if row == ROWS -1 or row == 0:
            pionek.krolowka = True

    #Funkcja rysująca całą plansze wraz z pionkami
    def rysuj(self, win):
        self.rysuj_kwadraty(win)
        for row in range(ROWS):
            for col in range(COLS):
                Pionek = self.szachownica[row][col]
                if Pionek != 0:
                    Pionek.rysujpionka(win)

    def remove(self, pioneki):
        for pionek in pioneki:
            self.szachownica[pionek.row][pionek.col] = 0

            if pionek != 0:
                if pionek.color == WHITE:
                    self.iloscbialych -= 1
                else:
                    self.iloscczarnych -= 1

    def dajdozwoloneruchy(self, pionek):
        ruchy = {}
        left = pionek.col - 1
        right = pionek.col + 1
        row = pionek.row

        if pionek.color == WHITE or pionek.krolowka:
            ruchy.update(self._trasaLeft(row - 1, max(row - 3, -1), -1, pionek.color, left))
            ruchy.update(self._trasaRight(row - 1, max(row - 3, -1), -1, pionek.color, right))
        if pionek.color == BLACKGREY or pionek.krolowka:
            ruchy.update(self._trasaLeft(row + 1, min(row + 3,  ROWS), 1, pionek.color, left))
            ruchy.update(self._trasaRight(row + 1, min(row + 3, ROWS), 1, pionek.color, right))

        return ruchy

    def _trasaLeft(self, start, stop, step, color, left, pomin=[]):
        ruchy = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.szachownica[r][left]
            if current == 0:
                if pomin and not last:
                    break
                elif pomin:
                    ruchy[(r, left)] = last + pomin
                else:
                    ruchy[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    ruchy.update(self._trasaLeft(r + step, row, step, color, left - 1, pomin=last))
                    ruchy.update(self._trasaRight(r + step, row, step, color, left + 1, pomin=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return ruchy
    def _trasaRight(self, start, stop, step, color, right, pomin=[]):
        ruchy = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.szachownica[r][right]
            if current == 0:
                if pomin and not last:
                    break
                elif pomin:
                    ruchy[(r, right)] = last + pomin
                else:
                    ruchy[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    ruchy.update(self._trasaLeft(r + step, row, step, color, right - 1, pomin=last))
                    ruchy.update(self._trasaRight(r + step, row, step, color, right + 1, pomin=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return ruchy

    def wygral(self):
        if self.iloscbialych <=0:
            return BLACKGREY
        elif self.iloscczarnych <=0:
            return WHITE