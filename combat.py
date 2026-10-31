"""
Combat system.

This file contains functions for battles,
damage, critical hits, blocking
and using skills in combat.
"""

import random
import skills
import player
import drop
import mobs
import ui

def zredukuj_kryt(szansa):
    if szansa > 100:
        szansa = 100
    elif szansa < 0:
        szansa = 0
    return szansa

def oblicz_obrazenia(atak, obrona):
    obrazenia = atak - obrona
    if obrazenia < 1:
        obrazenia = 1
    return obrazenia

def wykonaj_atak(atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona, hp, blok=0):
    los_bloku = random.randint(1, 100)
    if los_bloku <= blok:
        return 0, hp, False, True
    krytyk = False
    czy_blok = False
    obrazenia_atak = random.randint(atak_min, atak_max)
    twoj_kryt = zredukuj_kryt(kryt_szansa)
    kryt = random.randint(1, 100)
    if kryt <= twoj_kryt:
        obrazenia_atak = obrazenia_atak * kryt_mnoznik
        obrazenia_atak = int(obrazenia_atak)
        krytyk = True
    obrazenia_atakujacego = oblicz_obrazenia(obrazenia_atak, obrona)
    hp -= obrazenia_atakujacego
    if hp < 0:
        hp = 0
    return  obrazenia_atakujacego, hp, krytyk, czy_blok

def wykonaj_skill(atakujacy, broniacy, hp_obrona, wybrana, blok=0):
    if wybrana['Rodzaj'] == 'Atak':
        kryt_skill = False
        czy_blok = False
        if atakujacy['Statystyki']['Mana'] >= wybrana['Mana']:
            atakujacy['Statystyki']['Mana'] -= wybrana['Mana']
            los_bloku = random.randint(1, 100)
            if los_bloku <= blok:
                return True, 0, hp_obrona, False, True
            mnoznik_obrazen = wybrana['Mnożnik obrażeń']
            obrazenia_atak = random.randint(atakujacy['Statystyki']['Atak MIN'], atakujacy['Statystyki']['Atak MAX'])
            obrazenia_atak = obrazenia_atak * mnoznik_obrazen
            szansa_kryt = zredukuj_kryt(atakujacy['Statystyki']['Kryt szansa'] + wybrana['Kryt szansa'])
            kryt_umka = random.randint(1, 100)
            if kryt_umka <= szansa_kryt:
                total_kryt = atakujacy['Statystyki']['Kryt mnożnik'] + wybrana['Kryt mnożnik']
                obrazenia_atak = obrazenia_atak * total_kryt
                kryt_skill = True
            obrazenia_atak = int(obrazenia_atak)
            obrazenia_atakujacego = oblicz_obrazenia(obrazenia_atak, broniacy['Statystyki']['Obrona'])
            hp_obrona -= obrazenia_atakujacego
            if hp_obrona < 0:
                hp_obrona = 0
            return True, obrazenia_atakujacego, hp_obrona, kryt_skill, czy_blok
        return False, None, hp_obrona, False, False
    return False, None, hp_obrona, False, False

def wygrana(gracz, hp_atak, mob):
    print(f'\n\033[1;32mZWYCIĘSTWO! Pokonano: {mob["Nazwa"]} (Poziom: {mob["Poziom"]})!\033[0m')
    gracz['Statystyki']['HP'] = hp_atak
    gracz['Statystyki']['Mana'] = gracz['Statystyki']['Mana MAX']
    gracz['Złoto'] += mob['Złoto']
    if gracz['Poziom'] > mob['Poziom']:
        roznica = min(gracz['Poziom'] - mob['Poziom'], 10)
        zdobyty_exp = mob['Exp'] - (mob['Exp'] * roznica / 10)
        zdobyty_exp = int(zdobyty_exp)
    else:
        zdobyty_exp = mob['Exp']
    gracz['Exp'] += zdobyty_exp
    print(f'\n\033[1;32mZdobyto: {zdobyty_exp} XP oraz {mob['Złoto']} złota!\033[0m')
    player.sprawdz_poziom(gracz)
    drop.wykonaj_drop(gracz, mob)

def przegrana(gracz, hp_atak, mob):
    print(f'\n\033[1;31mPORAŻKA! {gracz['Nick']} poległ w walce z {mob['Nazwa']} (Poziom: {mob['Poziom']})!\033[0m')
    gracz['Statystyki']['HP'] = hp_atak
    gracz['Statystyki']['Mana'] = gracz['Statystyki']['Mana MAX']

def wybierz_umiejetnosc(gracz):
    dostepne = skills.pokaz_wybrane_umiejetnosci_walka(gracz)
    if dostepne:
        print('\nWybierz numer umiejętności: ')
        numer_umiejetnosci = ui.pobierz_wybor(1, len(dostepne))
        wybrana = dostepne[numer_umiejetnosci - 1]
        return True, wybrana
    return False, None

