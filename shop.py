"""
Shop system.

This file contains functions for buying
and selling items, checking prices
and managing player gold.
"""

import equipment
import items
import ui

sklep_eliksiry = [
{
        'Nazwa': 'Bardzo Mały Eliksir Życia',
        'Rodzaj': 'Eliksir',
        'Poziom': 1,
        'HP': 25,
        'Cena': 1,
        'Ilość': 1
    },
{
        'Nazwa': 'Mały Eliksir Życia',
        'Rodzaj': 'Eliksir',
        'Poziom': 5,
        'HP': 500,
        'Cena': 10,
        'Ilość': 1
    },
{
        'Nazwa': 'Średni Eliksir Życia',
        'Rodzaj': 'Eliksir',
        'Poziom': 10,
        'HP': 1000,
        'Cena': 25,
        'Ilość': 1
    },
{
        'Nazwa': 'Spory Eliksir Życia',
        'Rodzaj': 'Eliksir',
        'Poziom': 15,
        'HP': 2500,
        'Cena': 80,
        'Ilość': 1
    },
{
        'Nazwa': 'Duży Eliksir Życia',
        'Rodzaj': 'Eliksir',
        'Poziom': 20,
        'HP': 5000,
        'Cena': 150,
        'Ilość': 1
    },
{
        'Nazwa': 'Bardzo Duży Eliksir Życia',
        'Rodzaj': 'Eliksir',
        'Poziom': 25,
        'HP': 10000,
        'Cena': 250,
        'Ilość': 1
    },
{
        'Nazwa': 'Pełny Eliksir Życia',
        'Rodzaj': 'Eliksir',
        'Poziom': 30,
        'HP': 'MAX',
        'Cena': 400,
        'Ilość': 1
    },
]

sklep_bronie_wojownik = [
{
                 'Nazwa': 'Kamień',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 1,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 10,
                 'Kryt szansa': 5,
                 'Kryt mnożnik': 0.1,
                 'Cena': 10,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Prowizoryczna Włócznia',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 5,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 30,
                 'Kryt szansa': 5,
                 'Kryt mnożnik': 0.15,
                 'Cena': 75,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Miecz Rekruta',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 9,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 80,
                 'Kryt szansa': 5,
                 'Kryt mnożnik': 0.20,
                 'Cena': 300,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Toporek Rozbójnika',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 13,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 120,
                 'Kryt szansa': 7,
                 'Kryt mnożnik': 0.25,
                 'Cena': 750,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Ostrze Strażnika',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 22,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 225,
                 'Kryt szansa': 8,
                 'Kryt mnożnik': 0.5,
                 'Cena': 3500,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Hartowany Miecz',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 25,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 325,
                 'Kryt szansa': 10,
                 'Kryt mnożnik': 0.5,
                 'Cena': 5500,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Ostrze Weterana',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 30,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 450,
                 'Kryt szansa': 10,
                 'Kryt mnożnik': 0.6,
                 'Cena': 10000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Zadzior',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 48,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 1000,
                 'Kryt szansa': 12,
                 'Kryt mnożnik': 1,
                 'Cena': 55000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Ostrze Korony',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 53,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 1500,
                 'Kryt szansa': 15,
                 'Kryt mnożnik': 1,
                 'Cena': 80000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Wierny Przysiędze',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 59,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 2000,
                 'Kryt szansa': 15,
                 'Kryt mnożnik': 1.2,
                 'Cena': 120000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Obsydianowy Miecz',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 66,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 2750,
                 'Kryt szansa': 15,
                 'Kryt mnożnik': 1.3,
                 'Cena': 190000,
                 'Ilość': 1
             }
]

