"""
Potion system.

This file contains functions for showing
available potions, using health potions
and restoring player HP.
"""

import ui


def pokaz_eliksiry(gracz):
    eliksiry = pobierz_eliksiry(gracz)
    if eliksiry:
        ui.wyswietl_tytul('ELIKSIRY')
        for indeks, eliksir in enumerate(eliksiry, start=1):
            for klucz, wartosc in eliksir.items():
                if klucz == 'Nazwa':
                    print(f'\n{indeks}) "{wartosc}"')
                else:
                    print(f'{klucz}: {wartosc}')
        print('\n0) Powrót')
    else:
        print('\nBrak eliksirów!')

def pobierz_eliksiry(gracz):
    eliksiry = []
    if gracz['Ekwipunek']:
        for przedmiot1 in gracz['Ekwipunek']:
            if przedmiot1['Rodzaj'] == 'Eliksir':
                eliksiry.append(przedmiot1)
        return eliksiry
    return eliksiry

def wypij_eliksir(gracz, numer_przedmiotu):
    eliksiry = pobierz_eliksiry(gracz)
    if eliksiry:
        for indeks, eliksir in enumerate(eliksiry, start=1):
            if numer_przedmiotu == indeks:
                if gracz['Poziom'] >= eliksir['Poziom']:
                    if gracz['Statystyki']['HP'] < gracz['Statystyki']['HP MAX']:
                        eliksir['Ilość'] -= 1
                        if eliksir['Ilość'] < 1:
                            gracz['Ekwipunek'].remove(eliksir)
                        if eliksir['HP'] == 'MAX':
                            gracz['Statystyki']['HP'] = gracz['Statystyki']['HP MAX']
                        else:
                            gracz['Statystyki']['HP'] += eliksir['HP']
                        if gracz['Statystyki']['HP'] > gracz['Statystyki']['HP MAX']:
                            gracz['Statystyki']['HP'] = gracz['Statystyki']['HP MAX']
                        return f'\nPomyślnie wypito {eliksir['Nazwa']}!\nHP: {gracz['Statystyki']['HP']} / {gracz['Statystyki']['HP MAX']}'
                    return '\nTwoje HP jest pełne!'
                return f'\nWymagany poziom do wypicia eliksiru: {eliksir['Poziom']}'
        return '\nNieprawidłowy numer przedmiotu!'
    return '\nBrak eliksirów!'