def walka(gracz, lista2, przeciwnik):
    tura = 1
    if gracz['Statystyki']['HP'] <= 0:
        print(f'\nMusisz najpierw się uleczyć!')
        return
    mob = mobs.pobierz_moba(lista2, przeciwnik)
    if mob is None:
        print(f'Brak moba "{przeciwnik}"!')
        return
    hp_atak = gracz['Statystyki']['HP']
    hp_obrona = mob['Statystyki']['HP']
    opcje = ['Atak', 'Umiejętność']
    while True:
        ui.wyswietl_menu('WALKA', opcje)
        wybor_ataku = ui.pobierz_wybor(1, len(opcje))
        if wybor_ataku == 1:
            blok = mob['Statystyki']['Blok']
            obrazenia_atakujacego, hp_obrona, krytyk, czy_blok = wykonaj_atak(gracz['Statystyki']['Atak MIN'], gracz['Statystyki']['Atak MAX'], gracz['Statystyki']['Kryt szansa'], gracz['Statystyki']['Kryt mnożnik'], mob['Statystyki']['Obrona'], hp_obrona, blok)
            ui.wyswietl_ture(tura)
            if czy_blok:
                print(f'\n{mob['Nazwa']} blokuje Twój atak!')
                print(f'Pozostała mana: {gracz['Statystyki']['Mana']}/{gracz['Statystyki']['Mana MAX']}')
            if krytyk:
                ui.wyswietl_kryt()
            if not czy_blok:
                print(f'\n{gracz['Nick']} atakuje przeciwnika "{mob['Nazwa']}"!')
                print(f'Zadane obrażenia: {obrazenia_atakujacego}')
                print(f'Pozostałe HP przeciwnika: {hp_obrona}')
                print(f'Pozostała mana: {gracz['Statystyki']['Mana']}/{gracz['Statystyki']['Mana MAX']}')
        elif wybor_ataku == 2:
            blok = mob['Statystyki']['Blok']
            status2, wybrana = wybierz_umiejetnosc(gracz)
            if not status2:
                print('\nBrak dostępnych umiejętności!')
                continue
            status1, obrazenia_atakujacego, hp_obrona, kryt_skill, czy_blok1 = wykonaj_skill(gracz, mob, hp_obrona, wybrana, blok)
            if status1:
                ui.wyswietl_ture(tura)
                if czy_blok1:
                    print(f'\n{mob['Nazwa']} blokuje umiejętność "{wybrana['Nazwa']}"!')
                    print(f'Pozostała mana: {gracz['Statystyki']['Mana']}/{gracz['Statystyki']['Mana MAX']}')
                if kryt_skill:
                    ui.wyswietl_kryt()
                if not czy_blok1:
                    print(f'\n{gracz['Nick']} używa umiejętności "{wybrana['Nazwa']}"!')
                    print(f'Zadane obrażenia: {obrazenia_atakujacego}')
                    print(f'Pozostałe HP przeciwnika: {hp_obrona}')
                    print(f'Pozostała mana: {gracz['Statystyki']['Mana']}/{gracz['Statystyki']['Mana MAX']}')
            else:
                print('\nMasz za mało many!')
                continue

        if hp_obrona == 0:
            wygrana(gracz, hp_atak, mob)
            break
        blok = gracz['Statystyki']['Blok']
        kryt_szansa_mob = max(0, mob['Statystyki']['Kryt szansa'] - gracz['Statystyki']['Kryt redukcja szansy'])
        kryt_mnoznik_mob = max(1.0, mob['Statystyki']['Kryt mnożnik'] - gracz['Statystyki']['Kryt redukcja obrażeń'] / 100)
        obrazenia_broniacego, hp_atak, krytyk_mob, czy_blok_mob = wykonaj_atak(mob['Statystyki']['Atak MIN'], mob['Statystyki']['Atak MAX'], kryt_szansa_mob, kryt_mnoznik_mob, gracz['Statystyki']['Obrona'], hp_atak, blok)
        tura += 1
        if czy_blok_mob:
            print(f'\nBlokujesz atak przeciwnika "{mob['Nazwa']}"!')
        if krytyk_mob:
            ui.wyswietl_kryt()
        if not czy_blok_mob:
            print(f'\n{mob['Nazwa']} atakuje!')
            print(f'Otrzymane obrażenia: {obrazenia_broniacego}')
            print(f'Pozostałe HP: {hp_atak}')
        if hp_atak == 0:
            przegrana(gracz, hp_atak, mob)
            break

def menu_walki(gracz):
    while True:
        zyje = gracz['Statystyki']['HP'] >= 1
        if zyje:
            if not mobs.moby:
                print('\nBrak mobów!')
                break
            wybrana_mapa = mobs.wybierz_mape(mobs.mapy, gracz)
            if wybrana_mapa == 0:
                break
            if wybrana_mapa is not None:
                dostepne_moby = mobs.moby_na_mapie(mobs.moby, wybrana_mapa)
                if not dostepne_moby:
                    print('\nNa tej mapie nie ma przeciwników!')
                    continue
                opcje = ['Walcz', 'Powrót']
                while True:
                    mobs.pokaz_liste_mobow(dostepne_moby)
                    wybor_moba = ui.pobierz_wybor(0, len(dostepne_moby))
                    if wybor_moba == 0:
                        break
                    mobek = dostepne_moby[wybor_moba - 1]
                    mobs.pokaz_moba(mobek)
                    przeciwnik = mobek['Nazwa']
                    ui.wyswietl_menu('WALKA', opcje)
                    wybor2 = ui.pobierz_wybor(1, len(opcje))
                    if wybor2 == 1:
                        walka(gracz, mobs.moby, przeciwnik)
                        if gracz['Statystyki']['HP'] <= 0:
                            break
                    elif wybor2 == 2:
                        continue
        else:
            print('\nMusisz najpierw się uleczyć!')
            break