sklep_tarcze_wojownik = [
    {
        'Nazwa': 'Fragment Płotu',
        'Rodzaj': 'Tarcza',
        'Klasa': 'Wojownik',
        'Poziom': 3,
        'Jakość': 50,
        'Ulepszono': 0,
        'Blok': 5,
        'Obrona': 1,
        'HP': 10,
        'Cena': 35,
        'Ilość': 1
    },
    {
        'Nazwa': 'Tarcza Rekruta',
        'Rodzaj': 'Tarcza',
        'Klasa': 'Wojownik',
        'Poziom': 9,
        'Jakość': 50,
        'Ulepszono': 0,
        'Blok': 8,
        'Obrona': 3,
        'HP': 150,
        'Cena': 200,
        'Ilość': 1
    },
    {
        'Nazwa': 'Tarcza Strażnika',
        'Rodzaj': 'Tarcza',
        'Klasa': 'Wojownik',
        'Poziom': 22,
        'Jakość': 50,
        'Ulepszono': 0,
        'Blok': 18,
        'Obrona': 15,
        'HP': 700,
        'Cena': 2500,
        'Ilość': 1
    },
    {
        'Nazwa': 'Hartowana Tarcza',
        'Rodzaj': 'Tarcza',
        'Klasa': 'Wojownik',
        'Poziom': 25,
        'Jakość': 50,
        'Ulepszono': 0,
        'Blok': 20,
        'Obrona': 15,
        'HP': 1000,
        'Cena': 4000,
        'Ilość': 1
    },
    {
        'Nazwa': 'Tarcza Złotej Gwardii',
        'Rodzaj': 'Tarcza',
        'Klasa': 'Wojownik',
        'Poziom': 54,
        'Jakość': 50,
        'Ulepszono': 0,
        'Blok': 25,
        'Obrona': 90,
        'HP': 2000,
        'Cena': 61000,
        'Ilość': 1
    },
    {
        'Nazwa': 'Obsydianowa Tarcza',
        'Rodzaj': 'Tarcza',
        'Klasa': 'Wojownik',
        'Poziom': 68,
        'Jakość': 50,
        'Ulepszono': 0,
        'Blok': 25,
        'Obrona': 150,
        'HP': 3000,
        'Cena': 160000,
        'Ilość': 1
    }
]

sklep_helmy_wojownik = [
    {
        'Nazwa': 'Czapka Wędrowca',
        'Rodzaj': 'Hełm',
        'Klasa': 'Wojownik',
        'Poziom': 4,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 1,
        'HP': 15,
        'Cena': 20,
        'Ilość': 1
    },
    {
        'Nazwa': 'Hełm Rekruta',
        'Rodzaj': 'Hełm',
        'Klasa': 'Wojownik',
        'Poziom': 10,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 3,
        'HP': 150,
        'Cena': 200,
        'Ilość': 1
    },
    {
        'Nazwa': 'Hełm Strażnika',
        'Rodzaj': 'Hełm',
        'Klasa': 'Wojownik',
        'Poziom': 23,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 20,
        'HP': 800,
        'Cena': 2000,
        'Ilość': 1
    },
    {
        'Nazwa': 'Hartowany Hełm',
        'Rodzaj': 'Hełm',
        'Klasa': 'Wojownik',
        'Poziom': 26,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 20,
        'HP': 1200,
        'Cena': 3100,
        'Ilość': 1
    },
    {
        'Nazwa': 'Hełm Złotej Gwardii',
        'Rodzaj': 'Hełm',
        'Klasa': 'Wojownik',
        'Poziom': 55,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 100,
        'HP': 2500,
        'Cena': 45500,
        'Ilość': 1
    },
    {
        'Nazwa': 'Obsydianowy Hełm',
        'Rodzaj': 'Hełm',
        'Klasa': 'Wojownik',
        'Poziom': 69,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 200,
        'HP': 4000,
        'Cena': 120000,
        'Ilość': 1
    }
]

sklep_zbroja_wojownik = [
    {
        'Nazwa': 'Płaszcz Wędrowca',
        'Rodzaj': 'Zbroja',
        'Klasa': 'Wojownik',
        'Poziom': 4,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 1,
        'HP': 20,
        'Cena': 35,
        'Ilość': 1
    },
    {
        'Nazwa': 'Kolczuga Rekruta',
        'Rodzaj': 'Zbroja',
        'Klasa': 'Wojownik',
        'Poziom': 10,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 3,
        'HP': 200,
        'Cena': 350,
        'Ilość': 1
    },
    {
        'Nazwa': 'Zbroja Strażnika',
        'Rodzaj': 'Zbroja',
        'Klasa': 'Wojownik',
        'Poziom': 23,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 25,
        'HP': 1000,
        'Cena': 3600,
        'Ilość': 1
    },
    {
        'Nazwa': 'Hartowana Zbroja',
        'Rodzaj': 'Zbroja',
        'Klasa': 'Wojownik',
        'Poziom': 26,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 25,
        'HP': 1500,
        'Cena': 5500,
        'Ilość': 1
    },
    {
        'Nazwa': 'Zbroja Złotej Gwardii',
        'Rodzaj': 'Zbroja',
        'Klasa': 'Wojownik',
        'Poziom': 55,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 125,
        'HP': 3000,
        'Cena': 81000,
        'Ilość': 1
    },
    {
        'Nazwa': 'Obsydianowy Pancerz',
        'Rodzaj': 'Zbroja',
        'Klasa': 'Wojownik',
        'Poziom': 69,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 250,
        'HP': 5000,
        'Cena': 210000,
        'Ilość': 1
    }
]

