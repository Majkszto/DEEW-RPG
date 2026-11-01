"""
Skills system.

This file contains player skills
and functions for learning skills,
checking requirements and assigning
skills to combat slots.
"""

import ui

umiejetnosci = [
{
        'Nazwa': 'Mocne Uderzenie',
        'Klasa': 'Wojownik',
        'Rodzaj': 'Atak',
        'Poziom': 15,
        'Mana': 80,
        'Mnożnik obrażeń': 1.25,
        'Kryt szansa': 2,
        'Kryt mnożnik': 0.1,
        'Cena': 250},
{
        'Nazwa': 'Przebicie',
        'Klasa': 'Wojownik',
        'Rodzaj': 'Atak',
        'Poziom': 25,
        'Mana': 180,
        'Mnożnik obrażeń': 1.40,
        'Kryt szansa': 3,
        'Kryt mnożnik': 0.15,
        'Cena': 1000},
{
        'Nazwa': 'Uderzenie z Wyskoku',
        'Klasa': 'Wojownik',
        'Rodzaj': 'Atak',
        'Poziom': 40,
        'Mana': 400,
        'Mnożnik obrażeń': 1.55,
        'Kryt szansa': 4,
        'Kryt mnożnik': 0.2,
        'Cena': 5000},
{
        'Nazwa': 'Stalowa Szarża',
        'Klasa': 'Wojownik',
        'Rodzaj': 'Atak',
        'Poziom': 50,
        'Mana': 550,
        'Mnożnik obrażeń': 1.70,
        'Kryt szansa': 5,
        'Kryt mnożnik': 0.25,
        'Cena': 15000},
{
        'Nazwa': 'Brutalne Uderzenie',
        'Klasa': 'Wojownik',
        'Rodzaj': 'Atak',
        'Poziom': 62,
        'Mana': 750,
        'Mnożnik obrażeń': 1.85,
        'Kryt szansa': 6,
        'Kryt mnożnik': 0.3,
        'Cena': 40000},
{
        'Nazwa': 'Księżycowy Atak',
        'Klasa': 'Wojownik',
        'Rodzaj': 'Atak',
        'Poziom': 76,
        'Mana': 1400,
        'Mnożnik obrażeń': 2.00,
        'Kryt szansa': 7,
        'Kryt mnożnik': 0.35,
        'Cena': 100000},
{
        'Nazwa': 'Rozszczepienie Ziemi',
        'Klasa': 'Wojownik',
        'Rodzaj': 'Atak',
        'Poziom': 88,
        'Mana': 1800,
        'Mnożnik obrażeń': 2.15,
        'Kryt szansa': 8,
        'Kryt mnożnik': 0.4,
        'Cena': 250000},
{
        'Nazwa': 'Wężowy Atak',
        'Klasa': 'Wojownik',
        'Rodzaj': 'Atak',
        'Poziom': 93,
        'Mana': 2100,
        'Mnożnik obrażeń': 2.50,
        'Kryt szansa': 10,
        'Kryt mnożnik': 0.5,
        'Cena': 500000},
{
        'Nazwa': 'Wyrok Śmierci',
        'Klasa': 'Wojownik',
        'Rodzaj': 'Atak',
        'Poziom': 99,
        'Mana': 4800,
        'Mnożnik obrażeń': 3.50,
        'Kryt szansa': 40,
        'Kryt mnożnik': 1.0,
        'Cena': 1000000},
]

def trener_pokaz_umiejetnosci(gracz):
    do_nauczenia = trener_pobierz_umiejetnosci(gracz)
    if not do_nauczenia:
        print('\nWszystkie umiejętności zostały już nauczone!')
        return do_nauczenia
    ui.wyswietl_tytul('UMIEJĘTNOŚCI')
    for indeks, umiejetnosc_do_nauczenia in enumerate(do_nauczenia, start=1):
        for klucz2, wartosc2 in umiejetnosc_do_nauczenia.items():
            if klucz2 == 'Nazwa':
                print(f'\n{indeks}) {klucz2}: {wartosc2}')
            elif klucz2 == 'Kryt szansa':
                print(f'Szansa na cios krytyczny: +{wartosc2}%')
            elif klucz2 == 'Kryt mnożnik':
                print(f'Cios krytyczny: +{wartosc2 * 100:.0f}%')
            else:
                print(f'{klucz2}: {wartosc2}')
    return do_nauczenia

