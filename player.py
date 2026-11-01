"""
Player system.

This file contains functions for creating
a player, managing stats, experience
and leveling up.
"""

import equipment
import skills
import ui


def nowa_gra(nick_gracza):
    gracze = [
        {'Nick': nick_gracza,
         'Klasa': 'Wojownik',
         'Poziom': 1,
         'Exp': 0,
         'Złoto': 1,
         'Założone': {
             'Broń': None,
             'Dodatkowa': None,
             'Hełm': None,
             'Zbroja': None,
             'Buty': None,
             'Pierścień': None,
             'Naszyjnik': None},
         'Statystyki': {
             'HP': 10,
             'HP MAX': 10,
             'Mana': 10,
             'Mana MAX': 10,
             'Atak MIN': 5,
             'Atak MAX': 10,
             'Kryt szansa': 3,
             'Kryt mnożnik': 1.25,
             'Obrona': 0,
             'Blok': 0,
             'Kryt redukcja szansy': 0,
             'Kryt redukcja obrażeń': 0},
         'Umiejętności': {
             'Slot 1': None,
             'Slot 2': None,
             'Slot 3': None,
             'Slot 4': None,
             'Slot 5': None},
         'Wyuczono': [],
         'Ekwipunek': []
         }
    ]
    return gracze

def pobierz_gracza(lista, nick):
    for gracz in lista:
        if gracz['Nick'].lower() == nick.lower():
            return gracz
    return None

def wyswietl_postac(gracz):
    for klucz, wartosc in gracz.items():
        if klucz == 'Nick':
            ui.wyswietl_tytul(wartosc)
        elif klucz in ('Poziom', 'Klasa'):
            print(f'{klucz}: {wartosc}')
        elif klucz == 'Exp':
            if gracz['Poziom'] < 99:
                wymagany_exp = int(100 * gracz['Poziom'] ** 4)
                print(f'{klucz}: {wartosc} / {wymagany_exp}')
            else:
                print(f'{klucz}: {wartosc}')
        elif klucz == 'Złoto':
            print(f'{klucz}: {wartosc}')
            print('━' * 75)
        elif klucz == 'Założone':
            equipment.pokaz_zalozone_przedmioty_postac(gracz)
        elif klucz == 'Statystyki':
            pokaz_statystyki(gracz)
        elif klucz == 'Umiejętności':
            skills.pokaz_wybrane_umiejetnosci_postac(gracz)

def pokaz_statystyki(gracz):
    print('STATYSTYKI'.center(75))
    print('━' * 75)
    for statystyka, ile in gracz['Statystyki'].items():
        if statystyka == 'HP':
            print(f'{statystyka}: {ile} / {gracz['Statystyki']['HP MAX']}')
        elif statystyka == 'Mana':
            print(f'{statystyka}: {ile} / {gracz['Statystyki']['Mana MAX']}')
        elif statystyka == 'Atak MIN':
            print(f'Atak: {gracz['Statystyki']['Atak MIN']} - {gracz['Statystyki']['Atak MAX']}')
        elif statystyka == 'Obrona':
            print(f'{statystyka}: {ile}')
        elif statystyka == 'Kryt szansa':
            print(f'Szansa na cios krytyczny: {ile}%')
        elif statystyka == 'Kryt mnożnik':
            print(f'Cios krytyczny: {ile * 100:.0f}%')
        elif statystyka == 'Kryt redukcja szansy':
            print(f'Redukcja szansy na cios krytyczny: {ile}%')
        elif statystyka == 'Kryt redukcja obrażeń':
            print(f'Redukcja obrażeń ciosu krytycznego: {ile}%')
        elif statystyka == 'Blok':
            print(f'Blok: {ile}%')
    print('━' * 75)

def sprawdz_poziom(gracz):
    wymagany_exp = int(100 * gracz['Poziom'] ** 4)
    statystyki = gracz['Statystyki']
    while gracz['Poziom'] < 99 and gracz['Exp'] >= wymagany_exp:
        gracz['Exp'] -= wymagany_exp
        gracz['Poziom'] += 1
        statystyki['HP MAX'] += int(20 * gracz['Poziom'])
        statystyki['HP'] = statystyki['HP MAX']
        statystyki['Mana MAX'] += gracz['Poziom']
        statystyki['Mana'] = statystyki['Mana MAX']
        statystyki['Atak MIN'] += gracz['Poziom']
        statystyki['Atak MAX'] += int(gracz['Poziom'] * 1.5)
        statystyki['Obrona'] += int(gracz['Poziom'] / 2)
        wymagany_exp = int(100 * gracz['Poziom'] ** 4)
        print(f'Pomyślnie awansowano na {gracz['Poziom']} poziom!')