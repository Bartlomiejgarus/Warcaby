import pygame
from warcaby.ustawienia import WIDTH, HEIGHT, WielkoscKwadratu
from warcaby.gra import Gra

#Okno do wyswietlana obiektow
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#nazwa okna
pygame.display.set_caption("Warcaby")
pygame.init()


def dajPozycjeZMyszki(pos):
    '''
    daje dana kolumne i rzad na podstawie wartosci pos
    :param pos: wartosc pos
    :return:
    '''
    x, y = pos
    row = y // WielkoscKwadratu
    col = x // WielkoscKwadratu
    return row, col


def main():
    '''
    Funkcja glowna ktora uruchamia grę warcaby
    '''
    run = True
    clock = pygame.time.Clock()
    gra = Gra(WIN)

    #dopuki gra dziala dzialaja na niej zdarzenia
    while run:
        clock.tick(60)

        for event in pygame.event.get():

            # jesli wyjdziemy z gdy
            if event.type == pygame.QUIT:
                run = False

            #jesli klikniemy myszka
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                #jesli klikiemy przycisk inny niz reset
                if not gra.reset(pos):
                    row, col = dajPozycjeZMyszki(pos)
                    gra.wybierz(row, col)

        gra.grajmy()

    pygame.quit()


main()