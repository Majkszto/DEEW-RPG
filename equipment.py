"""
Equipment system.

This file contains functions for managing
equipment, equipping and removing items,
and updating player stats.
"""

import items
import potions
import ui


def filtruj_ekwipunek(gracz, rodzaje):
    lista = []
    for przedmiot in gracz['Ekwipunek']:
        if przedmiot['Rodzaj'] in rodzaje:
            lista.append(przedmiot)
    return lista

def filtruj_ekwipunek_bez(gracz, rodzaje):
    lista = []
    for przedmiot in gracz['Ekwipunek']:
        if przedmiot['Rodzaj'] not in rodzaje:
            lista.append(przedmiot)
    return lista

def wyswietl_ekwipunek(gracz):
    if not gracz['Ekwipunek']:
        print('\nBrak przedmiotów w ekwipunku!')
        return
    ui.wyswietl_tytul('EKWIPUNEK')
    for indeks, przedmiot in enumerate(gracz['Ekwipunek'], start=1):
        for klucz, wartosc in przedmiot.items():
            if klucz == 'Nazwa':
                if przedmiot.get('Jakość') is not None:
                    unikalnosc, bonus = items.sprawdz_jakosc(przedmiot['Jakość'])
                    print(f'\n{indeks}) "[{unikalnosc}] {wartosc} +{przedmiot['Ulepszono']}"')
                else:
                    print(f'\n{indeks}) "{wartosc}"')
            elif klucz == 'Jakość':
                print(f'{klucz}: {wartosc}/100')
            elif klucz == 'Obrażenia':
                status, dmg = items.oblicz_dmg_przedmiotu(przedmiot)
                print(f'{klucz}: +{dmg}')
            elif klucz == 'Kryt szansa':
                print(f'Szansa na cios krytyczny: +{wartosc}%')
            elif klucz == 'Kryt mnożnik':
                print(f'Cios krytyczny: +{wartosc * 100:.0f}%')
            elif klucz == 'Kryt redukcja szansy':
                print(f'Redukcja szansy na cios krytyczny: {wartosc}%')
            elif klucz == 'Kryt redukcja obrażeń':
                print(f'Redukcja obrażeń ciosu krytycznego: {wartosc}%')
            elif klucz == 'Obrona':
                status, obrona = items.oblicz_obrone_przedmiotu(przedmiot)
                print(f'{klucz}: +{obrona}')
            elif klucz == 'HP':
                print(f'{klucz}: +{wartosc}')
            elif klucz == 'Blok':
                print(f'Blok: {wartosc}%')
            elif klucz in ('Ulepszono', 'ID'):
                continue
            else:
                print(f'{klucz}: {wartosc}')

