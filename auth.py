import database
import ui
import re
from argon2 import PasswordHasher
import pwinput
from argon2.exceptions import VerifyMismatchError
import sqlite3

ph = PasswordHasher()


def rejestracja():
    ui.wyswietl_tytul('DEEW RPG')
    print('Wpisz "0", żeby anulować w dowolnym momencie proces rejestracji!\n')

    while True:
        login = input('Login: ')
        if login == '0':
            print('\nAnulowano rejestrację!')
            print('━' * 75)
            return False
        if not 4 <= len(login) <= 16:
            print('\nNieprawidłowa ilość znaków (4 - 16)!\n')
        elif not login.isalnum():
            print('\nLogin może zawierać tylko litery i cyfry!\n')
        elif database.czy_login_zajety(login):
            print('\nTen login jest już zajęty!\n')
        else:
            print('━' * 75)
            break

    while True:
        email = input('E-mail: ')
        if email == '0':
            print('\nAnulowano rejestrację!')
            print('━' * 75)
            return False
        if not re.fullmatch(r'[^@\s]+@[^@\s.]+\.[^@\s.]+', email):
            print('\nNiepoprawny format e-mail!\n')
        elif database.czy_email_zajety(email):
            print('\nTen e-mail jest już zajęty!\n')
        else:
            print('━' * 75)
            break

    while True:
        haslo = pwinput.pwinput(prompt='Hasło: ', mask='*')
        if haslo == '0':
            print('\nAnulowano rejestrację!')
            print('━' * 75)
            return False
        if not 8 <= len(haslo) <= 64:
            print('\nNieprawidłowa ilość znaków (8 - 64)!\n')
        else:
            print('━' * 75)
            break

    while True:
        powtorz_haslo = pwinput.pwinput(prompt='Powtórz hasło: ', mask='*')
        if powtorz_haslo == '0':
            print('\nAnulowano rejestrację!')
            print('━' * 75)
            return False
        if not powtorz_haslo == haslo:
            print('\nHasła różnią się!\n')
        else:
            print('━' * 75)
            break

    haslo_hash = hashuj_haslo(haslo)

    if database.dodaj_konto(email, login, haslo_hash):
        print('Pomyślnie utworzono konto!')
        print('━' * 75)
        return True
    else:
        print('Nie udało się utworzyć konta!')
        print('━' * 75)
        return False

def hashuj_haslo(haslo):
    hash = ph.hash(haslo)
    return hash

def logowanie():
    ui.wyswietl_tytul('DEEW RPG')
    print('Wpisz "0", żeby anulować w dowolnym momencie procesu logowania!\n')

    while True:
        login = input('Login: ')
        if login == '0':
            print('\nAnulowano!')
            print('━' * 75)
            return None
        wynik = database.pobierz_konto(login)
        if wynik:
            print('━' * 75)
            break
        else:
            print('\nNieprawidłowy login!\n')

    haslozhashem = wynik[3]

    while True:
        haslo = pwinput.pwinput(prompt='Hasło: ', mask='*')
        if haslo == '0':
            print('\nAnulowano!')
            print('━' * 75)
            return None
        try:
            ph.verify(haslozhashem, haslo)
            print('\nZalogowano pomyślnie!')
            print('━' * 75)
            return wynik[0]

        except VerifyMismatchError:
            print('\nNieprawidłowe hasło!\n')


def menu_konta(id_konta):
    opcje = ['Wybierz serwer', 'Ustawienia konta', 'Wyloguj się']

    while True:
        ui.wyswietl_menu('DEEW RPG', opcje)
        wybor_konto = input()

        if wybor_konto == '1':
            while True:
                id_wybranego_serwera = wybor_serwera(id_konta)
                if id_wybranego_serwera is not None:
                    print(f'\nWybrano serwer {id_wybranego_serwera}!')
                    id_postaci = menu_postaci(id_konta, id_wybranego_serwera)
                    if id_postaci is not None:
                        print(f'\nRozpoczynanie gry postacią ID: {id_postaci}...')
                else:
                    break
        elif wybor_konto == '2':
            pass
            #tutaj menu ustawien konta
        elif wybor_konto == '3':
            print('\nWylogowano pomyślnie!')
            return None
        else:
            print('\nNieprawidłowa opcja!')


def wybor_serwera(id_konta):
    dostepne_serwery = database.pobierz_serwery()

    while True:
        ui.wyswietl_tytul('DEEW RPG')
        for indeks, dostepny_serwer in enumerate(dostepne_serwery, start=1):
            print(f'{indeks} - {dostepny_serwer[1]}')
        print('0 - Powrót')
        print('━' * 75)
        try:
            wybrany_serwer = int(input('\n'))
            if wybrany_serwer == 0:
                return None
            if not 1 <= wybrany_serwer <= len(dostepne_serwery):
                print('\nNieprawidłowy numer serwera!')
            else:
                id_serwera = dostepne_serwery[wybrany_serwer - 1][0]
                return id_serwera
        except ValueError:
            print('\nNieprawidłowa opcja!')

