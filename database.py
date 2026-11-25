import sqlite3

DB_PATH = 'deew_rpg_test.db'

def polacz_z_baza():

    polaczenie = sqlite3.connect(DB_PATH)

    polaczenie.execute('PRAGMA foreign_keys = ON')

    return polaczenie

def inicjalizuj_baze():

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            CREATE TABLE IF NOT EXISTS konta (
            id_konta INTEGER PRIMARY KEY,
            email TEXT NOT NULL UNIQUE,
            login TEXT NOT NULL UNIQUE,
            haslo_hash TEXT NOT NULL,
            ranga TEXT NOT NULL DEFAULT 'Gracz')
        ''')

        kursor.execute('''
            CREATE TABLE IF NOT EXISTS serwery (
            id_serwera INTEGER PRIMARY KEY,
            nazwa TEXT NOT NULL UNIQUE,
            aktywny INTEGER NOT NULL DEFAULT 1 CHECK (aktywny IN (0, 1)))
        ''')

        kursor.execute('''
            CREATE TABLE IF NOT EXISTS postacie (
            id_postaci INTEGER PRIMARY KEY,
            id_konta INTEGER NOT NULL,
            id_serwera INTEGER NOT NULL,
            nick TEXT NOT NULL,
            plec TEXT NOT NULL,
            klasa TEXT NOT NULL,
            poziom INTEGER NOT NULL DEFAULT 1 CHECK (poziom BETWEEN 1 AND 99),
            exp INTEGER NOT NULL DEFAULT 0 CHECK (exp >= 0),
            zloto INTEGER NOT NULL DEFAULT 1 CHECK (zloto >= 0),
            FOREIGN KEY (id_konta) REFERENCES konta(id_konta),
            FOREIGN KEY (id_serwera) REFERENCES serwery(id_serwera),
            UNIQUE(id_serwera, nick))
        ''')

        kursor.execute('''
            CREATE TABLE IF NOT EXISTS statystyki (
            id_statystyki INTEGER PRIMARY KEY,
            id_postaci INTEGER NOT NULL UNIQUE,
            HP INTEGER NOT NULL CHECK (HP >= 0) CHECK (HP <= hp_max),
            hp_max INTEGER NOT NULL CHECK (hp_max >= 1),
            mana INTEGER NOT NULL CHECK (mana >= 0) CHECK (mana <= mana_max),
            mana_max INTEGER NOT NULL CHECK (mana_max >= 0),
            atak_min REAL NOT NULL CHECK (atak_min >= 0) CHECK (atak_min <= atak_max),
            atak_max REAL NOT NULL CHECK (atak_max >= 1),
            kryt_szansa REAL NOT NULL CHECK (kryt_szansa BETWEEN 0 AND 100),
            kryt_mnoznik REAL NOT NULL CHECK (kryt_mnoznik BETWEEN 0 AND 10),
            obrona REAL NOT NULL CHECK (obrona >= 0),
            blok INTEGER NOT NULL CHECK (blok BETWEEN 0 AND 100),
            kryt_redukcja_szansy REAL NOT NULL CHECK (kryt_redukcja_szansy BETWEEN 0 AND 100),
            kryt_redukcja_obrazen REAL NOT NULL CHECK (kryt_redukcja_obrazen >= 0),
            FOREIGN KEY (id_postaci) REFERENCES postacie(id_postaci)
            ON DELETE CASCADE)
        ''')

        polaczenie.commit()
        print('\nBaza danych gotowa!')

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()


def sprawdz_klucze_obce():

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('PRAGMA foreign_key_list(statystyki)')

        wyniki = kursor.fetchall()

        if wyniki:
            for wynik in wyniki:
                print()
                print(wynik)
        else:
            print('\nNie znaleziono kluczy obcych w tabeli statystyki!')

        kursor.execute('PRAGMA table_info(postacie)')

        wyniki2 = kursor.fetchall()

        if wyniki2:
            for wynik2 in wyniki2:
                print(wynik2)
        else:
            print('\nNie znaleziono tabeli postacie!')

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()


def dodaj_konto(email, login, haslo_hash):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            INSERT INTO konta (email, login, haslo_hash)
            VALUES (?, ?, ?)
        ''', (email, login, haslo_hash))

        polaczenie.commit()
        return True

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        if polaczenie is not None:
            polaczenie.rollback()
        return False

    finally:
        if polaczenie is not None:
            polaczenie.close()