def zaloz_przedmiot(gracz, numer):
    rodzaje_pancerza = ['Hełm', 'Zbroja', 'Buty']
    rodzaje_bizuterii = ['Pierścień', 'Naszyjnik']
    if numer < 1:
        return False, '\nNieprawidłowy numer!'
    for indeks, przedmiot in enumerate(gracz['Ekwipunek'], start=1):
        if numer == indeks:
            slot_eq = przedmiot['Rodzaj']
            if przedmiot.get('Klasa') and gracz['Klasa'] != przedmiot['Klasa']:
                return False, f'\nTylko {przedmiot['Klasa']} może założyć ten przedmiot!'
            if gracz['Poziom'] < przedmiot['Poziom']:
                return False, f'\nWymagany poziom do założenia "{przedmiot['Nazwa']}": {przedmiot['Poziom']}'
            if slot_eq == 'Broń':
                if gracz['Założone'][slot_eq]:
                    status, dmg_zalozone = items.oblicz_dmg_przedmiotu(gracz['Założone'][slot_eq])
                    gracz['Statystyki']['Atak MIN'] -= dmg_zalozone
                    gracz['Statystyki']['Atak MAX'] -= dmg_zalozone
                    gracz['Statystyki']['Kryt szansa'] -= gracz['Założone'][slot_eq]['Kryt szansa']
                    gracz['Statystyki']['Kryt mnożnik'] -= gracz['Założone'][slot_eq]['Kryt mnożnik']
                gracz['Założone'][slot_eq] = przedmiot
                nowy_status, nowy_dmg_zalozone = items.oblicz_dmg_przedmiotu(gracz['Założone'][slot_eq])
                gracz['Statystyki']['Atak MIN'] += nowy_dmg_zalozone
                gracz['Statystyki']['Atak MAX'] += nowy_dmg_zalozone
                gracz['Statystyki']['Kryt szansa'] += przedmiot['Kryt szansa']
                gracz['Statystyki']['Kryt mnożnik'] += przedmiot['Kryt mnożnik']
                return True, przedmiot
            elif slot_eq in rodzaje_pancerza:
                if gracz['Założone'][slot_eq]:
                    gracz['Statystyki']['HP MAX'] -= gracz['Założone'][slot_eq]['HP']
                    status, obrona = items.oblicz_obrone_przedmiotu(gracz['Założone'][slot_eq])
                    gracz['Statystyki']['Obrona'] -= obrona
                gracz['Założone'][slot_eq] = przedmiot
                gracz['Statystyki']['HP MAX'] += przedmiot['HP']
                if gracz['Statystyki']['HP'] > gracz['Statystyki']['HP MAX']:
                    gracz['Statystyki']['HP'] = gracz['Statystyki']['HP MAX']
                status, obrona = items.oblicz_obrone_przedmiotu(gracz['Założone'][slot_eq])
                gracz['Statystyki']['Obrona'] += obrona
                return True, przedmiot
            elif slot_eq == 'Tarcza':
                slot_eq = 'Dodatkowa'
                if gracz['Założone'][slot_eq]:
                    gracz['Statystyki']['HP MAX'] -= gracz['Założone'][slot_eq]['HP']
                    gracz['Statystyki']['Blok'] -= gracz['Założone'][slot_eq]['Blok']
                    status, obrona = items.oblicz_obrone_przedmiotu(gracz['Założone'][slot_eq])
                    gracz['Statystyki']['Obrona'] -= obrona
                gracz['Założone'][slot_eq] = przedmiot
                gracz['Statystyki']['HP MAX'] += przedmiot['HP']
                if gracz['Statystyki']['HP'] > gracz['Statystyki']['HP MAX']:
                    gracz['Statystyki']['HP'] = gracz['Statystyki']['HP MAX']
                gracz['Statystyki']['Blok'] += przedmiot['Blok']
                status, obrona = items.oblicz_obrone_przedmiotu(gracz['Założone'][slot_eq])
                gracz['Statystyki']['Obrona'] += obrona
                return True, przedmiot
            elif slot_eq in rodzaje_bizuterii:
                if gracz['Założone'][slot_eq]:
                    gracz['Statystyki']['Kryt redukcja szansy'] -= gracz['Założone'][slot_eq].get('Kryt redukcja szansy', 0)
                    gracz['Statystyki']['Kryt redukcja obrażeń'] -= gracz['Założone'][slot_eq].get('Kryt redukcja obrażeń', 0)
                gracz['Założone'][slot_eq] = przedmiot
                gracz['Statystyki']['Kryt redukcja szansy'] += gracz['Założone'][slot_eq].get('Kryt redukcja szansy', 0)
                gracz['Statystyki']['Kryt redukcja obrażeń'] += gracz['Założone'][slot_eq].get('Kryt redukcja obrażeń', 0)
                return True, przedmiot
            return False, '\nNie możesz założyć tego przedmiotu!'
    return False, f'\nNie znaleziono przedmiotu o numerze: {numer}!'

def pokaz_zalozone_przedmioty_postac(gracz):
    print('ZAŁOŻONE'.center(75))
    print('━' * 75)
    for indeks, (slot, item) in enumerate(gracz['Założone'].items(), start=1):
        if item is not None:
            if item.get('Jakość') is not None:
                unikalnosc, bonus = items.sprawdz_jakosc(item['Jakość'])
                print(f'{indeks}. {slot}: [{unikalnosc}] {item['Nazwa']} +{item['Ulepszono']} (Poziom: {item['Poziom']})')
            else:
                print(f'{indeks}. {slot}: {item['Nazwa']} (Poziom: {item['Poziom']})')
        else:
            print(f'{indeks}. {slot}: Brak')
    print('━' * 75)

def pokaz_zalozone_przedmioty(gracz):
    ui.wyswietl_tytul('ZAŁOŻONE')
    for indeks, (slot, item) in enumerate(gracz['Założone'].items(), start=1):
        if item is not None:
            if item.get('Jakość') is not None:
                unikalnosc, bonus = items.sprawdz_jakosc(item['Jakość'])
                print(f'{indeks}. {slot}: [{unikalnosc}] {item['Nazwa']} +{item['Ulepszono']} (Poziom: {item['Poziom']})')
            else:
                print(f'{indeks}. {slot}: {item['Nazwa']} (Poziom: {item['Poziom']})')
        else:
            print(f'{indeks}. {slot}: Brak')
    print('━' * 75)

