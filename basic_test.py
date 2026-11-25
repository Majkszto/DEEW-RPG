import sqlite3
import database
import pytest
import player
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier


@pytest.fixture
def test_osobna_baza(tmp_path, monkeypatch):

    sciezka = tmp_path / 'test_rpg.db'

    monkeypatch.setattr(database, 'DB_PATH', sciezka)

    database.inicjalizuj_baze()

    polaczenie = database.polacz_z_baza()

    polaczenie.execute('''
        INSERT INTO konta (id_konta, email, login, haslo_hash, ranga)
        VALUES (1, 'dd@wp.pl', 'kup1', 'kup234', 'Gracz')
    ''')

    polaczenie.execute('''
        INSERT INTO konta (id_konta, email, login, haslo_hash, ranga)
        VALUES (2, 'ds@wp.pl', 'kup2', 'kup234', 'Gracz')
    ''')

    polaczenie.execute('''
        INSERT INTO konta (id_konta, email, login, haslo_hash, ranga)
        VALUES (3, 'dx@wp.pl', 'kup3', 'kup234', 'Gracz')
    ''')

    polaczenie.execute('''
        INSERT INTO serwery (id_serwera, nazwa, aktywny)
        VALUES (1, 'Manhatan', 1)
    ''')

    polaczenie.execute('''
        INSERT INTO serwery (id_serwera, nazwa, aktywny)
        VALUES (2, 'NewYork', 1)
    ''')

    polaczenie.commit()

    polaczenie.close()

    return sciezka

@pytest.fixture
def polaczenie_testowe(test_osobna_baza):

    polaczenie = database.polacz_z_baza()

    yield polaczenie

    polaczenie.close()