def sprawdz_konto(login):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            SELECT id_konta, login, ranga
            FROM konta
            WHERE login = ?
        ''', (login,))

        wyniki = kursor.fetchone()

        if wyniki:
            print(wyniki)
        else:
            print('\nNie znaleziono konta o podanym loginie!')

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()

def dodaj_serwer(nazwa):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            INSERT INTO serwery (nazwa)
            VALUES (?)
        ''', (nazwa,))

        polaczenie.commit()
        return True


    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        if polaczenie is not None:
            polaczenie.rollback()
        return False

    finally:
        if polaczenie is not None:
            polaczenie.close()

def pobierz_serwery():

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            SELECT id_serwera, nazwa
            FROM serwery
            WHERE aktywny = 1
        ''')

        wyniki = kursor.fetchall()

        return wyniki

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()




def dodaj_postac(id_konta, id_serwera, nick, plec, klasa, HP, hp_max, mana, mana_max,
                 atak_min, atak_max, kryt_szansa, kryt_mnoznik, obrona,
                 blok, kryt_redukcja_szansy, kryt_redukcja_obrazen):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            INSERT INTO postacie (id_konta, id_serwera, nick, plec, klasa)
            VALUES (?, ?, ?, ?, ?)
        ''', (id_konta, id_serwera, nick, plec, klasa))

        id_postaci = kursor.lastrowid

        kursor.execute('''
            INSERT INTO statystyki (
            id_postaci, HP, hp_max, mana, mana_max,
            atak_min, atak_max, kryt_szansa, kryt_mnoznik,
            obrona, blok, kryt_redukcja_szansy, kryt_redukcja_obrazen)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            id_postaci, HP, hp_max, mana, mana_max,
            atak_min, atak_max, kryt_szansa, kryt_mnoznik,
            obrona, blok, kryt_redukcja_szansy, kryt_redukcja_obrazen
        ))

        polaczenie.commit()
        print(f'\nPomyślnie utworzono postać: {nick}!\nID POSTACI: {id_postaci}')
        return id_postaci

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        return None

    finally:
        if polaczenie is not None:
            polaczenie.close()


def pokaz_postac(id_postaci):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            SELECT nick, klasa, poziom, HP, hp_max, mana, mana_max
            FROM statystyki
            JOIN postacie
            ON postacie.id_postaci = statystyki.id_postaci
            WHERE postacie.id_postaci = ?
        ''', (id_postaci,))

        wynik = kursor.fetchone()

        if wynik:
            print('━' * 75)
            print('DEEW RPG'.center(75))
            print('━' * 75)
            print(f'Nick: {wynik[0]}\nKlasa: {wynik[1]}\nPoziom: {wynik[2]}\nHP: {wynik[3]}/{wynik[4]}\nMana: {wynik[5]}/{wynik[6]}')
            print('━' * 75)
        else:
            print(f'\nNie znaleziono postaci o ID: {id_postaci}!')

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()

def pobierz_postacie(id_konta, id_serwera):
    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            SELECT id_postaci, nick, klasa, poziom
            FROM postacie
            WHERE id_konta = ? AND id_serwera = ?
        ''', (id_konta, id_serwera))

        wynik = kursor.fetchall()

        return wynik

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()



def aktualizuj_hp(id_postaci, nowe_hp):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            UPDATE statystyki
            SET HP = ?
            WHERE id_postaci = ?
        ''', (nowe_hp, id_postaci))

        polaczenie.commit()

        if kursor.rowcount > 0:
            print(f'\nPomyślnie zmieniono HP na {nowe_hp}!')
        else:
            print(f'\nNie znaleziono postaci o ID: {id_postaci}!')

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')

    finally:
        if polaczenie is not None:
            polaczenie.close()