sklep_buty_wojownik = [
    {
        'Nazwa': 'Buty Wędrowca',
        'Rodzaj': 'Buty',
        'Klasa': 'Wojownik',
        'Poziom': 4,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 1,
        'HP': 10,
        'Cena': 15,
        'Ilość': 1
    },
    {
        'Nazwa': 'Trzewiki Rekruta',
        'Rodzaj': 'Buty',
        'Klasa': 'Wojownik',
        'Poziom': 10,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 2,
        'HP': 150,
        'Cena': 150,
        'Ilość': 1
    },
    {
        'Nazwa': 'Trzewiki Strażnika',
        'Rodzaj': 'Buty',
        'Klasa': 'Wojownik',
        'Poziom': 23,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 15,
        'HP': 700,
        'Cena': 1700,
        'Ilość': 1
    },
    {
        'Nazwa': 'Hartowane Trzewiki',
        'Rodzaj': 'Buty',
        'Klasa': 'Wojownik',
        'Poziom': 26,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 15,
        'HP': 1000,
        'Cena': 2600,
        'Ilość': 1
    },
    {
        'Nazwa': 'Trzewiki Złotej Gwardii',
        'Rodzaj': 'Buty',
        'Klasa': 'Wojownik',
        'Poziom': 55,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 90,
        'HP': 2000,
        'Cena': 38000,
        'Ilość': 1
    },
    {
        'Nazwa': 'Obsydianowe Trzewiki',
        'Rodzaj': 'Buty',
        'Klasa': 'Wojownik',
        'Poziom': 69,
        'Jakość': 50,
        'Ulepszono': 0,
        'Obrona': 150,
        'HP': 3000,
        'Cena': 100000,
        'Ilość': 1
    }
]

sklep_pierscienie =[
             {
                 'Nazwa': 'Miedziany Pierścień',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 4,
                 'Kryt redukcja szansy': 1,
                 'Kryt redukcja obrażeń': 2,
                 'Cena': 15,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Pierścień Rekruta',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 10,
                 'Kryt redukcja szansy': 2,
                 'Kryt redukcja obrażeń': 4,
                 'Cena': 150,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Pierścień Strażnika',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 23,
                 'Kryt redukcja szansy': 4,
                 'Kryt redukcja obrażeń': 10,
                 'Cena': 1800,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Hartowany Pierścień',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 26,
                 'Kryt redukcja szansy': 4,
                 'Kryt redukcja obrażeń': 13,
                 'Cena': 2700,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Sygnet Złotej Gwardii',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 55,
                 'Kryt redukcja szansy': 7,
                 'Kryt redukcja obrażeń': 26,
                 'Cena': 40000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Obsydianowy Pierścień',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 69,
                 'Kryt redukcja szansy': 8,
                 'Kryt redukcja obrażeń': 31,
                 'Cena': 105000,
                 'Ilość': 1
             }
]

sklep_naszyjniki = [
{
                 'Nazwa': 'Naszyjnik Wędrowca',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 4,
                 'Kryt redukcja szansy': 1,
                 'Kryt redukcja obrażeń': 3,
                 'Cena': 15,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Amulet Rekruta',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 10,
                 'Kryt redukcja szansy': 1,
                 'Kryt redukcja obrażeń': 6,
                 'Cena': 150,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Medalion Strażnika',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 23,
                 'Kryt redukcja szansy': 2,
                 'Kryt redukcja obrażeń': 13,
                 'Cena': 1800,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Hartowany Medalion',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 26,
                 'Kryt redukcja szansy': 3,
                 'Kryt redukcja obrażeń': 17,
                 'Cena': 2700,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Amulet Złotej Gwardii',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 55,
                 'Kryt redukcja szansy': 4,
                 'Kryt redukcja obrażeń': 32,
                 'Cena': 40000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Obsydianowy Medalion',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 69,
                 'Kryt redukcja szansy': 5,
                 'Kryt redukcja obrażeń': 38,
                 'Cena': 105000,
                 'Ilość': 1
             },
]

