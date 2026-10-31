"""
Item drop system.

This file contains functions for random
item drops, drop chances, item quantities
and adding items to the inventory.
"""

import random
import items

def wykonaj_drop(gracz, mob):
    rodzaje_eq = ['Broń', 'Hełm', 'Zbroja', 'Buty', 'Tarcza', 'Pierścień', 'Naszyjnik']
    los = False
    print(f'\nDrop:')
    for przedmiot in mob['Drop']:
        wylosowano = random.uniform(0, 100)
        if wylosowano <= przedmiot['Szansa']:
            los = True
            znaleziono = False
            wydropiony_przedmiot = przedmiot.copy()
            status, przedmiot_z_jakoscia = items.losuj_jakosc(wydropiony_przedmiot)
            if status:
                wydropiony_przedmiot = przedmiot_z_jakoscia
            wydropiony_przedmiot.pop('Szansa')
            if przedmiot.get('Ilość MIN') is not None:
                ilosc = random.randint(przedmiot['Ilość MIN'], przedmiot['Ilość MAX'])
                wydropiony_przedmiot['Ilość'] = ilosc
                wydropiony_przedmiot.pop('Ilość MIN')
                wydropiony_przedmiot.pop('Ilość MAX')

            if wydropiony_przedmiot.get('Jakość') is not None:
                unikalnosc, bonus = items.sprawdz_jakosc(wydropiony_przedmiot['Jakość'])
                print(f'"[{unikalnosc}] {wydropiony_przedmiot['Nazwa']} +{wydropiony_przedmiot['Ulepszono']}" - {wydropiony_przedmiot['Ilość']} szt')
            else:
                print(f'"{wydropiony_przedmiot['Nazwa']}" - {wydropiony_przedmiot['Ilość']} szt')
            if wydropiony_przedmiot['Rodzaj'] in rodzaje_eq:
                items.nadaj_id(wydropiony_przedmiot)
                gracz['Ekwipunek'].append(wydropiony_przedmiot)
                continue
            for eq in gracz['Ekwipunek']:
                if (eq['Nazwa'] == wydropiony_przedmiot['Nazwa'] and eq.get('Poziom') == wydropiony_przedmiot.get('Poziom') and eq['Rodzaj'] == wydropiony_przedmiot['Rodzaj']):
                    eq['Ilość'] += wydropiony_przedmiot['Ilość']
                    znaleziono = True
                    break
            if not znaleziono:
                gracz['Ekwipunek'].append(wydropiony_przedmiot)
    if not los:
        print('Nic nie wypadło!')