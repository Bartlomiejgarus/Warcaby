# 5.Warcaby


Opis zadania

- Okno z siatką przycisków 8x8 oraz przyciskiem do resetowania gry.
- Przyciski reprezentują pola planszy do gry w warcaby. Pola puste - przyciski bez tekstu. Pola z pionkami gracza 1 - przycisk z tekstem "C". Pola z pionkami gracza
2 - przycisk z tekstem "B". Damki oznaczane są dodatkową literą d ("Cd", "Bd").
- Nad planszą wyswietlana jest informacja "Tura gracza 1" lub "Tura gracza 2".
- Gracz wybiera pionka (tekst pola zmienia się z "C" na "[C]" lub z "B" na "[B]"), a potem pole na które chce wykonać ruch. Jeśli ruch jest dozwolony, pionek jest przestawiany. Jesli nie, to wyswietlany jest komunikat "ruch niedozwolony".
Zasady jak  w  warcabach  (https://pl.wikipedia.org/wiki/Warcaby ,  dowolny wariant). Zwykłe pionki i damki mają być obiektami dwóch róznych klas dziedziczonych po klasie Pionek.
- Gdy gra się kończy, wyswietlane jest okienko z napisem "Wygrał gracz 1" lub
"Wygrał gracz 2", zaleznie kto wygrał grę . Możliwe jest zresetowanie planszy bez zamykania głównego okna.

Testy
1.	Wykonanie po dwa ruchy przez kazdego z graczy.
2.	Niepowodzenie błędnego ruchu pionkiem.
3.	Wykonanie bicia pojedynczego pionka.
4.	Wykonanie bicia przynajmniej dwóch pionków.
5.	Zamiana pionka w damką.
6.	Bicie damką.
7.	Wygrana gracza grającego czarnymi pionkami.
8.	Rozpoczcie nowej gry po zwycistwie jednego z graczy.
Wskazane jest przygotowanie specjalnych początkowych rozstawień pionków dla testów d, e, f, g, h.