def zdejmij_przedmiot(gracz, numer):
    rodzaje_pancerza = ['Hełm', 'Zbroja', 'Buty']
    rodzaje_bizuterii = ['Pierścień', 'Naszyjnik']
    if numer < 1:
        return False, '\nNieprawidłowy numer przedmiotu!'
    for indeks, (slot, item) in enumerate(gracz['Założone'].items(), start=1):
        if indeks == numer:
            if item is not None:
                zdjety = item.copy()
                if item['Rodzaj'] == 'Broń':
                    status, dmg_zalozone = items.oblicz_dmg_przedmiotu(item)
                    gracz['Statystyki']['Atak MIN'] -= dmg_zalozone
                    gracz['Statystyki']['Atak MAX'] -= dmg_zalozone
                    gracz['Statystyki']['Kryt szansa'] -= item['Kryt szansa']
                    gracz['Statystyki']['Kryt mnożnik'] -= item['Kryt mnożnik']
                    gracz['Założone'][slot] = None
                    return True, zdjety
                elif item['Rodzaj'] in rodzaje_pancerza:
                    gracz['Statystyki']['HP MAX'] -= item['HP']
                    if gracz['Statystyki']['HP'] > gracz['Statystyki']['HP MAX']:
                        gracz['Statystyki']['HP'] = gracz['Statystyki']['HP MAX']
                    status, obrona = items.oblicz_obrone_przedmiotu(item)
                    gracz['Statystyki']['Obrona'] -= obrona
                    gracz['Założone'][slot] = None
                    return True, zdjety
                elif item['Rodzaj'] == 'Tarcza':
                    gracz['Statystyki']['HP MAX'] -= item['HP']
                    if gracz['Statystyki']['HP'] > gracz['Statystyki']['HP MAX']:
                        gracz['Statystyki']['HP'] = gracz['Statystyki']['HP MAX']
                    status, obrona = items.oblicz_obrone_przedmiotu(item)
                    gracz['Statystyki']['Obrona'] -= obrona
                    gracz['Statystyki']['Blok'] -= item['Blok']
                    gracz['Założone'][slot] = None
                    return True, zdjety
                elif item['Rodzaj'] in rodzaje_bizuterii:
                    gracz['Statystyki']['Kryt redukcja szansy'] -= item.get('Kryt redukcja szansy', 0)
                    gracz['Statystyki']['Kryt redukcja obrażeń'] -= item.get('Kryt redukcja obrażeń', 0)
                    gracz['Założone'][slot] = None
                    return True, zdjety
                return False, '\nNie możesz zdjąć tego przedmiotu!'
            else:
                return False, '\nTen slot jest pusty!'
    return False, '\nNieprawidłowy numer przedmiotu!'

def menu_ekwipunku(gracz):
    while True:
        opcje = ('Pokaż założone', 'Pokaż ekwipunek', 'Załóż przedmiot', 'Zdejmij przedmiot', 'Wypij eliksir', 'Powrót')
        ui.wyswietl_menu('EKWIPUNEK', opcje)
        opcja1 = ui.pobierz_wybor(1, 6)
        if opcja1 == 1:
            pokaz_zalozone_przedmioty(gracz)
        elif opcja1 == 2:
            wyswietl_ekwipunek(gracz)
        elif opcja1 == 3:
            if not gracz['Ekwipunek']:
                print('\nBrak przedmiotów w ekwipunku!')
                continue
            wyswietl_ekwipunek(gracz)
            print('\nWybierz numer przedmiotu: ')
            numer = ui.pobierz_wybor(1, len(gracz['Ekwipunek']))
            status, wynik = zaloz_przedmiot(gracz, numer)
            if status:
                if wynik.get('Ulepszono') is not None:
                    print(f'\nPomyślnie założono: {wynik['Nazwa']} +{wynik['Ulepszono']} (Poziom: {wynik['Poziom']})!')
                else:
                    print(f'\nPomyślnie założono: {wynik['Nazwa']} (Poziom: {wynik['Poziom']})!')
            else:
                print(f'{wynik}')
        elif opcja1 == 4:
            znaleziono = False
            for slot, item in gracz['Założone'].items():
                if item is not None:
                    znaleziono = True
                    break
            if znaleziono:
                pokaz_zalozone_przedmioty(gracz)
                numer = ui.pobierz_wybor(1, 7)
                status, wynik = zdejmij_przedmiot(gracz, numer)
                if status:
                    if wynik.get('Ulepszono') is not None:
                        print(
                            f'\nPomyślnie zdjęto: {wynik["Nazwa"]} +{wynik["Ulepszono"]} (Poziom: {wynik["Poziom"]})!')
                    else:
                        print(f'\nPomyślnie zdjęto: {wynik["Nazwa"]} (Poziom: {wynik["Poziom"]})!')
                else:
                    print(f'{wynik}')
            else:
                print('\nBrak założonych przedmiotów!')
        elif opcja1 == 5:
            eq = filtruj_ekwipunek(gracz, ['Eliksir'])
            if not eq:
                print('\nBrak posiadanych eliksirów!')
                continue
            potions.pokaz_eliksiry(gracz)
            numer_przedmiotu = ui.pobierz_wybor(1, len(eq))
            komunikat = potions.wypij_eliksir(gracz, numer_przedmiotu)
            print(komunikat)
        elif opcja1 == 6:
            break
        else:
            print('\nNieprawidłowa opcja!')