def trener_pobierz_umiejetnosci(gracz):
    do_nauczenia = []
    for umiejetnosc in umiejetnosci:
        znaleziono = False
        if umiejetnosc.get('Klasa'):
            if gracz['Klasa'] != umiejetnosc['Klasa']:
                znaleziono = True
        for umiejetnosc_gracza in gracz['Wyuczono']:
            if umiejetnosc_gracza['Nazwa'] == umiejetnosc['Nazwa']:
                znaleziono = True
        if not znaleziono:
            do_nauczenia.append(umiejetnosc)
    return do_nauczenia

def trener_naucz_umiejetnosci(gracz, numer_umiejetnosci):
    if numer_umiejetnosci < 1:
        return '\nNieprawidłowy numer umiejetnosci!'
    dostepne = trener_pobierz_umiejetnosci(gracz)
    if not dostepne:
        return None
    if numer_umiejetnosci > len(dostepne):
        return '\nNieprawidłowy numer umiejetnosci!'
    wybrana_umiejetnosc = dostepne[numer_umiejetnosci - 1]
    if gracz['Poziom'] >= wybrana_umiejetnosc['Poziom']:
        if gracz['Klasa'] == wybrana_umiejetnosc['Klasa']:
            if gracz['Złoto'] >= wybrana_umiejetnosc['Cena']:
                gracz['Złoto'] -= wybrana_umiejetnosc['Cena']
                gracz['Wyuczono'].append(wybrana_umiejetnosc.copy())
                return f'\nPomyślnie nauczono umiejętności "{wybrana_umiejetnosc['Nazwa']}"!'
            return f'\nNiewystarczająca ilość złota!\nPotrzebujesz: {wybrana_umiejetnosc['Cena']} złota!'
        return f'\nTa umiejętność jest przeznaczona dla klasy: {wybrana_umiejetnosc['Klasa']}!'
    return f'\nZbyt niski poziom gracza!\nWymagany: {wybrana_umiejetnosc['Poziom']} poziom!'

def pokaz_wybrane_umiejetnosci_postac(gracz):
    print('UMIEJĘTNOŚCI'.center(75))
    print('━' * 75)
    for slot, skill in gracz['Umiejętności'].items():
        if skill is not None:
            print(f'{slot}: {skill['Nazwa']} (Poziom: {skill['Poziom']})')
        else:
            print(f'{slot}: Brak')
    print('━' * 75)

def pokaz_wybrane_umiejetnosci(gracz):
    ui.wyswietl_tytul('UMIEJĘTNOŚCI')
    for slot, skill in gracz['Umiejętności'].items():
        if skill is not None:
            print(f'{slot}: {skill['Nazwa']} (Poziom: {skill['Poziom']})')
        else:
            print(f'{slot}: Brak')
    print('━' * 75)

def pokaz_wybrane_umiejetnosci_walka(gracz):
    niepuste = []
    for skill in gracz['Umiejętności'].values():
        if skill is None:
            continue
        niepuste.append(skill)
    if niepuste:
        ui.wyswietl_tytul('UMIEJĘTNOŚCI')
        for indeks, umka in enumerate(niepuste, start=1):
            for klucz, wartosc in umka.items():
                if klucz == 'Nazwa':
                    print(f'\n{indeks}) "{wartosc}"')
                elif klucz == 'Poziom':
                    print(f'{klucz}: {wartosc}')
                elif klucz == 'Mana':
                    print(f'{klucz}: {wartosc}')
    return niepuste

def pokaz_nauczone_umiejetnosci(gracz):
    ui.wyswietl_tytul('TWOJE UMIEJĘTNOŚCI')
    if gracz['Wyuczono']:
        for indeks, nauczone_skille in enumerate(gracz['Wyuczono'], start=1):
            for klucz1, wartosc1 in nauczone_skille.items():
                if klucz1 == 'Nazwa':
                    print(f'\n{indeks}) {klucz1}: {wartosc1}')
                elif klucz1 == 'Kryt szansa':
                    print(f'Szansa na cios krytyczny: +{wartosc1}%')
                elif klucz1 == 'Kryt mnożnik':
                    print(f'Cios krytyczny: +{wartosc1 * 100:.0f}%')
                else:
                    print(f'{klucz1}: {wartosc1}')
        return
    print('\nNie posiadasz jeszcze umiejętności!\n')

