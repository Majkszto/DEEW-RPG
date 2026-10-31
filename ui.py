"""
User interface.

This file contains functions for showing
menus, displaying titles and checking
player input.
"""

def pobierz_wybor(najnizsza_liczba, najwyzsza_liczba):
    while True:
        try:
            wybor = int(input())
            if najnizsza_liczba <= wybor <= najwyzsza_liczba:
                return wybor
        except ValueError:
            pass
        print('\nNieprawidłowa opcja!\n')

def wyswietl_menu(tytul, opcje):
    print()
    print('━' * 75)
    print(tytul.center(75))
    print('━' * 75)
    for indeks, opcja in enumerate(opcje, start=1):
        print(f'{indeks}. {opcja}')
    print('━' * 75)
    print()

def wyswietl_tytul(tytul):
    print()
    print('━' * 75)
    print(tytul.center(75))
    print('━' * 75)

def wyswietl_kryt():
    print('\n\033[1;33m CIOS KRYTYCZNY! \033[0m')

def wyswietl_ture(tura):
    print(f'\n\033[1;94m TURA {tura} \033[0m')