def menu_postaci(id_konta, id_serwera):
    opcje = ['Wybierz postać', 'Stwórz postać', 'Usuń postać', 'Powrót']

    while True:
        ui.wyswietl_menu('DEEW RPG', opcje)
        try:
            wybor_opcje_postac = int(input())
            if wybor_opcje_postac == 1:
                id_postaci = wybierz_postac(id_konta, id_serwera)
                if id_postaci is not None:
                    return id_postaci
            elif wybor_opcje_postac == 2:
                stworz_postac(id_konta, id_serwera)
            elif wybor_opcje_postac == 3:
                wynik = wybierz_postac_do_usuniecia(id_konta, id_serwera)
                if wynik is not None:
                    potwierdzenie_usuniecia = database.usun_postac(id_konta, id_serwera, wynik)
                    if potwierdzenie_usuniecia == 1:
                        print('\nPomyślnie usunięto postać!')
                    else:
                        print('\nNie udało się usunąć postaci!')
                else:
                    print('\nAnulowano usuwanie postaci.')
            elif wybor_opcje_postac == 4:
                return None
            else:
                print('\nNieprawidłowa opcja!')
        except ValueError:
            print('\nNieprawidłowa opcja!')
        except sqlite3.Error:
            print('\nWystąpił błąd bazy danych!')

def wybierz_postac(id_konta, id_serwera):
    postacie = database.pobierz_postacie(id_konta, id_serwera)
    if not postacie:
        print('\nBrak dostępnych postaci!')
        return None
    while True:
        ui.wyswietl_tytul('DEEW RPG')
        for indeks, postac in enumerate(postacie, start=1):
            print(f'{indeks}. {postac[1]} | {postac[2]} | Poziom: {postac[3]}')
        print('0 - Powrót')
        print('━' * 75)
        try:
            wybor_postaci = int(input('\n'))
            if wybor_postaci == 0:
                return None
            elif 1 <= wybor_postaci <= len(postacie):
                return postacie[wybor_postaci - 1][0]
            else:
                print('\nNieprawidłowa opcja!\n')

        except ValueError:
            print('\nNieprawidłowa opcja!\n')


def stworz_postac(id_konta, id_serwera):

    while True:
        ui.wyswietl_tytul('DEEW RPG')
        print('Tworzenie postaci!\nNick musi zawierać 4-16 znaków oraz nie może zawierać spacji!\nWpisz "0", żeby anulować.\n')
        nick = input('Nick: ')
        if nick == '0':
            return None
        if any(znak.isspace() for znak in nick):
            print('\nNick nie może zawierać spacji!')
        elif not 4 <= len(nick) <= 16:
            print('\nNick musi zawierać 4-16 znaków!')
        elif database.czy_nick_zajety(id_serwera, nick):
            print('\nTen nick jest już zajęty!!')
        else:
            break

    opcje = ['Mężczyzna', 'Kobieta', 'Powrót']

    while True:
        ui.wyswietl_menu('DEEW RPG', opcje)
        try:
            wybierz_plec = int(input('Wybierz płeć: '))
            if wybierz_plec == 1:
                wybrana_plec = 'Mężczyzna'
                print(f'\nWybrana płeć: {wybrana_plec}!')
                break
            elif wybierz_plec == 2:
                wybrana_plec = 'Kobieta'
                print(f'\nWybrana płeć: {wybrana_plec}!')
                break
            elif wybierz_plec == 3:
                return None
            else:
                print('\nNieprawidłowa opcja!')

        except ValueError:
            print('\nNieprawidłowa opcja!')

    opcje = ['Wojownik', 'Powrót']

    while True:
        ui.wyswietl_menu('DEEW RPG', opcje)
        try:
            wybierz_klase = int(input('Wybierz klasę: '))
            if wybierz_klase == 1:
                wybrana_klasa = 'Wojownik'
                print(f'\nWybrana klasa: {wybrana_klasa}!')
                break
            elif wybierz_klase == 2:
                return None
            else:
                print('\nNieprawidłowa opcja!')

        except ValueError:
            print('\nNieprawidłowa opcja!')

    HP = 10
    hp_max = 10
    mana = 10
    mana_max = 10
    atak_min = 5
    atak_max = 10
    kryt_szansa = 3
    kryt_mnoznik = 1.25
    obrona = 0
    blok = 0
    kryt_redukcja_szansy = 0
    kryt_redukcja_obrazen = 0
    id_postaci = database.dodaj_postac(id_konta, id_serwera, nick, wybrana_plec, wybrana_klasa, HP, hp_max, mana, mana_max,
                 atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                 blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    if id_postaci is None:
        print('\nNie udało się utworzyć postaci!')
        return None
    return id_postaci

def wybierz_postac_do_usuniecia(id_konta, id_serwera):
    postacie = database.pobierz_postacie(id_konta, id_serwera)
    if not postacie:
        print('\nBrak dostępnych postaci!')
        return None

    while True:
        ui.wyswietl_tytul('DEEW RPG')
        for indeks, postac in enumerate(postacie, start=1):
            print(f'{indeks}. {postac[1]} | {postac[2]} | Poziom: {postac[3]}')
        print('0. Powrót')
        print('━' * 75)
        try:
            wybierz_postac = int(input('\nWybierz postać do usunięcia: '))
            if wybierz_postac == 0:
                return None
            if not 1 <= wybierz_postac <= len(postacie):
                print('\nNieprawidłowy numer postaci!')
            else:
                id_wybranej_postaci = postacie[wybierz_postac - 1][0]
                nick_wybranej_postaci = postacie[wybierz_postac - 1][1]
                print('\nUWAGA! Usunięcie postaci jest nieodwracalne!')
                potwierdzenie_nicku = input('\nAby potwierdzić usunięcie postaci, wpisz jej nick: ')
                if potwierdzenie_nicku == nick_wybranej_postaci:
                    return id_wybranej_postaci
                else:
                    print('\nNieprawidłowy nick!')
                    return None
        except ValueError:
            print('\nNieprawidłowa opcja!')