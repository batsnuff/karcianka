import random

# Definicje kart
kolory = {
    "Kier": {
        "🂱": 14, "🂾": 13, "🂽": 12, "🂻": 11, "🂺": 10, "🂹": 9, "🂸": 8, "🂷": 7, "🂶": 6, "🂵": 5, "🂴": 4, "🂳": 3, "🂲": 2
    },
    "Karo": {
        "🃁": 14, "🃎": 13, "🃍": 12, "🃋": 11, "🃊": 10, "🃉": 9, "🃈": 8, "🃇": 7, "🃆": 6, "🃅": 5, "🃄": 4, "🃃": 3, "🃂": 2
    },
    "Pik": {
        "🂡": 14, "🂮": 13, "🂭": 12, "🂫": 11, "🂪": 10, "🂩": 9, "🂨": 8, "🂧": 7, "🂦": 6, "🂥": 5, "🂤": 4, "🂣": 3, "🂢": 2
    },
    "Trefl": {
        "🃑": 14, "🃞": 13, "🃝": 12, "🃛": 11, "🃚": 10, "🃙": 9, "🃘": 8, "🃗": 7, "🃖": 6, "🃕": 5, "🃔": 4, "🃓": 3, "🃒": 2
    },
}

def rozgrywka(liczba_graczy, karty_na_gracza, nazwy_graczy):
    """Funkcja przeprowadzająca jedną rozgrywkę."""

    # Tworzenie talii kart
    talia = [(kolor, ranga) for kolor in kolory for ranga in kolory[kolor]]

    # Tasowanie kart
    random.shuffle(talia)

    # Rozdanie kart
    gracze = [[] for _ in range(liczba_graczy)]
    for i in range(karty_na_gracza * liczba_graczy):
        karta = talia.pop()
        gracz_idx = i % liczba_graczy
        gracze[gracz_idx].append(karta)

    # Obliczanie sumy punktów dla każdego gracza
    punkty_graczy = []
    for karty_gracza in gracze:
        suma_punktow = sum(kolory[karta[0]][karta[1]] for karta in karty_gracza)
        punkty_graczy.append(suma_punktow)

    # Wyświetlanie rąk graczy (tylko emoji rang)
    for i, karty_gracza in enumerate(gracze):
        reka_gracza_str = ", ".join([karta[1] for karta in karty_gracza])
        print(f"Ręka {nazwy_graczy[i]}: {reka_gracza_str}")

    # Wyłonienie zwycięzcy
    zwyciezca = punkty_graczy.index(max(punkty_graczy))
    najlepszy_wynik = max(punkty_graczy)

    return punkty_graczy, zwyciezca, najlepszy_wynik

# Główna pętla gry
while True:
    # Pobranie liczby graczy
    while True:
        try:
            liczba_graczy = int(input("Podaj liczbę graczy (2-10): "))
            if 2 <= liczba_graczy <= 10:
                break
            else:
                print("Niepoprawna liczba graczy. Wprowadź liczbę od 2 do 10.")
        except ValueError:
            print("Niepoprawny format. Wprowadź liczbę całkowitą.")

    # Pobranie nazw graczy
    nazwy_graczy = []
    for i in range(liczba_graczy):
        nazwa = input(f"Podaj nazwę gracza {i + 1}: ")
        nazwy_graczy.append(nazwa)

    # Pobranie liczby kart na gracza
    while True:
        try:
            karty_na_gracza = int(input("Podaj liczbę kart na gracza (maksymalnie 10): "))
            if 1 <= karty_na_gracza <= 10 and karty_na_gracza * liczba_graczy <= 52:
                break
            else:
                print("Niepoprawna liczba kart. Wprowadź liczbę od 1 do 10, tak aby nie przekroczyć liczby kart w talii.")
        except ValueError:
            print("Niepoprawny format. Wprowadź liczbę całkowitą.")

    punkty_graczy, zwyciezca, najlepszy_wynik = rozgrywka(liczba_graczy, karty_na_gracza, nazwy_graczy)

    # Wyświetlanie zwycięzcy z wynikiem
    print(f"\nZwycięzcą jest {nazwy_graczy[zwyciezca]} z {najlepszy_wynik} punktami!")

    while True:
        decyzja = input("Co chcesz zrobić? (ponownie / wyniki / zakończ): ").lower()

        if decyzja == "ponownie":
            break
        elif decyzja == "wyniki":
            for i, punkty in enumerate(punkty_graczy):
                print(f"{nazwy_graczy[i]}: {punkty} punktów")
        elif decyzja == "zakończ":
            print("Koniec gry!")
            exit()
        else:
            print("Niepoprawna komenda. Wybierz 'ponownie', 'wyniki' lub 'zakończ'.")
