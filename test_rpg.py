"""
Game tests.

This file contains basic tests for
the main game systems, including combat,
equipment, shops, skills, potions,
item drops and saving progress.
"""

import copy
import os
import tempfile
from unittest.mock import patch

import player
import shop
import equipment
import skills
import potions
import combat
import drop
import save


def test(nazwa, funkcja):
    try:
        funkcja()
        print(f"[OK] {nazwa}")
        return True
    except Exception as blad:
        print(f"[BLAD] {nazwa}")
        print(f"       {type(blad).__name__}: {blad}")
        return False


def nowy_gracz():
    gracz = player.nowa_gra("Tester")[0]
    gracz["Poziom"] = 99
    gracz["Złoto"] = 10_000_000
    gracz["Statystyki"]["HP MAX"] = 10000
    gracz["Statystyki"]["HP"] = 10000
    gracz["Statystyki"]["Mana MAX"] = 10000
    gracz["Statystyki"]["Mana"] = 10000
    return gracz


def test_sklepu():
    gracz = nowy_gracz()
    bron = shop.sklep_bronie_wojownik[0]
    zloto = gracz["Złoto"]

    komunikat, przedmiot, cena = shop.kup_przedmiot(
        gracz, shop.sklep_bronie_wojownik, bron["Nazwa"], 1
    )

    assert przedmiot is not None, komunikat
    assert len(gracz["Ekwipunek"]) == 1
    assert gracz["Złoto"] == zloto - cena
    assert gracz["Ekwipunek"][0].get("ID")

    status, wynik = equipment.zaloz_przedmiot(gracz, 1)
    assert status, wynik
    assert gracz["Założone"]["Broń"] is not None

    zloto_przed = gracz["Złoto"]
    komunikat = shop.sprzedaj_przedmiot(
        gracz, gracz["Ekwipunek"], 1, 1
    )

    assert gracz["Złoto"] == zloto_przed, (
        "Udalo sie sprzedac zalozony przedmiot!"
    )
    assert len(gracz["Ekwipunek"]) == 1

    # Kupujemy drugi, niezalozony egzemplarz.
    komunikat, przedmiot, cena = shop.kup_przedmiot(
        gracz, shop.sklep_bronie_wojownik, bron["Nazwa"], 1
    )
    assert przedmiot is not None, komunikat
    assert len(gracz["Ekwipunek"]) == 2

    id_przedmiotow = [p["ID"] for p in gracz["Ekwipunek"]]
    assert len(set(id_przedmiotow)) == 2, "Powtorzone ID!"

    zloto_przed = gracz["Złoto"]
    komunikat = shop.sprzedaj_przedmiot(
        gracz, gracz["Ekwipunek"], 2, 1
    )
    assert len(gracz["Ekwipunek"]) == 1, komunikat
    assert gracz["Złoto"] > zloto_przed


def test_umiejetnosci():
    gracz = nowy_gracz()

    zloto_przed = gracz["Złoto"]
    komunikat = skills.trener_naucz_umiejetnosci(gracz, 1)

    assert len(gracz["Wyuczono"]) == 1, komunikat
    assert gracz["Złoto"] < zloto_przed

    komunikat = skills.trener_naucz_umiejetnosci(gracz, 1)
    assert len(gracz["Wyuczono"]) == 2, (
        "Nie nauczono drugiej umiejetnosci"
    )

    gracz["Umiejętności"]["Slot 1"] = gracz["Wyuczono"][0]
    dostepne = skills.pokaz_wybrane_umiejetnosci_walka(gracz)

    assert len(dostepne) == 1
    assert dostepne[0]["Nazwa"] == "Mocne Uderzenie"


def test_eliksirow():
    gracz = nowy_gracz()

    eliksir = copy.deepcopy(shop.sklep_eliksiry[0])
    eliksir["Ilość"] = 2
    gracz["Ekwipunek"].append(eliksir)

    gracz["Statystyki"]["HP"] = 100
    hp_przed = gracz["Statystyki"]["HP"]

    komunikat = potions.wypij_eliksir(gracz, 1)

    assert gracz["Statystyki"]["HP"] > hp_przed, komunikat
    assert gracz["Ekwipunek"][0]["Ilość"] == 1

    gracz["Statystyki"]["HP"] = gracz["Statystyki"]["HP MAX"]
    komunikat = potions.wypij_eliksir(gracz, 1)

    assert gracz["Ekwipunek"][0]["Ilość"] == 1
    assert gracz["Statystyki"]["HP"] == gracz["Statystyki"]["HP MAX"]


