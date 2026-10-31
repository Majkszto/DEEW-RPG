"""
Save system.

This file contains functions for saving
and loading game progress using JSON.
"""

import json

def zapisz_gre(lista):
    try:
        with open('zapis_gry.json', 'w', encoding='utf-8') as plik:
            json.dump(lista, plik, ensure_ascii=False, indent=4)
        print('\nZapisano pomyślnie.')
        return True
    except (OSError, TypeError, ValueError):
        return False

def wczytaj_gre():
    try:
        with open('zapis_gry.json', 'r', encoding='utf-8') as plik:
            lista = json.load(plik)
        return lista
    except FileNotFoundError:
        return None
    except (json.JSONDecodeError, UnicodeError, OSError):
        print('\nNie udało się odczytać zapisu gry!')
        return None