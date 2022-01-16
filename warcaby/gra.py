import pygame
from .szachownica import Szachownica
from .ustawienia import WHITE, BLACKGREY, BLUE, WielkoscKwadratu, RESET_W_TRAKCIE, WYGRANA_RESET


class Gra:
    '''
    Klasa Gra do sterowania gra
    Dziala ona na klasie szachownica
    Wyswietla dzialanie rychy dozwolone ruchy na podstawie tego co chcemy uzyskac
    '''
    def __init__(self, win):
        '''
        konstruktor wymaga okna w ktorym wyswietla szachowice pionki i ruchy
        :param win:
        '''
        #metoda inicjacji
        self._inicjacja()
        self.win = win

    def _inicjacja(self):
        '''
        Metoda inicjcji wywolywana przy starcie gry lub resecie
        :return:
        '''
        #wartosc wybrana na poczatku None
        self.wybrana = None

        #stworzenie klasy szachownica
        self.szachownica = Szachownica()

        #kogo jest tura na poczatku bialych
        self.tura = WHITE

        #Dozwolone ruchy do wykonania
        self.dozwoloneruchy = {}

    def grajmy(self):
        '''
        Metoda glowna klasy slozaca do rysowania szachownicy
        :return:
        '''
        #rysowanie szachownicy
        self.szachownica.rysuj(self.win, self.wybrana)
        #rysoanie dozwolonych rychow dla danej pozycji
        self.rysujdozwolneruchy(self.dozwoloneruchy)
        pygame.display.update()

    def reset(self, pozycjamyszy):
        '''
        Funkcja resetu gry jesli klikniemy przycik resetu gra sie zresetuje
        :param pozycjamyszy: pozycja myszki
        :return: True gdy zresetujemy inaczej False
        '''
        resetrect = WYGRANA_RESET if self.szachownica.iloscczarnych <= 0 or self.szachownica.iloscbialych <= 0 else RESET_W_TRAKCIE
        pygamerect = pygame.Rect(resetrect[0], resetrect[1], resetrect[2], resetrect[3])
        if pygamerect.collidepoint(pozycjamyszy):
            self._inicjacja()
            return True
        return False

    def wybierz(self, row, col):
        '''
        wybiera na podstawie rzedow i kolumn pionka
        Jesli wybierzemy pole bez pionka/krolowke lub pionka ktorego nie jest tura to zwroci false
        Jesli wybierzemy pionka/krolowke to zwroci prawde
        :param row: rzedy
        :param col: kolumny
        :return:
        '''
        if self.wybrana:
            wynik = self.ruch(row, col)
            if not wynik:
                self.wybrana = None
                self.wybierz(row, col)

        pionek = self.szachownica.dajpionka(row, col)
        if pionek != 0 and pionek.color == self.tura:
            self.wybrana = pionek
            self.dozwoloneruchy = self.szachownica.dajdozwoloneruchy(pionek)
            return True

        return False



    def ruch(self, row, col):
        '''
        Przenosi pionka na dany rzad i kolumne jesli ruch jest dozwolony wtedy tez zmienia sie tura
        :param row: rzedy wybrane
        :param col: kolumny wybrane
        :return: true jesli przeniesienie sie uda albo false jest sie nie uda
        '''
        pionek = self.szachownica.dajpionka(row, col)
        if self.wybrana and pionek == 0 and (row, col) in self.dozwoloneruchy:
            self.szachownica.ruch(self.wybrana, row, col)
            pomin = self.dozwoloneruchy[(row, col)]
            if pomin:
                self.szachownica.remove(pomin)
            self.zmienture()
            self.wybrana = None
        else:
            return False
        return True

    def rysujdozwolneruchy(self, ruchy):
        '''
        Metoda rysuje dozowolne ruchy na podstawie ruchow
        :param ruchy:
        '''
        for ruch in ruchy:
            row, col = ruch
            pygame.draw.circle(self.win, BLUE, (col * WielkoscKwadratu + WielkoscKwadratu // 2, row * WielkoscKwadratu + WielkoscKwadratu // 2), 15)

    def zmienture(self):
        '''
        Zmienia ture na gracza przeciwnego
        '''
        self.dozwoloneruchy = {}
        if self.tura == WHITE:
            self.tura = BLACKGREY
        else:
            self.tura = WHITE