def test_usun_postac(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

    kursor.execute('''
        INSERT INTO postacie (id_postaci, id_konta, id_serwera, nick, plec, klasa, poziom, exp, zloto)
        VALUES (1, 1, 1, 'Mikibb', 'Kobieta', 'Wojownik', 69, 111, 111)
    ''')

    polaczenie_testowe.commit()

    wynik = database.usun_postac(1, 1, 1)

    assert wynik == 1

    kursor.execute('SELECT * FROM postacie')

    postacie = kursor.fetchall()

    assert len(postacie) == 0

def test_usun_jedna_z_dwoch_postaci(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

    kursor.execute('''
        INSERT INTO postacie (id_postaci, id_konta, id_serwera, nick, plec, klasa, poziom, exp, zloto)
        VALUES (1, 1, 1, 'Mikibb1', 'Kobieta', 'Wojownik', 69, 111, 111)
    ''')

    kursor.execute('''
        INSERT INTO postacie (id_postaci, id_konta, id_serwera, nick, plec, klasa, poziom, exp, zloto)
        VALUES (2, 2, 1, 'Mikibb2', 'Kobieta', 'Wojownik', 5, 0, 0)
    ''')

    kursor.execute('''
        INSERT INTO postacie (id_postaci, id_konta, id_serwera, nick, plec, klasa, poziom, exp, zloto)
        VALUES (3, 2, 1, 'Mikibb3', 'Kobieta', 'Wojownik', 99, 79, 79)
    ''')

    polaczenie_testowe.commit()

    wynik = database.usun_postac(1, 1, 1)

    assert wynik == 1

    kursor.execute('''
        SELECT * FROM postacie
    ''')

    postacie = kursor.fetchall()

    assert len(postacie) == 2

    assert not any(postac[0] == 1 for postac in postacie)

    assert any(postac[0] == 2 for postac in postacie)

    assert any(postac[0] == 3 for postac in postacie)


def test_usun_nieswoja_postac(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

    kursor.execute('''
        INSERT INTO postacie (id_postaci, id_konta, id_serwera, nick, plec, klasa, poziom, exp, zloto)
        VALUES (1, 1, 1, 'Mikibb2', 'Kobieta', 'Wojownik', 99, 79, 79)
    ''')

    kursor.execute('''
        INSERT INTO postacie (id_postaci, id_konta, id_serwera, nick, plec, klasa, poziom, exp, zloto)
        VALUES (2, 2, 1, 'Mikibb3', 'Kobieta', 'Wojownik', 99, 79, 79)
    ''')

    polaczenie_testowe.commit()

    wynik = database.usun_postac(1, 1, 2)

    assert wynik == 0

    kursor = polaczenie_testowe.cursor()

    kursor.execute('''
        SELECT * FROM postacie
    ''')

    postacie = kursor.fetchall()

    assert any(postac[0] == 2 for postac in postacie)

def test_dodaj_postac(polaczenie_testowe):

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

    database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                 atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                 blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    kursor = polaczenie_testowe.cursor()

    kursor.execute('''
        SELECT * FROM postacie
    ''')

    postacie = kursor.fetchall()

    kursor.execute('''
        SELECT * FROM statystyki
    ''')

    statystyki = kursor.fetchall()

    assert any(postac[3] == 'Kiszka' for postac in postacie)

    assert any(statystyka[6] == 5 for statystyka in statystyki)

    assert any(statystyka[2] == 10 for statystyka in statystyki)


def test_pobierz_postacie(test_osobna_baza):

    wynik = database.pobierz_postacie(999999, 1)

    assert wynik == []

def test_pobierz_postacie_lista(test_osobna_baza):

    wynik = database.pobierz_postacie(999999, 1)

    assert wynik == []

    assert isinstance(wynik, list)

def test_pobierz_istniejaca_postac(test_osobna_baza):

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

    dodano = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                  atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                  blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano == 1

    wynik = database.pobierz_postacie(1, 1)

    assert len(wynik) > 0

    assert any(postac[1] == 'Kiszka' for postac in wynik)

def test_usun_nieistniejaca_postac(test_osobna_baza):

    wynik = database.usun_postac(999999, 999999, 999999)

    assert wynik == 0

def test_duplikat_nicku(polaczenie_testowe):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                  atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                  blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    dodano2 = database.dodaj_postac(2, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano2 is None

    kursor = polaczenie_testowe.cursor()

    kursor.execute('''
        SELECT nick
        FROM postacie
        WHERE nick = ?
        AND id_serwera = ?
    ''', ('Kiszka', 1))

    wynik = kursor.fetchall()

    assert len(wynik) == 1

def test_ten_sam_nick_rozne_serwery(polaczenie_testowe):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    dodano2 = database.dodaj_postac(2, 2, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano2 is not None

    kursor = polaczenie_testowe.cursor()

    kursor.execute('''
        SELECT nick
        FROM postacie
        WHERE nick = ?
        AND id_serwera = ?
    ''', ('Kiszka', 1))

    wynik = kursor.fetchall()

    assert len(wynik) == 1

    kursor.execute('''
        SELECT nick
        FROM postacie
        WHERE nick = ?
        AND id_serwera = ?
    ''', ('Kiszka', 2))

    wynik2 = kursor.fetchall()

    assert len(wynik2) == 1


def test_usuniecie_postaci_usuwa_statystyki(polaczenie_testowe):

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

    dodano = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano is not None

    kursor = polaczenie_testowe.cursor()

    kursor.execute('''
        SELECT id_postaci
        FROM postacie
        WHERE nick = ?
        AND id_serwera = ?
    ''', ('Kiszka', 1))

    wynik = kursor.fetchall()

    assert wynik[0][0] == 1

    kursor.execute('''
        SELECT *
        FROM statystyki
        WHERE id_postaci = ?
    ''', (wynik[0][0],))

    wynik1 = kursor.fetchall()

    assert len(wynik1) == 1

    usunieto = database.usun_postac(1, 1, wynik[0][0])

    assert usunieto == 1

    kursor.execute('''
        SELECT *
        FROM statystyki
        WHERE id_postaci = ?
    ''', (wynik[0][0],))

    wynik2 = kursor.fetchall()

    assert len(wynik2) == 0

@pytest.mark.parametrize('HP, hp_max, mana, mana_max, atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona, blok, kryt_redukcja_szansy, kryt_redukcja_obrazen',
                         [
    (20, 10, 10, 10, 5, 10, 3, 1.25, 0, 0, 0, 0),
    (-10, 10, 10, 10, 5, 10, 3, 1.25, 0, 0, 0, 0),
    (20, -10, 10, 10, 5, 10, 3, 1.25, 0, 0, 0, 0),
    (10, 10, 20, 10, 5, 10, 3, 1.25, 0, 0, 0, 0),
    (10, 10, -10, 10, 5, 10, 3, 1.25, 0, 0, 0, 0),
    (10, 10, 10, 10, -1, 10, 3, 1.25, 0, 0, 0, 0),
    (10, 10, 10, 10, 5, -1, 3, 1.25, 0, 0, 0, 0),
    (10, 10, 10, 10, 5, 0, 3, 1.25, 0, 0, 0, 0),
    (10, 10, 10, 10, 5, 10, -1, 1.25, 0, 0, 0, 0),
    (10, 10, 10, 10, 5, 10, 3, -1, 0, 0, 0, 0),
    (10, 10, 10, 10, 5, 10, 3, 100, 0, 0, 0, 0),
    (10, 10, 10, 10, 5, 10, 3, 1.25, 0, 101, 0, 0),
    (10, 10, 10, 10, 5, 10, 3, 1.25, 0, -1, 0, 0),
    (10, 10, 10, 10, 5, 10, 3, 1.25, 0, 0, -1, 0),
    (10, 10, 10, 10, 5, 10, 3, 1.25, 0, 0, 101, 0),
    (10, 10, 10, 10, 5, 10, 3, 1.25, 0, 0, 0, -1),
    (10, 10, 10, 10, 5, 10, 3, 1.25, -1, 0, 0, 0)
],
ids=[
    'hp_wieksze_od_max',
    'ujemne_hp',
    'ujemne_hp_max',
    'mana_wieksza_od_max',
    'ujemna_mana',
    'ujemny_atak_min',
    'ujemny_atak_max',
    'atak_min_wiekszy_od_max',
    'ujemna_kryt_szansa',
    'ujemna_kryt_mnoznik',
    'za_wysoki_kryt_mnoznik',
    'za_wysoki_blok',
    'ujemny_blok',
    'ujemna_kryt_redukcja_szansy',
    'za_wysoka_kryt_redukcja_szansy',
    'ujemny_kryt_redukcja_obrazen',
    'ujemna_obrona',
])
def test_nieprawidlowe_statystyki(polaczenie_testowe, HP, hp_max, mana, mana_max, atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona, blok, kryt_redukcja_szansy, kryt_redukcja_obrazen):

    dodano = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                   atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                   blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano is None

    kursor = polaczenie_testowe.cursor()

    kursor.execute('''
        SELECT id_postaci
        FROM postacie
        WHERE nick = ?
    ''', ('Kiszka',))

    wynik = kursor.fetchall()

    assert wynik == []

    kursor.execute('''
        SELECT *
        FROM statystyki
    ''')

    wynik3 = kursor.fetchall()

    assert wynik3 == []


@pytest.mark.parametrize('HP, hp_max, mana, mana_max, atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona, blok, kryt_redukcja_szansy, kryt_redukcja_obrazen',
                         [
    (0, 10, 10, 10, 5, 10, 3, 1.25, 0, 0, 0, 0),
    (10, 10, 10, 10, 5, 10, 3, 1.25, 0, 0, 0, 0),
    (10, 10, 0, 10, 5, 10, 3, 1.25, 0, 0, 0, 0),
    (10, 10, 10, 10, 5, 10, 0, 1.25, 0, 0, 0, 0),
    (10, 10, 10, 10, 5, 10, 100, 1.25, 0, 0, 0, 0),
    (10, 10, 10, 10, 5, 10, 3, 1.25, 0, 100, 0, 0)],
    ids = [
    'hp_zero',
    'hp_rowne_max',
    'mana_zero',
    'kryt_szansa_zero',
    'kryt_szansa_100',
    'blok_100'
])
def test_graniczne_statystyki(polaczenie_testowe, HP, hp_max, mana, mana_max, atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona, blok, kryt_redukcja_szansy, kryt_redukcja_obrazen):

    dodano = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                   atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                   blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano is not None

    kursor = polaczenie_testowe.cursor()

    kursor.execute('''
        SELECT id_postaci
        FROM postacie
        WHERE nick = ?
    ''', ('Kiszka',))

    wynik = kursor.fetchall()

    assert wynik == [(dodano,)]

    kursor.execute('''
        SELECT HP, hp_max, mana, mana_max, atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona, blok, kryt_redukcja_szansy, kryt_redukcja_obrazen
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano,))

    wynik3 = kursor.fetchone()

    assert wynik3 == (HP, hp_max, mana, mana_max, atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona, blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)


def test_pobierz_tylko_swoje_postacie(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    dodano2 = database.dodaj_postac(2, 1, 'WOJWOJ', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano2 is not None

    pobrano = database.pobierz_postacie(2, 1)

    assert any(postac[1] == 'WOJWOJ' for postac in pobrano)

    assert not any(postac[1] == 'Kiszka' for postac in pobrano)

    assert len(pobrano) == 1

def test_odejmij_zloto(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    dodano = database.dodaj_zloto(dodano1, 500)

    assert dodano == 1

    pierwszy_zakup = database.odejmij_zloto(dodano1, 200)

    assert pierwszy_zakup == 1

    drugi_zakup = database.odejmij_zloto(dodano1, 400)

    assert drugi_zakup == 0

    kursor.execute('''
        SELECT zloto
        FROM postacie
        WHERE id_postaci = ?
    ''', (dodano1,))

    status = kursor.fetchone()

    assert status[0] == 301

def test_odejmij_ujemne_zloto(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    odjecie = database.odejmij_zloto(1, -1)

    assert odjecie == 0

    kursor.execute('''
        SELECT zloto
        FROM postacie
        WHERE id_postaci = ?
    ''', (dodano1,))

    status = kursor.fetchone()

    assert status[0] == 1

def test_dodaj_zloto(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    pierwszy_mob = database.dodaj_zloto(dodano1, 1)

    assert pierwszy_mob == 1

    kursor.execute('''
        SELECT zloto
        FROM postacie
        WHERE id_postaci = ?
    ''', (dodano1,))

    status = kursor.fetchone()

    assert status[0] == 2

    drugi_mob = database.dodaj_zloto(dodano1, 1)

    assert drugi_mob == 1

    kursor.execute('''
        SELECT zloto
        FROM postacie
        WHERE id_postaci = ?
    ''', (dodano1,))

    status = kursor.fetchone()

    assert status[0] == 3

    nieprawidlowa_nagroda = database.dodaj_zloto(dodano1, -500)

    assert nieprawidlowa_nagroda == 0

def test_dodaj_hp(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

    HP = 10
    hp_max = 100
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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    dodaj_hp = database.dodaj_hp(dodano1, 25)

    assert dodaj_hp == 1

    kursor.execute('''
        SELECT HP, hp_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status1 = kursor.fetchone()

    assert status1[0] == 35

    assert status1[1] == 100

    dodaj_hp2 = database.dodaj_hp(dodano1, 25)

    assert dodaj_hp2 == 1

    kursor.execute('''
        SELECT HP
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status3 = kursor.fetchone()

    assert status3[0] == 60

    dodaj_hp3 = database.dodaj_hp(dodano1, 500)

    assert dodaj_hp3 == 1

    kursor.execute('''
        SELECT HP, hp_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status4 = kursor.fetchone()

    assert status4[0] == 100

    assert status4[1] == 100

    dodaj_hp4 = database.dodaj_hp(dodano1, -500)

    assert dodaj_hp4 == 0

    kursor.execute('''
        SELECT HP, hp_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status5 = kursor.fetchone()

    assert status5[0] == 100

    assert status5[1] == 100


def test_odejmij_hp(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

    HP = 100
    hp_max = 100
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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    usun_hp = database.odejmij_hp(dodano1, 10)

    assert usun_hp == 1

    kursor.execute('''
        SELECT HP, hp_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status1 = kursor.fetchone()

    assert status1[0] == 90

    assert status1[1] == 100

    usun_hp2 = database.odejmij_hp(dodano1, 20)

    assert usun_hp2 == 1

    kursor.execute('''
        SELECT HP, hp_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status3 = kursor.fetchone()

    assert status3[0] == 70

    assert status3[1] == 100

    usun_hp3 = database.odejmij_hp(dodano1, -500)

    assert usun_hp3 == 0

    kursor.execute('''
        SELECT HP, hp_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status4 = kursor.fetchone()

    assert status4[0] == 70

    assert status4[1] == 100

    usun_hp4 = database.odejmij_hp(dodano1, 500)

    assert usun_hp4 == 1

    kursor.execute('''
        SELECT HP, hp_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status5 = kursor.fetchone()

    assert status5[0] == 0

    assert status5[1] == 100

    usun_hp5 = database.odejmij_hp(dodano1, 50)

    assert usun_hp5 == 1

    kursor.execute('''
        SELECT HP, hp_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status6 = kursor.fetchone()

    assert status6[0] == 0

    assert status6[1] == 100


def test_dodaj_mane(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

    HP = 10
    hp_max = 10
    mana = 10
    mana_max = 100
    atak_min = 5
    atak_max = 10
    kryt_szansa = 3
    kryt_mnoznik = 1.25
    obrona = 0
    blok = 0
    kryt_redukcja_szansy = 0
    kryt_redukcja_obrazen = 0

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    dodaj_mane = database.dodaj_mane(dodano1, 10)

    assert dodaj_mane == 1

    kursor.execute('''
        SELECT mana, mana_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status1 = kursor.fetchone()

    assert status1[0] == 20

    assert status1[1] == 100

    dodaj_mane2 = database.dodaj_mane(dodano1, 20)

    assert dodaj_mane2 == 1

    kursor.execute('''
        SELECT mana, mana_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status3 = kursor.fetchone()

    assert status3[0] == 40

    assert status3[1] == 100

    dodaj_mane3 = database.dodaj_mane(dodano1, 500)

    assert dodaj_mane3 == 1

    kursor.execute('''
        SELECT mana, mana_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status4 = kursor.fetchone()

    assert status4[0] == 100

    assert status4[1] == 100

    dodaj_mane4 = database.dodaj_mane(dodano1, -500)

    assert dodaj_mane4 == 0

    kursor.execute('''
        SELECT mana, mana_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status5 = kursor.fetchone()

    assert status5[0] == 100

    assert status5[1] == 100

    kursor.execute('''
        SELECT HP, hp_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status_hp = kursor.fetchone()

    assert status_hp[0] == 10

    assert status_hp[1] == 10

def test_odejmij_mane(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

    HP = 10
    hp_max = 10
    mana = 100
    mana_max = 100
    atak_min = 5
    atak_max = 10
    kryt_szansa = 3
    kryt_mnoznik = 1.25
    obrona = 0
    blok = 0
    kryt_redukcja_szansy = 0
    kryt_redukcja_obrazen = 0

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    usun_mane = database.odejmij_mane(dodano1, 10)

    assert usun_mane == 1

    kursor.execute('''
        SELECT mana, mana_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status1 = kursor.fetchone()

    assert status1[0] == 90

    assert status1[1] == 100

    usun_mane2 = database.odejmij_mane(dodano1, 20)

    assert usun_mane2 == 1

    kursor.execute('''
        SELECT mana, mana_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status3 = kursor.fetchone()

    assert status3[0] == 70

    assert status3[1] == 100

    usun_mane3 = database.odejmij_mane(dodano1, -500)

    assert usun_mane3 == 0

    kursor.execute('''
        SELECT mana, mana_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status4 = kursor.fetchone()

    assert status4[0] == 70

    assert status4[1] == 100

    usun_mane4 = database.odejmij_mane(dodano1, 500)

    assert usun_mane4 == 1

    kursor.execute('''
        SELECT mana, mana_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status5 = kursor.fetchone()

    assert status5[0] == 0

    assert status5[1] == 100

    usun_mane5 = database.odejmij_mane(dodano1, 50)

    assert usun_mane5 == 1

    kursor.execute('''
        SELECT mana, mana_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status6 = kursor.fetchone()

    assert status6[0] == 0

    assert status6[1] == 100

    kursor.execute('''
        SELECT HP, hp_max
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    status_hp = kursor.fetchone()

    assert status_hp[0] == 10

    assert status_hp[1] == 10

def test_dodaj_exp(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

    HP = 10
    hp_max = 10
    mana = 100
    mana_max = 100
    atak_min = 5
    atak_max = 10
    kryt_szansa = 3
    kryt_mnoznik = 1.25
    obrona = 0
    blok = 0
    kryt_redukcja_szansy = 0
    kryt_redukcja_obrazen = 0

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    kursor.execute('''
        SELECT exp, poziom
        FROM postacie
        WHERE id_postaci = ?
    ''', (dodano1,))

    bazowy_exp = kursor.fetchone()

    assert bazowy_exp[0] == 0

    assert bazowy_exp[1] == 1

    dodaj_exp1 = database.dodaj_exp(dodano1, 10)

    assert dodaj_exp1 == 1

    kursor.execute('''
        SELECT exp, poziom
        FROM postacie
        WHERE id_postaci = ?
    ''', (dodano1,))

    exp1 = kursor.fetchone()

    assert exp1[0] == 10

    assert exp1[1] == 1

    dodaj_exp2 = database.dodaj_exp(dodano1, 200)

    assert dodaj_exp2 == 1

    kursor.execute('''
        SELECT exp, poziom
        FROM postacie
        WHERE id_postaci = ?
    ''', (dodano1,))

    exp2 = kursor.fetchone()

    assert exp2[0] == 210

    assert exp2[1] == 1

    dodaj_exp3 = database.dodaj_exp(dodano1, -200)

    assert dodaj_exp3 == 0

    kursor.execute('''
        SELECT exp, poziom
        FROM postacie
        WHERE id_postaci = ?
    ''', (dodano1,))

    exp3 = kursor.fetchone()

    assert exp3[0] == 210

    assert exp3[1] == 1

def test_zapisz_awans(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    gracz = {
        'Poziom': 3,
        'Exp': 300,
        'Statystyki': {
           'HP': 150,
           'HP MAX': 150,
           'Mana': 30,
           'Mana MAX': 30,
           'Atak MIN': 15,
           'Atak MAX': 25,
           'Obrona': 10
        }
    }

    awans = database.zapisz_awans(dodano1, gracz)

    assert awans == 1

    kursor.execute('''
        SELECT exp, poziom
        FROM postacie
        WHERE id_postaci = ?
    ''', (dodano1,))

    wynik1 = kursor.fetchone()

    assert wynik1 == (300, 3)

    kursor.execute('''
        SELECT hp, hp_max, mana, mana_max, atak_min, atak_max, obrona
        FROM statystyki
        WHERE id_postaci = ?
    ''', (dodano1,))

    wynik2 = kursor.fetchone()

    assert wynik2 == (150, 150, 30, 30, 15, 25, 10)

def test_zapisz_awans_nieistniejacej_postaci(test_osobna_baza):

    gracz = {
        'Poziom': 3,
        'Exp': 300,
        'Statystyki': {
            'HP': 150,
            'HP MAX': 150,
            'Mana': 30,
            'Mana MAX': 30,
            'Atak MIN': 15,
            'Atak MAX': 25,
            'Obrona': 10
        }
    }

    awans = database.zapisz_awans(999999, gracz)

    assert awans == 0

def test_zapisz_awans_rollback(polaczenie_testowe):

    kursor = polaczenie_testowe.cursor()

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    gracz = {
        'Poziom': 3,
        'Exp': 300,
        'Statystyki': {
            'HP': 200,
            'HP MAX': 150,
            'Mana': 30,
            'Mana MAX': 30,
            'Atak MIN': 15,
            'Atak MAX': 25,
            'Obrona': 10
        }
    }

    with pytest.raises(sqlite3.IntegrityError):
        database.zapisz_awans(dodano1, gracz)

    kursor.execute('''
        SELECT exp, poziom
        FROM postacie
        WHERE id_postaci = ?
    ''', (dodano1,))

    wynik1 = kursor.fetchone()

    assert wynik1 == (0, 1)


def test_pobierz_gracza(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    gracz = database.pobierz_gracza(dodano1)

    assert isinstance(gracz, dict)

    assert gracz['Nick'] == 'Kiszka'
    assert gracz['Poziom'] == 1
    assert gracz['Exp'] == 0
    assert gracz['Złoto'] == 1
    assert gracz['Klasa'] == 'Wojownik'
    assert gracz['Statystyki']['HP'] == 10
    assert gracz['Statystyki']['HP MAX'] == 10
    assert gracz['Statystyki']['Mana'] == 10
    assert gracz['Statystyki']['Mana MAX'] == 10
    assert gracz['Statystyki']['Atak MIN'] == 5
    assert gracz['Statystyki']['Atak MAX'] == 10
    assert gracz['Statystyki']['Kryt szansa'] == 3
    assert gracz['Statystyki']['Kryt mnożnik'] == 1.25
    assert gracz['Statystyki']['Obrona'] == 0
    assert gracz['Statystyki']['Blok'] == 0
    assert gracz['Statystyki']['Kryt redukcja szansy'] == 0
    assert gracz['Statystyki']['Kryt redukcja obrażeń'] == 0


def test_pobierz_nieistniejacego_gracza(test_osobna_baza):

    wynik = database.pobierz_gracza(9999999)

    assert wynik is None

def test_pelny_awans_postaci(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    gracz_przed = database.pobierz_gracza(dodano1)

    assert isinstance(gracz_przed, dict)

    gracz_przed['Exp'] += 2000

    player.sprawdz_poziom(gracz_przed)

    awans = database.zapisz_awans(dodano1, gracz_przed)

    assert awans == 1

    gracz = database.pobierz_gracza(dodano1)

    assert isinstance(gracz, dict)
    assert gracz['Poziom'] == 3
    assert gracz['Exp'] == 300
    assert gracz['Statystyki']['HP'] == 110
    assert gracz['Statystyki']['HP MAX'] == 110
    assert gracz['Statystyki']['Mana'] == 15
    assert gracz['Statystyki']['Mana MAX'] == 15
    assert gracz['Statystyki']['Atak MIN'] == 10
    assert gracz['Statystyki']['Atak MAX'] == 17
    assert gracz['Statystyki']['Obrona'] == 2
    assert gracz['Statystyki']['Kryt szansa'] == 3
    assert gracz['Statystyki']['Kryt mnożnik'] == 1.25
    assert gracz['Statystyki']['Blok'] == 0
    assert gracz['Statystyki']['Kryt redukcja szansy'] == 0
    assert gracz['Statystyki']['Kryt redukcja obrażeń'] == 0


def test_przyznaj_exp_bez_awansu(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    wynik = player.przyznaj_exp(dodano1, 10)

    assert wynik == 1

    gracz = database.pobierz_gracza(dodano1)

    assert isinstance(gracz, dict)
    assert gracz['Poziom'] == 1
    assert gracz['Exp'] == 10
    assert gracz['Statystyki']['HP'] == 10
    assert gracz['Statystyki']['HP MAX'] == 10
    assert gracz['Statystyki']['Mana'] == 10
    assert gracz['Statystyki']['Mana MAX'] == 10
    assert gracz['Statystyki']['Atak MIN'] == 5
    assert gracz['Statystyki']['Atak MAX'] == 10
    assert gracz['Statystyki']['Obrona'] == 0
    assert gracz['Statystyki']['Kryt szansa'] == 3
    assert gracz['Statystyki']['Kryt mnożnik'] == 1.25
    assert gracz['Statystyki']['Blok'] == 0
    assert gracz['Statystyki']['Kryt redukcja szansy'] == 0
    assert gracz['Statystyki']['Kryt redukcja obrażeń'] == 0

def test_przyznaj_exp_z_awansem(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    wynik = player.przyznaj_exp(dodano1, 2000)

    assert wynik == 1

    gracz = database.pobierz_gracza(dodano1)

    assert isinstance(gracz, dict)
    assert gracz['Poziom'] == 3
    assert gracz['Exp'] == 300
    assert gracz['Statystyki']['HP'] == 110
    assert gracz['Statystyki']['HP MAX'] == 110
    assert gracz['Statystyki']['Mana'] == 15
    assert gracz['Statystyki']['Mana MAX'] == 15
    assert gracz['Statystyki']['Atak MIN'] == 10
    assert gracz['Statystyki']['Atak MAX'] == 17
    assert gracz['Statystyki']['Obrona'] == 2
    assert gracz['Statystyki']['Kryt szansa'] == 3
    assert gracz['Statystyki']['Kryt mnożnik'] == 1.25
    assert gracz['Statystyki']['Blok'] == 0
    assert gracz['Statystyki']['Kryt redukcja szansy'] == 0
    assert gracz['Statystyki']['Kryt redukcja obrażeń'] == 0

def test_przyznaj_exp_ujemny(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    wynik = player.przyznaj_exp(dodano1, -100)

    assert wynik == 0

    gracz = database.pobierz_gracza(dodano1)

    assert isinstance(gracz, dict)
    assert gracz['Poziom'] == 1
    assert gracz['Exp'] == 0
    assert gracz['Statystyki']['HP'] == 10
    assert gracz['Statystyki']['HP MAX'] == 10
    assert gracz['Statystyki']['Mana'] == 10
    assert gracz['Statystyki']['Mana MAX'] == 10
    assert gracz['Statystyki']['Atak MIN'] == 5
    assert gracz['Statystyki']['Atak MAX'] == 10
    assert gracz['Statystyki']['Obrona'] == 0
    assert gracz['Statystyki']['Kryt szansa'] == 3
    assert gracz['Statystyki']['Kryt mnożnik'] == 1.25
    assert gracz['Statystyki']['Blok'] == 0
    assert gracz['Statystyki']['Kryt redukcja szansy'] == 0
    assert gracz['Statystyki']['Kryt redukcja obrażeń'] == 0

def test_przyznaj_exp_nieistniejaca_postac(test_osobna_baza):

    wynik = player.przyznaj_exp(99999, 100)

    assert wynik == 0

    gracz = database.pobierz_gracza(99999)

    assert gracz is None

def test_przyznaj_exp_zero(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    wynik = player.przyznaj_exp(dodano1, 0)

    assert wynik == 1

    gracz = database.pobierz_gracza(dodano1)

    assert isinstance(gracz, dict)
    assert gracz['Poziom'] == 1
    assert gracz['Exp'] == 0
    assert gracz['Statystyki']['HP'] == 10
    assert gracz['Statystyki']['HP MAX'] == 10
    assert gracz['Statystyki']['Mana'] == 10
    assert gracz['Statystyki']['Mana MAX'] == 10
    assert gracz['Statystyki']['Atak MIN'] == 5
    assert gracz['Statystyki']['Atak MAX'] == 10
    assert gracz['Statystyki']['Obrona'] == 0
    assert gracz['Statystyki']['Kryt szansa'] == 3
    assert gracz['Statystyki']['Kryt mnożnik'] == 1.25
    assert gracz['Statystyki']['Blok'] == 0
    assert gracz['Statystyki']['Kryt redukcja szansy'] == 0
    assert gracz['Statystyki']['Kryt redukcja obrażeń'] == 0

def test_przyznaj_zloto(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    dodaj_zloto = player.przyznaj_zloto(dodano1, 100)

    assert dodaj_zloto == 1

    postac = database.pobierz_gracza(dodano1)

    assert postac['Złoto'] == 101
    assert postac['Exp'] == 0
    assert postac['Poziom'] == 1

def test_odejmij_cale_zloto(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    dodano = database.dodaj_zloto(dodano1, 499)

    assert dodano == 1

    pierwszy_zakup = database.odejmij_zloto(dodano1, 500)

    assert pierwszy_zakup == 1

    wynik = database.pobierz_gracza(dodano1)

    assert wynik['Złoto'] == 0

def test_przyznaj_exp_wspolbieznosc(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    bariera = Barrier(2)

    def przyznaj_exp_testowo(id_postaci, ilosc_exp):
        bariera.wait(timeout=5)
        return player.przyznaj_exp(id_postaci, ilosc_exp)

    with ThreadPoolExecutor(max_workers=2) as executor:

        operacja1 = executor.submit(przyznaj_exp_testowo, dodano1, 20)
        operacja2 = executor.submit(przyznaj_exp_testowo, dodano1, 30)

        wynik1 = operacja1.result()
        wynik2 = operacja2.result()

        assert wynik1 == 1
        assert wynik2 == 1

    wynik = database.pobierz_gracza(dodano1)

    assert wynik['Exp'] == 50
    assert wynik['Poziom'] == 1

def test_przyznaj_exp_wspolbieznosc_z_awansem(test_osobna_baza):

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    bariera = Barrier(2)

    def przyznaj_exp_testowo(id_postaci, ilosc_exp):
        bariera.wait(timeout=5)
        return player.przyznaj_exp(id_postaci, ilosc_exp)

    with ThreadPoolExecutor(max_workers=2) as executor:
        operacja1 = executor.submit(przyznaj_exp_testowo, dodano1, 60)
        operacja2 = executor.submit(przyznaj_exp_testowo, dodano1, 70)

        wynik1 = operacja1.result()
        wynik2 = operacja2.result()

        assert wynik1 == 1
        assert wynik2 == 1

    wynik = database.pobierz_gracza(dodano1)

    assert wynik['Exp'] == 30
    assert wynik['Poziom'] == 2
    assert wynik['Statystyki']['HP'] == 50
    assert wynik['Statystyki']['HP MAX'] == 50
    assert wynik['Statystyki']['Mana'] == 12
    assert wynik['Statystyki']['Mana MAX'] == 12
    assert wynik['Statystyki']['Atak MIN'] == 7
    assert wynik['Statystyki']['Atak MAX'] == 13
    assert wynik['Statystyki']['Obrona'] == 1
    assert wynik['Statystyki']['Kryt szansa'] == 3
    assert wynik['Statystyki']['Kryt mnożnik'] == 1.25
    assert wynik['Statystyki']['Blok'] == 0
    assert wynik['Statystyki']['Kryt redukcja szansy'] == 0
    assert wynik['Statystyki']['Kryt redukcja obrażeń'] == 0

def test_przyznaj_exp_rollback(test_osobna_baza, monkeypatch):

    oryginalna_funkcja = player.sprawdz_poziom

    def bledny_awans(gracz):
        oryginalna_funkcja(gracz)
        gracz['Statystyki']['HP'] = 999999

    monkeypatch.setattr(player, 'sprawdz_poziom', bledny_awans)

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

    dodano1 = database.dodaj_postac(1, 1, 'Kiszka', 'Kobieta', 'Wojownik', HP, hp_max, mana, mana_max,
                                    atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                                    blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)

    assert dodano1 is not None

    wynik1 = database.pobierz_gracza(dodano1)

    assert wynik1 is not None

    with pytest.raises(sqlite3.IntegrityError):
        player.przyznaj_exp(dodano1, 130)

    wynik2 = database.pobierz_gracza(dodano1)

    assert wynik1 == wynik2