def wyswietl_sklep(lista):
    if not lista:
        print('\nSklep jest pusty!')
        return
    ui.wyswietl_tytul('SKLEP')
    for indeks, item in enumerate(lista, start=1):
        for klucz, wartosc in item.items():
            if klucz == 'Nazwa':
                if item.get('Jakość') is not None:
                    unikalnosc, bonus = items.sprawdz_jakosc(item['Jakość'])
                    print(f'\n{indeks}) "[{unikalnosc}] {wartosc} +{item['Ulepszono']}"')
                else:
                    print(f'\n{indeks}) "{wartosc}"')
            elif klucz == 'Jakość':
                print(f'{klucz}: {wartosc}/100')
            elif klucz == 'Obrażenia':
                status, dmg = items.oblicz_dmg_przedmiotu(item)
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
                status, obrona = items.oblicz_obrone_przedmiotu(item)
                print(f'{klucz}: +{obrona}')
            elif klucz == 'HP':
                print(f'{klucz}: +{wartosc}')
            elif klucz == 'Ulepszono':
                continue
            elif klucz == 'Blok':
                print(f'Blok: {wartosc}%')
            else:
                print(f'{klucz}: {wartosc}')
    print('\n0) Powrót')

def kup_przedmiot(gracz, sklep, nazwa_przedmiotu, ilosc):
    rodzaje_eq = ['Broń', 'Hełm', 'Zbroja', 'Buty', 'Tarcza', 'Pierścień', 'Naszyjnik']
    if ilosc < 1:
        return 'Zbyt mała ilość!', None, None
    for przedmiot in sklep:
        if przedmiot['Nazwa'].lower() == nazwa_przedmiotu.lower():
            if gracz['Poziom'] >= przedmiot['Poziom']:
                if gracz['Złoto'] >= przedmiot['Cena'] * ilosc:
                    cena = przedmiot['Cena'] * ilosc
                    gracz['Złoto'] -= cena
                    if przedmiot['Rodzaj'] in rodzaje_eq:
                        for niestackujacy in range(ilosc):
                            kupiony_przedmiot = przedmiot.copy()
                            kupiony_przedmiot['Ilość'] = 1
                            items.nadaj_id(kupiony_przedmiot)
                            gracz['Ekwipunek'].append(kupiony_przedmiot)
                        return f'Pomyślnie kupiono "{kupiony_przedmiot['Nazwa']}" w ilości: {ilosc}\nWartość: {cena:.2f} złota.', kupiony_przedmiot, cena
                    else:
                        kupiony_przedmiot = przedmiot.copy()
                        kupiony_przedmiot['Ilość'] = ilosc
                    for eq in gracz['Ekwipunek']:
                        if eq['Nazwa'] == kupiony_przedmiot['Nazwa']:
                            eq['Ilość'] += ilosc
                            return f'Pomyślnie kupiono "{kupiony_przedmiot['Nazwa']}" w ilości: {ilosc}\nWartość: {cena:.2f} złota.', kupiony_przedmiot, cena
                    gracz['Ekwipunek'].append(kupiony_przedmiot)
                    return f'Pomyślnie kupiono "{kupiony_przedmiot['Nazwa']}" w ilości: {ilosc}\nWartość: {cena:.2f} złota.', kupiony_przedmiot, cena
                return 'Zbyt mała ilość złota!', None, None
            return f'Zbyt niski poziom! Wymagany poziom: {przedmiot['Poziom']}', None, None
    return f'Brak przedmiotu "{nazwa_przedmiotu}" w sklepie!', None, None