def ustaw_umiejetnosc_w_slocie(gracz):
    if gracz['Wyuczono']:
        pokaz_wybrane_umiejetnosci(gracz)
        print('\n0) Powrót')
        print('\nWybierz numer slotu: ')
        wybierz_slot = ui.pobierz_wybor(0, 5)
        if wybierz_slot < 0 or wybierz_slot > 5:
            print('\nMusisz wybrać slot od 1 do 5!')
            return
        if wybierz_slot == 0:
            return
        pokaz_nauczone_umiejetnosci(gracz)
        print('\nWybierz numer umiejętności: ')
        wybierz_umiejetnosc = ui.pobierz_wybor(1, len(gracz['Wyuczono']))
        if wybierz_umiejetnosc < 1 or wybierz_umiejetnosc > len(gracz['Wyuczono']):
            print('\nNieprawidłowy numer umiejętności!')
            return
        wybrana_umiejetnosc = gracz['Wyuczono'][wybierz_umiejetnosc - 1]
        znaleziono = False
        for wartosc in gracz['Umiejętności'].values():
            if wartosc == wybrana_umiejetnosc:
                znaleziono = True
        if not znaleziono:
            gracz['Umiejętności'][f'Slot {wybierz_slot}'] = wybrana_umiejetnosc
            print(f'\nPomyślnie ustawiono umiejętność "{wybrana_umiejetnosc['Nazwa']}" w Slot {wybierz_slot}!')
            return
        else:
            print(f'\nUmiejętność "{wybrana_umiejetnosc['Nazwa']}" znajduje się już w slocie!')
            return
    else:
        print('\nBrak dostępnych umiejętności!')
        return

def usun_umiejetnosc_ze_slotu(gracz):
    znaleziono = False
    for wartosc in gracz['Umiejętności'].values():
        if wartosc is not None:
            znaleziono = True
    if not znaleziono:
        print('\nBrak przypisanych umiejętności!')
        return
    pokaz_wybrane_umiejetnosci(gracz)
    print('\n0) Powrót')
    print('\nWybierz numer slotu umiejętności do usunięcia: ')
    wybierz_slot = ui.pobierz_wybor(0, 5)
    if wybierz_slot < 0 or wybierz_slot > 5:
        print('\nWybrano niepoprawny numer slotu!')
        return
    if wybierz_slot == 0:
        return
    if gracz['Umiejętności'][f'Slot {wybierz_slot}'] is None:
        print(f'\nSlot {wybierz_slot} jest pusty!')
        return
    usuniety = gracz['Umiejętności'][f'Slot {wybierz_slot}']
    gracz['Umiejętności'][f'Slot {wybierz_slot}'] = None
    print(f'\nPomyślnie usunięto "{usuniety['Nazwa']}" z Slot {wybierz_slot}!')

def menu_trener(gracz):
    while True:
        opcje_trener = ('Wybrane umiejętności', 'Nauczone umiejętności', 'Ustaw umiejętność w slocie', 'Usuń umiejętność ze slotu', 'Pokaż dostępne umiejętności', 'Trenuj umiejętność', 'Wyjście')
        ui.wyswietl_menu('TRENER', opcje_trener)
        opcja2 = ui.pobierz_wybor(1, len(opcje_trener))
        if opcja2 == 1:
            pokaz_wybrane_umiejetnosci(gracz)
        elif opcja2 == 2:
            pokaz_nauczone_umiejetnosci(gracz)
        elif opcja2 == 3:
            ustaw_umiejetnosc_w_slocie(gracz)
        elif opcja2 == 4:
            usun_umiejetnosc_ze_slotu(gracz)
        elif opcja2 == 5:
            trener_pokaz_umiejetnosci(gracz)
        elif opcja2 == 6:
            dostepne = trener_pokaz_umiejetnosci(gracz)
            if dostepne:
                print('\n0) Powrót')
                print('\nPodaj numer umiejętności, której chcesz się nauczyć: ')
                numer_umiejetnosci1 = ui.pobierz_wybor(0, len(dostepne))
                if numer_umiejetnosci1 == 0:
                    continue
                komunikat = trener_naucz_umiejetnosci(gracz, numer_umiejetnosci1)
                print(komunikat)
        elif opcja2 == 7:
            break
        else:
            print('\nWybierz poprawną opcję!')