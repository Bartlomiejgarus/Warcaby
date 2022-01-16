import unittest
import pygame
from warcaby.gra import Gra
from warcaby.pionek import Pionek
from warcaby.ustawienia import WHITE, BLACKGREY, WIDTH, HEIGHT
class MyTestCase(unittest.TestCase):
    def test1ruch4pionkami(self):
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        gra = Gra(WIN)
        gra.wybierz(4, 5)
        gra.ruch(5, 4)
        gra.wybierz(3, 6)
        gra.ruch(4, 7)
        gra.wybierz(4, 3)
        gra.ruch(3, 4)
        gra.wybierz(2, 1)
        gra.ruch(3, 2)
    def test2blednyruch(self):
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        gra = Gra(WIN)
        #rych niedozwolny
        gra.wybierz(4, 5)
        gra.ruch(7, 7)
    def test3bicie(self):
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        gra = Gra(WIN)
        gra.wybierz(4, 5)
        gra.ruch(5, 4)
        gra.wybierz(2, 3)
        gra.ruch(3, 4)
        gra.wybierz(5, 4)
        gra.ruch(2, 3)
        gra.wybierz(2, 7)
        gra.ruch(3, 6)
        gra.wybierz(5, 2)
        gra.ruch(4, 3)
        gra.wybierz(4, 1)
        #bicie 1
        gra.wybierz(3, 4)
    def test4podwojnebicie(self):
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        gra = Gra(WIN)
        gra.wybierz(4, 5)
        gra.ruch(5, 4)
        gra.wybierz(2, 3)
        gra.ruch(3, 4)
        gra.wybierz(5, 4)
        gra.ruch(2, 3)
        gra.wybierz(2, 7)
        gra.ruch(3, 6)
        gra.wybierz(5, 2)
        gra.ruch(4, 3)
        gra.wybierz(4, 1)
        #bicie 2 na raz
        gra.wybierz(4, 5)
    def test5krolowka(self):
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        gra = Gra(WIN)
        gra.wybierz(4, 5)
        gra.ruch(5, 4)
        gra.wybierz(2, 1)
        gra.ruch(3, 0)
        gra.wybierz(6, 3)
        gra.ruch(5, 4)
        gra.wybierz(1, 0)
        gra.ruch(2, 1)
        gra.wybierz(7, 4)
        gra.ruch(6, 3)
        gra.wybierz(2, 1)
        gra.ruch(3, 2)
        gra.wybierz(5, 2)
        gra.ruch(4, 1)
        gra.wybierz(3, 0)
        #KROLOWKA CZARNA
        gra.ruch(7, 4)
    def test6bicieKrolowka(self):
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        gra = Gra(WIN)
        gra.wybierz(4, 5)
        gra.ruch(5, 4)
        gra.wybierz(2, 1)
        gra.ruch(3, 0)
        gra.wybierz(6, 3)
        gra.ruch(5, 4)
        gra.wybierz(1, 0)
        gra.ruch(2, 1)
        gra.wybierz(7, 4)
        gra.ruch(6, 3)
        gra.wybierz(2, 1)
        gra.ruch(3, 2)
        gra.wybierz(5, 2)
        gra.ruch(4, 1)
        gra.wybierz(3, 0)
        gra.ruch(7, 4)
        gra.wybierz(5, 6)
        gra.ruch(4, 7)
        gra.wybierz(7, 4)
        gra.ruch(4, 7)
        #podwojne bicie krolowka
        gra.ruch(4, 3)
    def test7wygraniegry(self):
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        gra = Gra(WIN)
        gra.wybierz(4, 5)
        gra.ruch(5, 4)
        gra.wybierz(2, 1)
        gra.ruch(3, 0)
        gra.wybierz(6, 3)
        gra.ruch(5, 4)
        gra.wybierz(1, 0)
        gra.ruch(2, 1)
        gra.wybierz(7, 4)
        gra.ruch(6, 3)
        gra.wybierz(2, 1)
        gra.ruch(3, 2)
        gra.wybierz(5, 2)
        gra.ruch(4, 1)
        gra.wybierz(3, 0)
        gra.ruch(7, 4)
        gra.wybierz(5, 6)
        gra.ruch(4, 7)
        gra.wybierz(7, 4)
        gra.ruch(4, 7)
        #podwojne bicie krolowka
        gra.ruch(4, 3)
        gra.wybierz(4, 7)
        gra.ruch(6, 3)
        gra.wybierz(2, 5)
        gra.ruch(4, 7)
        gra.wybierz(6, 7)
        gra.ruch(6, 5)#
        gra.wybierz(4, 7)
        gra.ruch(6, 5)
        gra.wybierz(7, 2)
        gra.ruch(6, 3)
        gra.wybierz(6, 5)
        gra.ruch(7, 4)
        gra.wybierz(7, 6)
        gra.ruch(6, 5)
        gra.wybierz(7, 4)
        gra.ruch(5, 6)
        gra.wybierz(5, 4)
        gra.ruch(4, 3)
        gra.wybierz(4, 3)
        gra.ruch(2, 7)
        gra.wybierz(6, 1)
        gra.ruch(5, 2)
        gra.wybierz(3, 2)
        gra.ruch(2, 3)
        gra.wybierz(5, 0)
        gra.ruch(5, 2)
    def test8RESET(self):
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        gra = Gra(WIN)
        gra.wybierz(4, 5)
        gra.ruch(5, 4)
        gra.wybierz(2, 1)
        gra.ruch(3, 0)
        gra.wybierz(6, 3)
        gra.ruch(5, 4)
        gra.wybierz(1, 0)
        gra.ruch(2, 1)
        gra.wybierz(7, 4)
        gra.ruch(6, 3)
        gra.wybierz(2, 1)
        gra.ruch(3, 2)
        gra.wybierz(5, 2)
        gra.ruch(4, 1)
        gra.wybierz(3, 0)
        gra.ruch(7, 4)
        gra.wybierz(5, 6)
        gra.ruch(4, 7)
        gra.wybierz(7, 4)
        gra.ruch(4, 7)
        #podwojne bicie krolowka
        gra.ruch(4, 3)
        gra.wybierz(4, 7)
        gra.ruch(6, 3)
        gra.wybierz(2, 5)
        gra.ruch(4, 7)
        gra.wybierz(6, 7)
        gra.ruch(6, 5)#
        gra.wybierz(4, 7)
        gra.ruch(6, 5)
        gra.wybierz(7, 2)
        gra.ruch(6, 3)
        gra.wybierz(6, 5)
        gra.ruch(7, 4)
        gra.wybierz(7, 6)
        gra.ruch(6, 5)
        gra.wybierz(7, 4)
        gra.ruch(5, 6)
        gra.wybierz(5, 4)
        gra.ruch(4, 3)
        gra.wybierz(4, 3)
        gra.ruch(2, 7)
        gra.wybierz(6, 1)
        gra.ruch(5, 2)
        gra.wybierz(3, 2)
        gra.ruch(2, 3)
        gra.wybierz(5, 0)
        gra.ruch(5, 2)
        #RESET
        gra.wybierz(4,4)
if __name__ == '__main__':
    unittest.main()
