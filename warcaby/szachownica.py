import pygame
from .ustawienia import BLACK, ROWS, COLS, GREEN, WielkoscKwadratu, WHITE,BLACKGREY, RED, RESET_W_TRAKCIE, WYGRANA_RESET
from .pionek import Pionek


class Szachownica:
    '''
    Klasa szachownica w ktora odpowiada za:
     logike gry
     rysowanie obiektow
    '''

    def __init__(self):
        '''
        Konstruktor klasy szachownica
        Przy wywołaniu rysuje się cala szachownica wraz z pionami
        '''

        #lista tego co przechowuje szachownica
        self.szachownica = []
        #wartosc wybrana poma
        self.Wybrana = None
        #ilosc pionkow bialych i czarnych
        self.iloscbialych = self.iloscczarnych = 12
        #metoda do stworzenia szachownicy i zapisanie jej do listy
        self.tworz_szachownice()

    def rysuj_kwadraty(self, win):
        '''
        Metoda rysujaca kwadraty na szachownicy 8 x 8
        :param win: Okno na ktorym wyswietlana jest gra
        '''

        #wypełnia plasze na czarno
        win.fill(BLACK)
        #Rysuje zielone pola tak zeby wygladalo to jak szachownica
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, GREEN, (row * WielkoscKwadratu, col * WielkoscKwadratu, WielkoscKwadratu, WielkoscKwadratu))

    def tworz_szachownice(self):
        '''
        Metoda ktora tworz szachownice dla logiki czyli
        wypelnia liste szachownica
        '''
        #wyraznienia lam przydatne do tworzenia pionkow lub pola bez nich
        lamDodajPion = lambda r, c, kol: self.szachownica[r].append(Pionek(r, c, kol))
        lamDodajPustePole = lambda r: self.szachownica[r].append(0)
        for row in range(ROWS):
            self.szachownica.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1)%2):
                    if row < 3:
                        #Pionek CZARNY
                        #self.szachownica[row].append(Pionek(row, col, BLACKGREY))
                        lamDodajPion(row,col,BLACKGREY)
                    elif row > 4:
                        #PIONEK BIALY
                        #self.szachownica[row].append(Pionek(row, col, WHITE))
                        lamDodajPion(row, col, WHITE)
                    else:
                        #PUSTE POLE
                        #self.szachownica[row].append(0)
                        lamDodajPustePole(row)
                else:
                    #self.szachownica[row].append(0)
                    lamDodajPustePole(row)


    def dajpionka(self, row, col):
        '''
        Funkcja zwracaja pionka na podstawie wartosci rzedow i kolumn
        :param row: rzad w ktorym jestesmy
        :param col: kolumna w ktorej jestesmy
        '''
        return self.szachownica[row][col]


    def ruch(self, pionek, row, col):
        '''
        Metoda do ruchu pionka na okreslone pole z parametrow row col
        Gdy pionek dojdzie do ostaniego pola to staje sie on krolowka
        :param pionek: pionek ktorym chcemy sie ruszysc
        :param row: rzad do ktorego sie rusza pionek
        :param col: kolumna do ktorej sie rusza pionek
        :return:
        '''
        self.szachownica[pionek.row][pionek.col], self.szachownica[row][col] =  self.szachownica[row][col], self.szachownica[pionek.row][pionek.col]
        pionek.ruch(row,col)

        #Gdy wartossc rzedu jest rowna dolnemy lub gornemu to pionek staje sie krolowka
        #Przy zaladoawniu program tu nie wejdzie bo ta metoda wywoluje sie tylko przy przesuwaniu pionka wiec nie ma potrzeby sprawdzc czy dany pionek to bialy czy czarny i dzielic na 2 warnuku
        if row == ROWS -1 or row == 0:
            pionek.krolowka = True

    def rysuj(self, win, wybrany):
        '''
        Metoda do rysowania calej planszy wraz z pionkami czyli rysuje:
        Szachownice
        Pionki
        Oraz przycisk resetu gry
        :param win: Okno w ktorym rysujemy
        :param wybrany:
        :return: Narysowana szachownice z pionkami i przyciskiem resetu
        '''
        #Rysuje szachownice
        self.rysuj_kwadraty(win)
        #Rysuje Pionki
        for row in range(ROWS):
            for col in range(COLS):
                Pionek = self.szachownica[row][col]
                if Pionek != 0:
                    Pionek.rysujpionka(win, Pionek == wybrany)
        #Rysuje przycisk resetu
        self.rysujReset(win)


    def rysujReset(self, win):
        '''
        Metoda rysyje przycisk resetu:
        Gdy gra trwa to jest on w prawym gornym rogu
        Jesli ktos Wygra i to wyswietla sie duzy z informacja kto wygral

        Umozliwa on zresestowanie gry
        :param win: Okno na ktorym rysujemy
        :return: Narysowany przycisk resetu
        '''
        #Jesli kots wygral:
        try:
            if self.iloscbialych <=0 or self.iloscczarnych <=0:
                #Rysuje duzy przycisk resestu
                pygame.draw.rect(win, RED, WYGRANA_RESET)
                font = pygame.font.Font(pygame.font.get_default_font(), 20)
                text = font.render(self.wygral() + "Click to RESET", False, WHITE)
                win.blit(text, (WYGRANA_RESET[0], WYGRANA_RESET[1]))
            else:
                #Inaczej rysuje w lewym gornym rogu
                pygame.draw.rect(win, RED, RESET_W_TRAKCIE)
        except:
            print("Nie udało się narysować przycisku resetu")


    def remove(self, pioneki):
        '''
        Metoda do usuwania pionkow przy bicu
        :param pioneki: pionki do usuniecia
        :return: usuwa pionki
        '''
        for pionek in pioneki:
            self.szachownica[pionek.row][pionek.col] = 0

        #zmniejszenie ilosci pionkow dla tego kto je stracil
            if pionek != 0:
                if pionek.color == WHITE:
                    self.iloscbialych -= 1
                else:
                    self.iloscczarnych -= 1

    def dajdozwoloneruchy(self, pionek):
        '''
        Metoda dajace dozwolne ruchy do wykonania dla danego pionka
        :param pionek: Pionek ktory wybralismy
        :return: zwraca kolekcje dozwolonych ruchow dla danego pionka
        '''

        #Kolekcja ruchow ktore bedzie mozna wykonac
        ruchy = {}

        #Wartosc po lewej od pionka  potrzebna do wyznaczenia dozwolonych ruchow
        left = pionek.col - 1

        #Wartosc po prawej od pionka potrzebna do wyznacznia dozwolnych ruchow
        right = pionek.col + 1

        #rzad w ktorym znajduje sie pionek
        row = pionek.row

        #Obliczenie dla bialych i krolowki mozliwych ruchow
        if pionek.color == WHITE or pionek.krolowka:
            #Po lewo od pionka
            ruchy.update(self._trasaPoLewej(row - 1, max(row - 3, -1), -1, pionek.color, left, []))
            # Po prawo od pionka
            ruchy.update(self._trasaPoPrawej(row - 1, max(row - 3, -1), -1, pionek.color, right, []))

        #Obliczenie dla czarnych i krolowki mozliwych ruchow
        if pionek.color == BLACKGREY or pionek.krolowka:
            # Po lewo od pionka
            ruchy.update(self._trasaPoLewej(row + 1, min(row + 3, ROWS), 1, pionek.color, left, []))
            # Po prawo od pionka
            ruchy.update(self._trasaPoPrawej(row + 1, min(row + 3, ROWS), 1, pionek.color, right, []))

        return ruchy

    def _trasaPoLewej(self, start, stop, step, color, lewo, pomin):
        '''
        Metoda sluzaca do wyznaczania trasy po lewo od danego pionka
        W srodku ma wywolanie samej siebie gdy mamy wiele bic lub _trasaPoPrawej
        :param start: wartosc startowych wyszukiwan
        :param stop: wartosc koncowych wyszukiwan
        :param step: krok jaki sie ruszamy dla bialych -1 czarny 1
        :param color: kolor pionka pomaga aby nie mozan bylo bić swoich pionkow
        :param lewo: wartosc po lewej ktora chcemy dotrzec
        :param pomin: paramet do tworzenia zlonych mozliwych tras
        :return: zwraca mozliwe ruchow do wykonania przez danego pionka
        '''
        ruchy = {}
        last = []
        for r in range(start, stop, step):
            if lewo < 0:
                break

            current = self.szachownica[r][lewo]
            if current == 0:
                if pomin and not last:
                    break
                elif pomin:
                    ruchy[(r, lewo)] = last + pomin
                else:
                    ruchy[(r, lewo)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)
                    ruchy.update(self._trasaPoLewej(r + step, row, step, color, lewo - 1, pomin=last))
                    ruchy.update(self._trasaPoPrawej(r + step, row, step, color, lewo + 1, pomin=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            lewo -= 1

        return ruchy

    def _trasaPoPrawej(self, start, stop, step, color, prawo, pomin):
        '''
        Metoda sluzaca do wyznaczania trasy po prawej od danego pionka
        W srodku ma wywolanie samej siebie gdy mamy wiele bic lub _trasaPoLewej
        :param start: wartosc startowych wyszukiwan
        :param stop: wartosc koncowych wyszukiwan
        :param step: krok jaki sie ruszamy dla bialych -1 czarny 1
        :param color: kolor pionka pomaga aby nie mozan bylo bić swoich pionkow
        :param prawo: wartosc po lewej ktora chcemy dotrzec
        :param pomin: paramet do tworzenia zlonych mozliwych tras
        :return: zwraca mozliwe ruchow do wykonania przez danego pionka
        '''
        ruchy = {}
        last = []
        for r in range(start, stop, step):
            if prawo >= COLS:
                break

            current = self.szachownica[r][prawo]
            if current == 0:
                if pomin and not last:
                    break
                elif pomin:
                    ruchy[(r, prawo)] = last + pomin
                else:
                    ruchy[(r, prawo)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)
                    ruchy.update(self._trasaPoLewej(r + step, row, step, color, prawo - 1, pomin=last))
                    ruchy.update(self._trasaPoPrawej(r + step, row, step, color, prawo + 1, pomin=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            prawo += 1

        return ruchy

    def wygral(self):
        '''
        Funkcja wygral zwracajca napis kto wygral
        :return: napis kto wygral dana gre
        '''
        if self.iloscbialych <=0:
            return "WYGRAŁ CZARNY!"
        elif self.iloscczarnych <=0:
            return "WYGRAŁ BIAŁY!"
        else:
            return "Nikt niewyrał"