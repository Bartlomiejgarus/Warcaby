#Dlugosc okna
WIDTH = 800

#Wysokosc okna
HEIGHT = 800

#Wielkosci do rysowania przycisku resetu gdy ktos wygra wygranej
WYGRANA_RESET = (WIDTH/4, WIDTH/4, 400, 200)

#Wielkosci do rysowania przycisku resetu w trakcji
RESET_W_TRAKCIE= (0,0,20,20)

#ilosc rzedow
ROWS = 8
#ilosc kolumnn (SZACHOWNICA 8 X 8)
COLS = 8

#Wielkosc jednego pola na szachownicy jest to dlugosc okna podzielona przez ilosc takich pol w columnie
lamWielkoscKwadratu = lambda x,y: x//y
WielkoscKwadratu = lamWielkoscKwadratu(WIDTH,COLS)    #WIDTH // COLS

#kolory
#Są one wyliczne na podstawie plety RGB RED GREEN BLUE
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREY = (128,128,128)
BLACKGREY = (100, 100, 100)
RED = (255,0,0)