def czy_login_zajety(login):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            SELECT login
            FROM konta
            WHERE login = ?
        ''', (login,))

        wynik = kursor.fetchone()

        if wynik:
            return True
        return False

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()

def czy_email_zajety(email):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            SELECT email
            FROM konta
            WHERE email = ?
        ''', (email,))

        wynik = kursor.fetchone()

        if wynik:
            return True
        return False

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()

def czy_nick_zajety(id_serwera, nick):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            SELECT nick
            FROM postacie
            WHERE id_serwera = ? 
            AND nick = ?
        ''', (id_serwera, nick))

        wynik = kursor.fetchone()

        if wynik:
            return True
        return False

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()


def pobierz_konto(login):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            SELECT id_konta, login, email, haslo_hash, ranga
            FROM konta
            WHERE login = ?
        ''', (login,))

        wynik = kursor.fetchone()

        if wynik:
            return wynik
        return None

    except sqlite3.Error as blad:
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()

def resetuj_postacie():

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('BEGIN')
        kursor.execute('DROP TABLE IF EXISTS statystyki')
        kursor.execute('DROP TABLE IF EXISTS postacie')

        polaczenie.commit()
        print('\nReset postaci powiódł się!')

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()

def usun_postac(id_konta, id_serwera, id_postaci):

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            DELETE FROM postacie
            WHERE id_postaci = ?
            AND id_konta = ?
            AND id_serwera = ?
        ''', (id_postaci, id_konta, id_serwera,))

        polaczenie.commit()

        wynik = kursor.rowcount

        return wynik

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()




def sprawdz_cascade():
    polaczenie = polacz_z_baza()
    try:
        kursor = polaczenie.cursor()
        kursor.execute('PRAGMA foreign_key_list(statystyki)')
        print()
        print(kursor.fetchall())
    finally:
        polaczenie.close()

def sprawdz_usuwanie():
    polaczenie = polacz_z_baza()
    try:
        kursor = polaczenie.cursor()

        kursor.execute('SELECT * FROM postacie')
        print('\nPOSTACIE:', kursor.fetchall())

        kursor.execute('SELECT * FROM statystyki')
        print('\nSTATYSTYKI:', kursor.fetchall())

    finally:
        polaczenie.close()

def dodaj_zloto(id_postaci, ilosc):

    if ilosc < 0:
        return 0

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            UPDATE postacie
            SET zloto = zloto + ?
            WHERE id_postaci = ?
        ''', (ilosc, id_postaci))

        wynik = kursor.rowcount

        polaczenie.commit()

        return wynik

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()

def odejmij_zloto(id_postaci, ilosc):

    if ilosc < 0:
        return 0

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            UPDATE postacie
            SET zloto = zloto - ?
            WHERE id_postaci = ?
            AND zloto >= ?
        ''', (ilosc, id_postaci, ilosc))

        wynik = kursor.rowcount

        polaczenie.commit()

        return wynik

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()



def dodaj_hp(id_postaci, ilosc):
    if ilosc <= 0:
        return 0

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            UPDATE statystyki
            SET HP = MIN(hp_max, HP + ?)
            WHERE id_postaci = ?
        ''', (ilosc, id_postaci))

        wynik = kursor.rowcount

        polaczenie.commit()

        return wynik

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()


def odejmij_hp(id_postaci, ilosc):
    if ilosc <= 0:
        return 0

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            UPDATE statystyki
            SET HP = MAX(0, HP - ?)
            WHERE id_postaci = ?
        ''', (ilosc, id_postaci))

        wynik = kursor.rowcount

        polaczenie.commit()

        return wynik

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()

def dodaj_mane(id_postaci, ilosc):
    if ilosc <= 0:
        return 0

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            UPDATE statystyki
            SET mana = MIN(mana_max, mana + ?)
            WHERE id_postaci = ?
        ''', (ilosc, id_postaci))

        wynik = kursor.rowcount

        polaczenie.commit()

        return wynik

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()

