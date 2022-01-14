import pygame
from warcaby.ustawienia import WIDTH, HEIGHT, SQUARE_SIZE, WHITE
from warcaby.szachownica import Szachownica
from warcaby.gra import Gra

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Warcaby")


def dajPozycjeZMyszki(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    gra = Gra(WIN)

    while run:
        clock.tick(FPS)

        if gra.szachownica.wygral() != None:
            print(gra.szachownica.wygral())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = dajPozycjeZMyszki(pos)
                gra.wybierz(row, col)

        gra.update()

    pygame.quit()


main()