def test_walki():
    obrazenia, hp, kryt, blok = combat.wykonaj_atak(
        100, 100, 0, 1.25, 20, 500, 0
    )

    assert obrazenia == 80
    assert hp == 420
    assert not blok

    obrazenia, hp, kryt, blok = combat.wykonaj_atak(
        100, 100, 0, 1.25, 20, 500, 100
    )

    assert obrazenia == 0
    assert hp == 500
    assert blok


def test_skilla_w_walce():
    gracz = nowy_gracz()
    przeciwnik = {
        "Statystyki": {"Obrona": 0}
    }

    skill = skills.umiejetnosci[0]
    mana_przed = gracz["Statystyki"]["Mana"]

    status, obrazenia, hp, kryt, blok = combat.wykonaj_skill(
        gracz, przeciwnik, 1000, skill, 0
    )

    assert status
    assert obrazenia > 0
    assert hp < 1000
    assert gracz["Statystyki"]["Mana"] == (
        mana_przed - skill["Mana"]
    )

    gracz["Statystyki"]["Mana"] = 0

    status, obrazenia, hp, kryt, blok = combat.wykonaj_skill(
        gracz, przeciwnik, 1000, skill, 0
    )

    assert not status
    assert hp == 1000


def test_dropu():
    gracz = nowy_gracz()

    mob = {
        "Drop": [
            {
                "Nazwa": "Testowy material",
                "Rodzaj": "Material",
                "Szansa": 100,
                "Ilość MIN": 2,
                "Ilość MAX": 2,
                "Cena": 10,
            }
        ]
    }

    drop.wykonaj_drop(gracz, mob)
    assert len(gracz["Ekwipunek"]) == 1
    assert gracz["Ekwipunek"][0]["Ilość"] == 2

    drop.wykonaj_drop(gracz, mob)
    assert len(gracz["Ekwipunek"]) == 1
    assert gracz["Ekwipunek"][0]["Ilość"] == 4


def test_zapisu():
    gracz = nowy_gracz()

    bron = shop.sklep_bronie_wojownik[0]
    shop.kup_przedmiot(
        gracz, shop.sklep_bronie_wojownik, bron["Nazwa"], 1
    )

    status, wynik = equipment.zaloz_przedmiot(gracz, 1)
    assert status, wynik

    skills.trener_naucz_umiejetnosci(gracz, 1)
    gracz["Umiejętności"]["Slot 1"] = gracz["Wyuczono"][0]

    lista = [gracz]
    stary_folder = os.getcwd()

    try:
        with tempfile.TemporaryDirectory() as folder:
            try:
                os.chdir(folder)

                assert save.zapisz_gre(lista)
                wczytane = save.wczytaj_gre()

                assert wczytane is not None
                assert wczytane == lista, (
                    "Dane po wczytaniu roznia sie od zapisu!"
                )

                odczytany = wczytane[0]
                assert odczytany["Założone"]["Broń"] is not None
                assert len(odczytany["Ekwipunek"]) == 1
                assert len(odczytany["Wyuczono"]) == 1
                assert odczytany["Umiejętności"]["Slot 1"] is not None

            finally:
                os.chdir(stary_folder)

    except Exception:
        os.chdir(stary_folder)
        raise

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("         DEEW RPG - TESTY AUTOMATYCZNE")
    print("=" * 50)

    wyniki = [
        test("Sklep, zakup, sprzedaz i EQ", test_sklepu),
        test("Nauka umiejetnosci", test_umiejetnosci),
        test("Eliksiry HP", test_eliksirow),
        test("Obrazenia i blok", test_walki),
        test("Skill i zuzycie many", test_skilla_w_walce),
        test("Drop i laczenie materialow", test_dropu),
        test("Zapis i odczyt gry", test_zapisu),
    ]

    print("\n" + "=" * 50)
    print(f"WYNIK: {sum(wyniki)} / {len(wyniki)} testow OK")
    print("=" * 50)

    if all(wyniki):
        print("PODSTAWOWE TESTY ZALICZONE!")
    else:
        print("SA BLEDY DO SPRAWDZENIA.")