def odejmij_mane(id_postaci, ilosc):
    if ilosc <= 0:
        return 0

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            UPDATE statystyki
            SET mana = MAX(0, mana - ?)
            WHERE id_postaci = ?
        ''', (ilosc, id_postaci))

        wynik = kursor.rowcount

        polaczenie.commit()

        return wynik

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()

def dodaj_exp(id_postaci, ilosc):
    if ilosc <= 0:
        return 0

    polaczenie = None

    try:
        polaczenie = polacz_z_baza()

        kursor = polaczenie.cursor()

        kursor.execute('''
            UPDATE postacie
            SET exp = exp + ?
            WHERE id_postaci = ?
        ''',(ilosc, id_postaci))

        wynik = kursor.rowcount

        polaczenie.commit()

        return wynik

    except sqlite3.Error as blad:
        if polaczenie is not None:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if polaczenie is not None:
            polaczenie.close()


def wymagany_exp(poziom):

    wymagany = int(100 * poziom ** 4)

    return wymagany

def zapisz_awans(id_postaci, gracz, polaczenie=None):

    wlasne_polaczenie = False

    poziom = gracz['Poziom']
    exp = gracz['Exp']
    statystyki = gracz['Statystyki']

    if polaczenie is None:
        polaczenie = polacz_z_baza()
        wlasne_polaczenie = True

    try:

        kursor = polaczenie.cursor()

        kursor.execute('''
            UPDATE postacie
            SET poziom = ?, exp = ?
            WHERE id_postaci = ?
        ''', (poziom, exp, id_postaci))

        wynik1 = kursor.rowcount

        kursor.execute('''
            UPDATE statystyki
            SET HP = ?, hp_max = ?, mana = ?, mana_max = ?, atak_min = ?, atak_max = ?, obrona = ?
            WHERE id_postaci = ?
        ''', (statystyki['HP'], statystyki['HP MAX'], statystyki['Mana'], statystyki['Mana MAX'], statystyki['Atak MIN'], statystyki['Atak MAX'], statystyki['Obrona'], id_postaci,))

        wynik2 = kursor.rowcount

        if wynik1 == 1 and wynik2 == 1:
            if wlasne_polaczenie:
                polaczenie.commit()
            return 1
        if wlasne_polaczenie:
            polaczenie.rollback()
        return 0

    except sqlite3.Error as blad:
        if wlasne_polaczenie:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if wlasne_polaczenie:
            polaczenie.close()

def pobierz_gracza(id_postaci, polaczenie=None):

    wlasne_polaczenie = False

    if polaczenie is None:
        polaczenie = polacz_z_baza()
        wlasne_polaczenie = True

    try:
        kursor = polaczenie.cursor()

        kursor.execute('''
            SELECT *
            FROM postacie
            WHERE id_postaci = ?
        ''', (id_postaci,))

        wynik1 = kursor.fetchone()

        if wynik1 is None:
            return None

        kursor.execute('''
            SELECT *
            FROM statystyki
            WHERE id_postaci = ?
        ''', (id_postaci,))

        wynik2 = kursor.fetchone()

        if wynik2 is None:
            return None

        gracz = {
            'ID postaci': wynik1[0],
            'ID konta': wynik1[1],
            'ID serwera': wynik1[2],
            'Nick': wynik1[3],
            'Płeć': wynik1[4],
            'Klasa': wynik1[5],
            'Poziom': wynik1[6],
            'Exp': wynik1[7],
            'Złoto': wynik1[8],
            'Statystyki': {
                'HP': wynik2[2],
                'HP MAX': wynik2[3],
                'Mana': wynik2[4],
                'Mana MAX': wynik2[5],
                'Atak MIN': wynik2[6],
                'Atak MAX': wynik2[7],
                'Kryt szansa': wynik2[8],
                'Kryt mnożnik': wynik2[9],
                'Obrona': wynik2[10],
                'Blok': wynik2[11],
                'Kryt redukcja szansy': wynik2[12],
                'Kryt redukcja obrażeń': wynik2[13]}
        }
        return gracz

    except sqlite3.Error as blad:
        if wlasne_polaczenie:
            polaczenie.rollback()
        print(f'\nBłąd bazy danych: {blad}')
        raise

    finally:
        if wlasne_polaczenie:
            polaczenie.close()