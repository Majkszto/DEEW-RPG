"""
DEEW RPG - Text-Based RPG Game

Author: Dawid Mikszto
Python: 3.12+
Status: Work in Progress

This is my personal RPG game made in Python.
I created it to learn and practice programming.

The game includes turn-based combat, enemies,
equipment, skills, shops, item drops,
character leveling and saving progress.

This file starts the game and connects
the other game modules.
"""

import combat
import player
import shop
import equipment
import skills
import save
import ui

def menu_startowe():
    opcje = ['Nowa gra', 'Wczytaj grę', 'Zakończ']
    while True:
        ui.wyswietl_menu('DEEW RPG', opcje)
        menu_logowanie = ui.pobierz_wybor(1, len(opcje))
        if menu_logowanie == 1:
            nick_gracza = input('\nNick: ')
            gracze = player.nowa_gra(nick_gracza)
            print(f'\nWitaj {nick_gracza}!')
            return gracze
        elif menu_logowanie == 2:
            wczytano = save.wczytaj_gre()
            if wczytano:
                print('\nPomyślnie wczytano grę.')
                return wczytano
            else:
                print('\nBrak zapisu!')
                continue
        elif menu_logowanie == 3:
            print('\nZakończono pomyślnie.')
            return None

def menu_glowne(gracz, gracze):
    opcje = ['Pokaż postać', 'Walcz', 'Sklep', 'Ekwipunek', 'Trener', 'Zapisz grę', 'Wyjdź']
    while True:
        ui.wyswietl_menu('MENU', opcje)
        wybor_menu = ui.pobierz_wybor(1, len(opcje))
        if wybor_menu == 1:
            player.wyswietl_postac(gracz)
        elif wybor_menu == 2:
            combat.menu_walki(gracz)
        elif wybor_menu == 3:
            shop.menu_sklepu(gracz)
        elif wybor_menu == 4:
            equipment.menu_ekwipunku(gracz)
        elif wybor_menu == 5:
            skills.menu_trener(gracz)
        elif wybor_menu == 6:
            save.zapisz_gre(gracze)
        elif wybor_menu == 7:
            print('\nZakończono pomyślnie.\n')
            break

def main():
    gracze = menu_startowe()
    if gracze is not None:
        gracz = player.pobierz_gracza(gracze, gracze[0]['Nick'])
        menu_glowne(gracz, gracze)

if __name__ == "__main__":
    main()