def sprzedaj_przedmiot(gracz, eq, numer_przedmiotu, ilosc):
    if ilosc < 1:
        return 'Zbyt mała ilość!'
    if gracz['Ekwipunek']:
        for indeks, przedmiot in enumerate(eq, start=1):
            if indeks == numer_przedmiotu:
                if ilosc <= przedmiot['Ilość']:
                    slot_eq = przedmiot['Rodzaj']
                    if slot_eq == 'Tarcza':
                        slot_eq = 'Dodatkowa'
                    for slot, item in gracz['Założone'].items():
                        if slot_eq == slot:
                            if item is not None:
                                if przedmiot.get('ID') is not None and item.get('ID') == przedmiot['ID']:
                                    return 'Najpierw zdejmij przedmiot!'
                    cena = (przedmiot['Cena'] * ilosc) * 0.5
                    cena = int(cena)
                    gracz['Złoto'] += cena
                    przedmiot['Ilość'] -= ilosc
                    if przedmiot['Ilość'] < 1:
                        usunieto = przedmiot
                        gracz['Ekwipunek'].remove(przedmiot)
                        if usunieto.get('Jakość') is not None:
                            unikalnosc, bonus = items.sprawdz_jakosc(usunieto['Jakość'])
                            return f'Pomyślnie sprzedano "[{unikalnosc}] {usunieto['Nazwa']} +{usunieto['Ulepszono']}" w ilości: {ilosc}\nWartość sprzedaży: {cena} złota.'
                        return f'Pomyślnie sprzedano "{usunieto['Nazwa']}" w ilości: {ilosc}\nWartość sprzedaży: {cena} złota.'
                    if przedmiot.get('Jakość') is not None:
                        unikalnosc, bonus = items.sprawdz_jakosc(przedmiot['Jakość'])
                        return f'Pomyślnie sprzedano "[{unikalnosc}] {przedmiot['Nazwa']} +{przedmiot['Ulepszono']}" w ilości: {ilosc}\nWartość sprzedaży: {cena} złota.'
                    return f'Pomyślnie sprzedano "{przedmiot['Nazwa']}" w ilości: {ilosc}\nWartość sprzedaży: {cena} złota.'
                return 'Zbyt mała ilość w ekwipunku!'
        return f'Brak przedmiotu o numerze: {numer_przedmiotu}!'
    return f'Brak przedmiotów w ekwipunku!'

def menu_sklepu(gracz):
    opcje = ('Kup przedmiot', 'Sprzedaj przedmiot', 'Ulepsz przedmiot', 'Zmień jakość przedmiotu', 'Powrót')
    while True:
        ui.wyswietl_menu('SKLEP', opcje)
        opcja_sklep = ui.pobierz_wybor(1, len(opcje))
        if opcja_sklep == 1:
            wybrany_sklep = None
            while True:
                opcje_handlarzy = ('Handlarz bronią', 'Handlarz zbroją', 'Jubiler', 'Alchemik', 'Powrót')
                ui.wyswietl_menu('HANDLARZE', opcje_handlarzy)
                opcja_kup = ui.pobierz_wybor(1, len(opcje_handlarzy))
                if opcja_kup == 1:
                    wyswietl_sklep(sklep_bronie_wojownik)
                    wybrany_sklep = sklep_bronie_wojownik
                elif opcja_kup == 2:
                    opcje_ekwipunku = ('Tarcze', 'Hełmy', 'Pancerz', 'Buty', 'Powrót')
                    ui.wyswietl_menu('EKWIPUNEK', opcje_ekwipunku)
                    wybor3 = ui.pobierz_wybor(1, len(opcje_ekwipunku))
                    if wybor3 == 1:
                        wybrany_sklep = sklep_tarcze_wojownik
                        wyswietl_sklep(wybrany_sklep)
                    elif wybor3 == 2:
                        wybrany_sklep = sklep_helmy_wojownik
                        wyswietl_sklep(wybrany_sklep)
                    elif wybor3 == 3:
                        wybrany_sklep = sklep_zbroja_wojownik
                        wyswietl_sklep(wybrany_sklep)
                    elif wybor3 == 4:
                        wybrany_sklep = sklep_buty_wojownik
                        wyswietl_sklep(wybrany_sklep)
                    elif wybor3 == 5:
                        continue
                    else:
                        print('\nNieprawidłowa opcja!')
                        continue
                elif opcja_kup == 3:
                    opcje_bizuteria = ('Pierścienie', 'Naszyjniki', 'Powrót')
                    ui.wyswietl_menu('BIZUTERIA', opcje_bizuteria)
                    wybor3 = ui.pobierz_wybor(1, len(opcje_bizuteria))
                    if wybor3 == 1:
                        wybrany_sklep = sklep_pierscienie
                        wyswietl_sklep(wybrany_sklep)
                    elif wybor3 == 2:
                        wybrany_sklep = sklep_naszyjniki
                        wyswietl_sklep(wybrany_sklep)
                    elif wybor3 == 3:
                        continue
                    else:
                        print('\nNieprawidłowa opcja!')
                        continue
                elif opcja_kup == 4:
                    wyswietl_sklep(sklep_eliksiry)
                    wybrany_sklep = sklep_eliksiry
                elif opcja_kup == 5:
                    break
                else:
                    print('\nNieprawidłowa opcja!')
                    continue
                if not wybrany_sklep:
                    continue
                print('\nPodaj numer przedmiotu do kupienia: ')
                numer_przedmiotu = ui.pobierz_wybor(0, len(wybrany_sklep))
                if numer_przedmiotu < 0:
                    print('\nNieprawidłowy numer przedmiotu!')
                    continue
                elif numer_przedmiotu == 0:
                    continue
                elif numer_przedmiotu > len(wybrany_sklep):
                    print('\nBrak przedmiotu o tym indeksie!')
                    continue
                nazwa_przedmiotu = wybrany_sklep[numer_przedmiotu - 1]['Nazwa']
                print('\nPodaj ilość: ')
                ilosc = ui.pobierz_wybor(1, 1000)
                komunikat, przedmiot, cena = kup_przedmiot(gracz, wybrany_sklep, nazwa_przedmiotu, ilosc)
                print(f'\n{komunikat}')
        elif opcja_sklep == 2:
            eq = []
            if not gracz['Ekwipunek']:
                print('\nEkwipunek jest pusty!')
                continue
            wybrany_sklep = None
            while True:
                rodzaje_handlarzy = ('Handlarz bronią', 'Handlarz zbroją', 'Jubiler', 'Alchemik', 'Powrót')
                ui.wyswietl_menu('HANDLARZE', rodzaje_handlarzy)
                opcja_kup = ui.pobierz_wybor(1, len(rodzaje_handlarzy))
                if opcja_kup == 1:
                    eq = equipment.filtruj_ekwipunek(gracz, ['Broń'])
                elif opcja_kup == 2:
                    eq = equipment.filtruj_ekwipunek(gracz, ['Hełm', 'Zbroja', 'Buty', 'Tarcza'])
                elif opcja_kup == 3:
                    eq = equipment.filtruj_ekwipunek(gracz, ['Pierścień', 'Naszyjnik'])
                elif opcja_kup == 4:
                    eq = equipment.filtruj_ekwipunek(gracz,['Ulepszanie EQ', 'Zmiana jakości EQ', 'Eliksir', 'Materiał', 'Inne'])
                elif opcja_kup == 5:
                    break
                else:
                    print('\nNieprawidłowa opcja!')
                    continue
                if not eq:
                    print('\nBrak przedmiotów w ekwipunku!')
                    continue
                for indeks, przedmiot in enumerate(eq, start=1):
                    for klucz, wartosc in przedmiot.items():
                        if klucz == 'Nazwa':
                            if przedmiot.get('Jakość') is not None:
                                unikalnosc, bonus = items.sprawdz_jakosc(przedmiot['Jakość'])
                                print(f'\n{indeks}) "{unikalnosc} {wartosc} +{przedmiot['Ulepszono']}"')
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
                        elif klucz == 'Ulepszono':
                            continue
                        elif klucz == 'Blok':
                            print(f'Blok: {wartosc}%')
                        elif klucz == 'ID':
                            continue
                        else:
                            print(f'{klucz}: {wartosc}')
                print('\n0) - Powrót')
                print('\nPodaj numer przedmiotu do sprzedaży: ')
                numer_przedmiotu = ui.pobierz_wybor(0, len(eq))
                if numer_przedmiotu < 0:
                    print('\nNieprawidłowy numer przedmiotu!')
                    continue
                if numer_przedmiotu == 0:
                    continue
                if numer_przedmiotu > len(eq):
                    print('\nBrak przedmiotu o tym indeksie!')
                    continue
                print('\nPodaj ilość: ')
                ilosc = ui.pobierz_wybor(1, 1000)
                komunikat = sprzedaj_przedmiot(gracz, eq, numer_przedmiotu, ilosc)
                print(f'\n{komunikat}')
        elif opcja_sklep == 3:
            items.wybierz_eq_do_ulepszenia(gracz)
        elif opcja_sklep == 4:
            items.wybierz_eq_do_zmiany_jakosci(gracz)
        elif opcja_sklep == 5:
            break
        else:
            print('\nNieprawidłowa opcja!')
            continue