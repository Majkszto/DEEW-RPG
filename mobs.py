"""
Enemies and locations.

This file contains enemies, bosses,
their stats, item drops
and game locations.
"""

import items
import ui

moby = [
{
        'Nazwa': 'Szczur',
        'Poziom': 1,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Stary Zagajnik',
        'Exp': 10,
        'Złoto': 1,
        'Statystyki': {
            'HP': 10,
            'HP MAX': 10,
            'Mana': 10,
            'Mana MAX': 10,
            'Atak MIN': 1,
            'Atak MAX': 3,
            'Kryt szansa': 2,
            'Kryt mnożnik': 1.1,
            'Obrona': 1,
            'Blok': 2},

        'Drop': [
{
            'Nazwa': 'Szczurzy ogon',
            'Rodzaj': 'Materiał',
            'Cena': 1,
            'Ilość': 1,
            'Szansa': 30
            },
{
            **items.zwoje_duszy[0],
            'Szansa': 10
            },
{
            **items.krysztaly_duszy[0],
            'Szansa': 10
            }
        ]
    },
{
        'Nazwa': 'Gigantyczny pająk',
        'Poziom': 3,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Stary Zagajnik',
        'Exp': 200,
        'Złoto': 5,
        'Statystyki': {
            'HP': 35,
            'HP MAX': 35,
            'Mana': 10,
            'Mana MAX': 10,
            'Atak MIN': 4,
            'Atak MAX': 10,
            'Kryt szansa': 2,
            'Kryt mnożnik': 1.15,
            'Obrona': 1,
            'Blok': 3},

        'Drop': [
{
            'Nazwa': 'Pajęcza nić',
            'Rodzaj': 'Materiał',
            'Cena': 3,
            'Ilość': 1,
            'Szansa': 30
            },
{
            'Nazwa': 'Woreczek jadu',
            'Rodzaj': 'Materiał',
            'Cena': 15,
            'Ilość': 1,
            'Szansa': 3
            },
        ]
    },
{
        'Nazwa': 'Dziki pies',
        'Poziom': 6,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Stary Zagajnik',
        'Exp': 5000,
        'Złoto': 10,
        'Statystyki': {
            'HP': 150,
            'HP MAX': 150,
            'Mana': 10,
            'Mana MAX': 10,
            'Atak MIN': 12,
            'Atak MAX': 20,
            'Kryt szansa': 5,
            'Kryt mnożnik': 1.25,
            'Obrona': 4,
            'Blok': 3},

        'Drop': [
{
            'Nazwa': 'Futro psa',
            'Rodzaj': 'Materiał',
            'Cena': 5,
            'Ilość': 1,
            'Szansa': 30
            },
{
            'Nazwa': 'Pazur psa',
            'Rodzaj': 'Materiał',
            'Cena': 10,
            'Ilość': 1,
            'Szansa': 10
            },
{
            **items.zwoje_duszy[1],
            'Szansa': 5
            },
{
            **items.krysztaly_duszy[1],
            'Szansa': 5
            }
        ]
    },
{
        'Nazwa': 'Młody wilk',
        'Poziom': 9,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Wilcza Knieja',
        'Exp': 25000,
        'Złoto': 15,
        'Statystyki': {
            'HP': 600,
            'HP MAX': 600,
            'Mana': 30,
            'Mana MAX': 30,
            'Atak MIN': 30,
            'Atak MAX': 50,
            'Kryt szansa': 7,
            'Kryt mnożnik': 1.35,
            'Obrona': 8,
            'Blok': 4},

        'Drop': [
{
            'Nazwa': 'Futro wilka',
            'Rodzaj': 'Materiał',
            'Cena': 12,
            'Ilość': 1,
            'Szansa': 15
            },
{
            'Nazwa': 'Kieł wilka',
            'Rodzaj': 'Materiał',
            'Cena': 13,
            'Ilość': 1,
            'Szansa': 10
            },
        ]
    },
{
        'Nazwa': 'Dziki wilk',
        'Poziom': 10,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Wilcza Knieja',
        'Exp': 38000,
        'Złoto': 20,
        'Statystyki': {
            'HP': 1000,
            'HP MAX': 1000,
            'Mana': 30,
            'Mana MAX': 30,
            'Atak MIN': 60,
            'Atak MAX': 100,
            'Kryt szansa': 8,
            'Kryt mnożnik': 1.4,
            'Obrona': 15,
            'Blok': 5},

        'Drop': [
{
            'Nazwa': 'Futro wilka',
            'Rodzaj': 'Materiał',
            'Cena': 12,
            'Ilość': 1,
            'Szansa': 20
            },
{
            'Nazwa': 'Kieł wilka',
            'Rodzaj': 'Materiał',
            'Cena': 13,
            'Ilość': 1,
            'Szansa': 15
            },
        ]
    },
{
        'Nazwa': 'Wściekły wilk',
        'Poziom': 12,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Wilcza Knieja',
        'Exp': 78000,
        'Złoto': 30,
        'Statystyki': {
            'HP': 1500,
            'HP MAX': 1500,
            'Mana': 30,
            'Mana MAX': 30,
            'Atak MIN': 90,
            'Atak MAX': 130,
            'Kryt szansa': 9,
            'Kryt mnożnik': 1.45,
            'Obrona': 22,
            'Blok': 6},

        'Drop': [
{
            'Nazwa': 'Futro wilka',
            'Rodzaj': 'Materiał',
            'Cena': 12,
            'Ilość': 1,
            'Szansa': 30
            },
{
            'Nazwa': 'Kieł wilka',
            'Rodzaj': 'Materiał',
            'Cena': 13,
            'Ilość': 1,
            'Szansa': 20
            },
{
            **items.zwoje_duszy[2],
            'Szansa': 2
            },
{
            **items.krysztaly_duszy[2],
            'Szansa': 2
            }
        ]
    },
{
        'Nazwa': 'Zgniły żołnierz',
        'Poziom': 15,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Dolina Poległych',
        'Exp': 175000,
        'Złoto': 50,
        'Statystyki': {
            'HP': 2200,
            'HP MAX': 2200,
            'Mana': 30,
            'Mana MAX': 30,
            'Atak MIN': 125,
            'Atak MAX': 175,
            'Kryt szansa': 9,
            'Kryt mnożnik': 1.5,
            'Obrona': 32,
            'Blok': 8},

        'Drop': [
{
            'Nazwa': 'Zgniłe mięso',
            'Rodzaj': 'Materiał',
            'Cena': 10,
            'Ilość': 1,
            'Szansa': 50
            }
        ]
    },
{
        'Nazwa': 'Zardzewiały rycerz',
        'Poziom': 17,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Dolina Poległych',
        'Exp': 280000,
        'Złoto': 80,
        'Statystyki': {
            'HP': 3000,
            'HP MAX': 3000,
            'Mana': 30,
            'Mana MAX': 30,
            'Atak MIN': 150,
            'Atak MAX': 220,
            'Kryt szansa': 10,
            'Kryt mnożnik': 1.5,
            'Obrona': 38,
            'Blok': 9},

        'Drop': [
{
            'Nazwa': 'Fragment zbroi',
            'Rodzaj': 'Materiał',
            'Cena': 25,
            'Ilość': 1,
            'Szansa': 20
            },
{
            **items.bron_wojownik[4],
            'Szansa': 4
            },
        ]
    },
{
        'Nazwa': 'Poległy wojownik',
        'Poziom': 18,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Dolina Poległych',
        'Exp': 350000,
        'Złoto': 100,
        'Statystyki': {
            'HP': 4000,
            'HP MAX': 4000,
            'Mana': 40,
            'Mana MAX': 40,
            'Atak MIN': 220,
            'Atak MAX': 280,
            'Kryt szansa': 11,
            'Kryt mnożnik': 1.55,
            'Obrona': 48,
            'Blok': 10},

        'Drop': [
{
            **items.tarcze_wojownik[2],
            'Szansa': 4
            },
{
            **items.helmy_wojownik[2],
            'Szansa': 4
            },
{
            **items.zbroja_wojownik[2],
            'Szansa': 4
            },
{
            **items.buty_wojownik[2],
            'Szansa': 4
            },
{
            **items.pierscienie[2],
            'Szansa': 4
            },
{
            **items.naszyjniki[2],
            'Szansa': 4
            },
{
            **items.zwoje_duszy[3],
            'Szansa': 1
            },
{
            **items.krysztaly_duszy[3],
            'Szansa': 1
            }
        ]
    },
{
        'Nazwa': 'Strażnik obozu',
        'Poziom': 20,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Obóz Rozbójników',
        'Exp': 525000,
        'Złoto': 125,
        'Statystyki': {
            'HP': 4800,
            'HP MAX': 4800,
            'Mana': 40,
            'Mana MAX': 40,
            'Atak MIN': 250,
            'Atak MAX': 320,
            'Kryt szansa': 12,
            'Kryt mnożnik': 1.55,
            'Obrona': 60,
            'Blok': 12},

        'Drop': [
{
            'Nazwa': 'Złote monety',
            'Rodzaj': 'Inne',
            'Cena': 10,
            'Ilość MIN': 2,
            'Ilość MAX': 5,
            'Szansa': 25
            },
        ]
    },
{
        'Nazwa': 'Rozbójnik',
        'Poziom': 22,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Obóz Rozbójników',
        'Exp': 780000,
        'Złoto': 160,
        'Statystyki': {
            'HP': 5600,
            'HP MAX': 5600,
            'Mana': 40,
            'Mana MAX': 40,
            'Atak MIN': 310,
            'Atak MAX': 390,
            'Kryt szansa': 14,
            'Kryt mnożnik': 1.6,
            'Obrona': 80,
            'Blok': 9},

        'Drop': [
{
            'Nazwa': 'Złote monety',
            'Rodzaj': 'Inne',
            'Cena': 10,
            'Ilość MIN': 3,
            'Ilość MAX': 8,
            'Szansa': 50
            },
{
            'Nazwa': 'Skradziona sakiewka',
            'Rodzaj': 'Inne',
            'Cena': 400,
            'Ilość': 1,
            'Szansa': 5
            },
        ]
    },
{
        'Nazwa': 'Herszt rabusiów',
        'Poziom': 24,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Boss',
        'Mapa': 'Obóz Rozbójników',
        'Exp': 1200000,
        'Złoto': 200,
        'Statystyki': {
            'HP': 7000,
            'HP MAX': 7000,
            'Mana': 40,
            'Mana MAX': 40,
            'Atak MIN': 400,
            'Atak MAX': 500,
            'Kryt szansa': 15,
            'Kryt mnożnik': 1.6,
            'Obrona': 100,
            'Blok': 12},

        'Drop': [
{
            'Nazwa': 'Złote monety',
            'Rodzaj': 'Inne',
            'Cena': 10,
            'Ilość MIN': 5,
            'Ilość MAX': 10,
            'Szansa': 50
            },
{
            'Nazwa': 'Fragment mapy skarbów',
            'Rodzaj': 'Inne',
            'Cena': 200,
            'Ilość': 1,
            'Szansa': 15
            },
{
            'Nazwa': 'Klucz do skrzyni',
            'Rodzaj': 'Inne',
            'Cena': 350,
            'Ilość': 1,
            'Szansa': 5
            },
{
            **items.zwoje_duszy[4],
            'Szansa': 2
            },
{
            **items.krysztaly_duszy[4],
            'Szansa': 2
            }
        ]
    },
{
        'Nazwa': 'Olbrzymi goryl',
        'Poziom': 27,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Gęsta Dżungla',
        'Exp': 1600000,
        'Złoto': 250,
        'Statystyki': {
            'HP': 8500,
            'HP MAX': 8500,
            'Mana': 45,
            'Mana MAX': 45,
            'Atak MIN': 600,
            'Atak MAX': 800,
            'Kryt szansa': 10,
            'Kryt mnożnik': 1.6,
            'Obrona': 150,
            'Blok': 14},

        'Drop': [
{
            'Nazwa': 'Czaszka goryla',
            'Rodzaj': 'Materiał',
            'Cena': 250,
            'Ilość': 1,
            'Szansa': 10
            },
{
            'Nazwa': 'Wielki kieł',
            'Rodzaj': 'Materiał',
            'Cena': 350,
            'Ilość': 1,
            'Szansa': 8
            },
{
            'Nazwa': 'Banan',
            'Rodzaj': 'Materiał',
            'Cena': 600,
            'Ilość': 1,
            'Szansa': 3
            },
        ]
    },
{
        'Nazwa': 'Dziki łowca',
        'Poziom': 30,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Gęsta Dżungla',
        'Exp': 2700000,
        'Złoto': 400,
        'Statystyki': {
            'HP': 9500,
            'HP MAX': 9500,
            'Mana': 45,
            'Mana MAX': 45,
            'Atak MIN': 750,
            'Atak MAX': 960,
            'Kryt szansa': 18,
            'Kryt mnożnik': 1.7,
            'Obrona': 125,
            'Blok': 10},
        'Drop': [
{
            'Nazwa': 'Dziwna maska',
            'Rodzaj': 'Materiał',
            'Cena': 800,
            'Ilość': 1,
            'Szansa': 7
            },
{
            'Nazwa': 'Ludzka kość',
            'Rodzaj': 'Materiał',
            'Cena': 1200,
            'Ilość': 1,
            'Szansa': 5
            },
{
            'Nazwa': 'Futro z jaguara',
            'Rodzaj': 'Materiał',
            'Cena': 750,
            'Ilość': 1,
            'Szansa': 10
            },
        ]
    },
{
        'Nazwa': 'Plemienny wojownik',
        'Poziom': 32,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Gęsta Dżungla',
        'Exp': 3000000,
        'Złoto': 500,
        'Statystyki': {
            'HP': 12000,
            'HP MAX': 12000,
            'Mana': 45,
            'Mana MAX': 45,
            'Atak MIN': 800,
            'Atak MAX': 1000,
            'Kryt szansa': 15,
            'Kryt mnożnik': 1.7,
            'Obrona': 180,
            'Blok': 15},

        'Drop': [
{
            'Nazwa': 'Dziwna maska',
            'Rodzaj': 'Materiał',
            'Cena': 800,
            'Ilość': 1,
            'Szansa': 10
            },
{
            'Nazwa': 'Ludzka kość',
            'Rodzaj': 'Materiał',
            'Cena': 1200,
            'Ilość': 1,
            'Szansa': 5
            },
{
            'Nazwa': 'Magiczny totem',
            'Rodzaj': 'Materiał',
            'Cena': 3000,
            'Ilość': 1,
            'Szansa': 3
            },
{
            **items.zwoje_duszy[5],
            'Szansa': 2
            },
{
            **items.krysztaly_duszy[5],
            'Szansa': 2
            }
        ]
    },
{
        'Nazwa': 'Ork berserker',
        'Poziom': 36,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Dolina Orków',
        'Exp': 4600000,
        'Złoto': 750,
        'Statystyki': {
            'HP': 15000,
            'HP MAX': 15000,
            'Mana': 50,
            'Mana MAX': 50,
            'Atak MIN': 1200,
            'Atak MAX': 1600,
            'Kryt szansa': 18,
            'Kryt mnożnik': 1.9,
            'Obrona': 150,
            'Blok': 5},

        'Drop': [
{
            'Nazwa': 'Złamany kieł',
            'Rodzaj': 'Materiał',
            'Cena': 250,
            'Ilość': 1,
            'Szansa': 20
            },
{
            'Nazwa': 'Serce berserkera',
            'Rodzaj': 'Materiał',
            'Cena': 3000,
            'Ilość': 1,
            'Szansa': 1
            },
        ]
    },
{
        'Nazwa': 'Ork wojownik',
        'Poziom': 38,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Dolina Orków',
        'Exp': 5700000,
        'Złoto': 900,
        'Statystyki': {
            'HP': 18000,
            'HP MAX': 18000,
            'Mana': 50,
            'Mana MAX': 50,
            'Atak MIN': 1300,
            'Atak MAX': 1650,
            'Kryt szansa': 13,
            'Kryt mnożnik': 1.7,
            'Obrona': 250,
            'Blok': 18},

        'Drop': [
{
            **items.bron_wojownik[8],
            'Szansa': 2
            },
{
            **items.tarcze_wojownik[5],
            'Szansa': 2
            },
{
            **items.helmy_wojownik[5],
            'Szansa': 2
            },
{
            **items.zbroja_wojownik[5],
            'Szansa': 2
            },
{
            **items.buty_wojownik[5],
            'Szansa': 2
            },
        ]
    },
{
        'Nazwa': 'Wódz orków',
        'Poziom': 40,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Boss',
        'Mapa': 'Dolina Orków',
        'Exp': 8500000,
        'Złoto': 1400,
        'Statystyki': {
            'HP': 30000,
            'HP MAX': 30000,
            'Mana': 60,
            'Mana MAX': 60,
            'Atak MIN': 1500,
            'Atak MAX': 2000,
            'Kryt szansa': 16,
            'Kryt mnożnik': 1.9,
            'Obrona': 300,
            'Blok': 15},

        'Drop': [
{
            'Nazwa': 'Pieczęć wodza',
            'Rodzaj': 'Materiał',
            'Cena': 3000,
            'Ilość': 1,
            'Szansa': 5
            },
{
            'Nazwa': 'Krew wodza',
            'Rodzaj': 'Materiał',
            'Cena': 4000,
            'Ilość': 1,
            'Szansa': 2
            },
{
            'Nazwa': 'Magiczny totem',
            'Rodzaj': 'Materiał',
            'Cena': 3000,
            'Ilość': 1,
            'Szansa': 3
            },
{
            **items.zwoje_duszy[6],
            'Szansa': 1
            },
{
            **items.krysztaly_duszy[6],
            'Szansa': 1
            },
{
            **items.pierscienie[5],
            'Szansa': 2
            },
{
            **items.naszyjniki[5],
            'Szansa': 2
            }
        ]
    },
{
        'Nazwa': 'Lodowy wilk',
        'Poziom': 42,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Północ',
        'Exp': 8000000,
        'Złoto': 1200,
        'Statystyki': {
            'HP': 22000,
            'HP MAX': 22000,
            'Mana': 60,
            'Mana MAX': 60,
            'Atak MIN': 2200,
            'Atak MAX': 2900,
            'Kryt szansa': 22,
            'Kryt mnożnik': 1.9,
            'Obrona': 200,
            'Blok': 12},

        'Drop': [
{
            'Nazwa': 'Lodowy odłamek',
            'Rodzaj': 'Materiał',
            'Cena': 800,
            'Ilość': 1,
            'Szansa': 50
            },
{
            'Nazwa': 'Kieł lodowego wilka',
            'Rodzaj': 'Materiał',
            'Cena': 1000,
            'Ilość': 1,
            'Szansa': 10
            },
        ]
    },
{
        'Nazwa': 'Zamarźnięty wojownik',
        'Poziom': 45,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Północ',
        'Exp': 10000000,
        'Złoto': 1800,
        'Statystyki': {
            'HP': 40000,
            'HP MAX': 40000,
            'Mana': 100,
            'Mana MAX': 100,
            'Atak MIN': 1200,
            'Atak MAX': 1750,
            'Kryt szansa': 18,
            'Kryt mnożnik': 1.8,
            'Obrona': 400,
            'Blok': 22},


        'Drop': [
{
            'Nazwa': 'Lodowy odłamek',
            'Rodzaj': 'Materiał',
            'Cena': 800,
            'Ilość': 1,
            'Szansa': 30
            },
{
            **items.bron_wojownik[9],
            'Szansa': 1.5
            },
{
            **items.tarcze_wojownik[6],
            'Szansa': 1.5
            },
{
            **items.helmy_wojownik[6],
            'Szansa': 1.5
            },
{
            **items.zbroja_wojownik[6],
            'Szansa': 1.5
            },
{
            **items.buty_wojownik[6],
            'Szansa': 1.5
            },
        ]
    },
{
        'Nazwa': 'Lodowy golem',
        'Poziom': 48,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Północ',
        'Exp': 12000000,
        'Złoto': 2400,
        'Statystyki': {
            'HP': 50000,
            'HP MAX': 50000,
            'Mana': 100,
            'Mana MAX': 100,
            'Atak MIN': 1300,
            'Atak MAX': 1700,
            'Kryt szansa': 15,
            'Kryt mnożnik': 1.6,
            'Obrona': 400,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Serce lodowego golema',
            'Rodzaj': 'Materiał',
            'Cena': 4000,
            'Ilość': 1,
            'Szansa': 3
            },
{
            'Nazwa': 'Lodowy odłamek',
            'Rodzaj': 'Materiał',
            'Cena': 800,
            'Ilość': 1,
            'Szansa': 40
            },
{
            **items.zwoje_duszy[7],
            'Szansa': 1
            },
{
            **items.krysztaly_duszy[7],
            'Szansa': 1
            },
{
            **items.pierscienie[6],
            'Szansa': 2.5
            },
{
            **items.naszyjniki[6],
            'Szansa': 2.5
            }
        ]
    },
{
        'Nazwa': 'Prastary ent',
        'Poziom': 53,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Tajemniczy Las',
        'Exp': 17000000,
        'Złoto': 3500,
        'Statystyki': {
            'HP': 60000,
            'HP MAX': 60000,
            'Mana': 100,
            'Mana MAX': 100,
            'Atak MIN': 2000,
            'Atak MAX': 3000,
            'Kryt szansa': 20,
            'Kryt mnożnik': 1.8,
            'Obrona': 400,
            'Blok': 25},
        'Drop': [
{
            'Nazwa': 'Prastare nasiono',
            'Rodzaj': 'Materiał',
            'Cena': 20000,
            'Ilość': 1,
            'Szansa': 0.1
            },
{
            'Nazwa': 'Dusza lasu',
            'Rodzaj': 'Materiał',
            'Cena': 5000,
            'Ilość': 1,
            'Szansa': 5
            },
        ]
    },
{
        'Nazwa': 'Leśna wiedźma',
        'Poziom': 57,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Tajemniczy Las',
        'Exp': 21000000,
        'Złoto': 5000,
        'Statystyki': {
            'HP': 30000,
            'HP MAX': 30000,
            'Mana': 1000,
            'Mana MAX': 1000,
            'Atak MIN': 5000,
            'Atak MAX': 7000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.5,
            'Obrona': 0,
            'Blok': 0},

        'Drop': [
{
            'Nazwa': 'Zatrute jabłko',
            'Rodzaj': 'Materiał',
            'Cena': 1500,
            'Ilość': 1,
            'Szansa': 20
            },
{
            'Nazwa': 'Mandragora',
            'Rodzaj': 'Materiał',
            'Cena': 20000,
            'Ilość': 1,
            'Szansa': 4
            },
{
            **items.eliksiry[6],
            'Szansa': 50
            }
        ]
    },
{
        'Nazwa': 'Krwiożerczy muchomor',
        'Poziom': 60,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Boss',
        'Mapa': 'Tajemniczy Las',
        'Exp': 28000000,
        'Złoto': 10000,
        'Statystyki': {
            'HP': 90000,
            'HP MAX': 90000,
            'Mana': 500,
            'Mana MAX': 500,
            'Atak MIN': 2500,
            'Atak MAX': 4000,
            'Kryt szansa': 18,
            'Kryt mnożnik': 2.0,
            'Obrona': 700,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Zaczarowany grzyb',
            'Rodzaj': 'Materiał',
            'Cena': 10000,
            'Ilość': 1,
            'Szansa': 7
            },
{
            'Nazwa': 'Tajemniczy mech',
            'Rodzaj': 'Materiał',
            'Cena': 30000,
            'Ilość': 1,
            'Szansa': 1
            },
{
            'Nazwa': 'Krwawa narośl',
            'Rodzaj': 'Materiał',
            'Cena': 50000,
            'Ilość': 1,
            'Szansa': 0.1
            },
{
            **items.zwoje_duszy[8],
            'Szansa': 1.5
            },
{
            **items.krysztaly_duszy[8],
            'Szansa': 1.5
            },
        ]
    },
{
        'Nazwa': 'Stary troll',
        'Poziom': 62,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Skalisko',
        'Exp': 28000000,
        'Złoto': 7000,
        'Statystyki': {
            'HP': 95000,
            'HP MAX': 95000,
            'Mana': 200,
            'Mana MAX': 200,
            'Atak MIN': 2500,
            'Atak MAX': 4000,
            'Kryt szansa': 18,
            'Kryt mnożnik': 2.0,
            'Obrona': 800,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Szara perła',
            'Rodzaj': 'Materiał',
            'Cena': 2000000,
            'Ilość': 1,
            'Szansa': 0.01
            },
        ]
    },
{
        'Nazwa': 'Troll jaskiniowy',
        'Poziom': 64,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Skalisko',
        'Exp': 30000000,
        'Złoto': 9000,
        'Statystyki': {
            'HP': 100000,
            'HP MAX': 100000,
            'Mana': 230,
            'Mana MAX': 230,
            'Atak MIN': 3000,
            'Atak MAX': 5000,
            'Kryt szansa': 20,
            'Kryt mnożnik': 2.1,
            'Obrona': 1000,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Biała perła',
            'Rodzaj': 'Materiał',
            'Cena': 2000000,
            'Ilość': 1,
            'Szansa': 0.01
            },
        ]
    },
{
        'Nazwa': 'Monstrualny troll',
        'Poziom': 66,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Skalisko',
        'Exp': 31000000,
        'Złoto': 11000,
        'Statystyki': {
            'HP': 110000,
            'HP MAX': 110000,
            'Mana': 280,
            'Mana MAX': 280,
            'Atak MIN': 4000,
            'Atak MAX': 5400,
            'Kryt szansa': 22,
            'Kryt mnożnik': 2.2,
            'Obrona': 1200,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Czarna perła',
            'Rodzaj': 'Materiał',
            'Cena': 2000000,
            'Ilość': 1,
            'Szansa': 0.01
            },
        ]
    },
{
        'Nazwa': 'Jadowity skorpion',
        'Poziom': 70,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Pustynia Magdbi',
        'Exp': 34000000,
        'Złoto': 15000,
        'Statystyki': {
            'HP': 120000,
            'HP MAX': 120000,
            'Mana': 660,
            'Mana MAX': 660,
            'Atak MIN': 5000,
            'Atak MAX': 6000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.2,
            'Obrona': 1000,
            'Blok': 16},

        'Drop': [
{
            'Nazwa': 'Kolec jadowy',
            'Rodzaj': 'Materiał',
            'Cena': 40000,
            'Ilość': 1,
            'Szansa': 5
            },
{
            'Nazwa': 'Pancerz skorpiona',
            'Rodzaj': 'Materiał',
            'Cena': 20000,
            'Ilość': 1,
            'Szansa': 10
            },
{
            'Nazwa': 'Pustynny pył',
            'Rodzaj': 'Materiał',
            'Cena': 5000,
            'Ilość': 1,
            'Szansa': 20
            },
{
            **items.zwoje_duszy[9],
            'Szansa': 1.5
            },
{
            **items.krysztaly_duszy[9],
            'Szansa': 1.5
            },
        ]
    },
{
        'Nazwa': 'Pustynny golem',
        'Poziom': 72,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Pustynia Magdbi',
        'Exp': 36000000,
        'Złoto': 18000,
        'Statystyki': {
            'HP': 150000,
            'HP MAX': 150000,
            'Mana': 800,
            'Mana MAX': 800,
            'Atak MIN': 5000,
            'Atak MAX': 7000,
            'Kryt szansa': 20,
            'Kryt mnożnik': 2.0,
            'Obrona': 1500,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Serce pustynnego golema',
            'Rodzaj': 'Materiał',
            'Cena': 20000,
            'Ilość': 1,
            'Szansa': 3
            },
{
            'Nazwa': 'Pustynny pył',
            'Rodzaj': 'Materiał',
            'Cena': 5000,
            'Ilość': 1,
            'Szansa': 40
            },
        ]
    },
{
        'Nazwa': 'Pustynny łupieżca',
        'Poziom': 73,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Pustynia Magdbi',
        'Exp': 37000000,
        'Złoto': 22000,
        'Statystyki': {
            'HP': 100000,
            'HP MAX': 100000,
            'Mana': 2000,
            'Mana MAX': 2000,
            'Atak MIN': 9000,
            'Atak MAX': 12000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.5,
            'Obrona': 900,
            'Blok': 16},

        'Drop': [
{
            'Nazwa': 'Magiczna lampa',
            'Rodzaj': 'Materiał',
            'Cena': 100000,
            'Ilość': 1,
            'Szansa': 1
            },
{
            'Nazwa': 'Pustynny pył',
            'Rodzaj': 'Materiał',
            'Cena': 5000,
            'Ilość': 1,
            'Szansa': 30
            },
{
            'Nazwa': 'Złote sztabki',
            'Rodzaj': 'Inne',
            'Cena': 500,
            'Ilość MIN': 3,
            'Ilość MAX': 8,
            'Szansa': 15
            },
        ]
    },
{
        'Nazwa': 'Krwiopijca',
        'Poziom': 76,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Dolina Krwawego Księżyca',
        'Exp': 42000000,
        'Złoto': 27000,
        'Statystyki': {
            'HP': 125000,
            'HP MAX': 125000,
            'Mana': 2200,
            'Mana MAX': 2200,
            'Atak MIN': 7000,
            'Atak MAX': 10000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.5,
            'Obrona': 1300,
            'Blok': 20},

        'Drop': [
{
            'Nazwa': 'Pradawna krew',
            'Rodzaj': 'Materiał',
            'Cena': 20000,
            'Ilość': 1,
            'Szansa': 3
            },
{
            'Nazwa': 'Złote sztabki',
            'Rodzaj': 'Inne',
            'Cena': 500,
            'Ilość MIN': 6,
            'Ilość MAX': 12,
            'Szansa': 25
            },
        ]
    },
{
        'Nazwa': 'Wilkołak',
        'Poziom': 77,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Dolina Krwawego Księżyca',
        'Exp': 44000000,
        'Złoto': 30000,
        'Statystyki': {
            'HP': 150000,
            'HP MAX': 150000,
            'Mana': 2000,
            'Mana MAX': 2000,
            'Atak MIN': 6000,
            'Atak MAX': 8000,
            'Kryt szansa': 20,
            'Kryt mnożnik': 2.1,
            'Obrona': 2000,
            'Blok': 20},

        'Drop': [
{
            'Nazwa': 'Futro wilkołaka',
            'Rodzaj': 'Materiał',
            'Cena': 5000,
            'Ilość': 1,
            'Szansa': 50
            },
{
            'Nazwa': 'Kieł wilkołaka',
            'Rodzaj': 'Materiał',
            'Cena': 100000,
            'Ilość': 1,
            'Szansa': 1
            },
{
            'Nazwa': 'Złote sztabki',
            'Rodzaj': 'Inne',
            'Cena': 500,
            'Ilość MIN': 8,
            'Ilość MAX': 15,
            'Szansa': 50
            },
        ]
    },
{
        'Nazwa': 'Władca Krwawego Księżyca',
        'Poziom': 78,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Boss',
        'Mapa': 'Dolina Krwawego Księżyca',
        'Exp': 50000000,
        'Złoto': 42000,
        'Statystyki': {
            'HP': 160000,
            'HP MAX': 160000,
            'Mana': 4000,
            'Mana MAX': 4000,
            'Atak MIN': 9000,
            'Atak MAX': 11000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.6,
            'Obrona': 2000,
            'Blok': 20},

        'Drop': [
{
            'Nazwa': 'Pradawna krew',
            'Rodzaj': 'Materiał',
            'Cena': 20000,
            'Ilość': 1,
            'Szansa': 33
            },
{
            'Nazwa': 'Serce wampira',
            'Rodzaj': 'Materiał',
            'Cena': 35000,
            'Ilość': 1,
            'Szansa': 3
            },
{
            'Nazwa': 'Złote sztabki',
            'Rodzaj': 'Inne',
            'Cena': 500,
            'Ilość MIN': 10,
            'Ilość MAX': 20,
            'Szansa': 100
            },
{
            **items.bron_wojownik[14],
            'Szansa': 1
            },
{
            **items.tarcze_wojownik[9],
            'Szansa': 1
            },
{
            **items.helmy_wojownik[9],
            'Szansa': 1
            },
{
            **items.zbroja_wojownik[9],
            'Szansa': 1
            },
{
            **items.buty_wojownik[9],
            'Szansa': 1
            },
{
            **items.zwoje_duszy[10],
            'Szansa': 1
            },
{
            **items.krysztaly_duszy[10],
            'Szansa': 1
            },
{
            **items.pierscienie[9],
            'Szansa': 1
            },
{
            **items.naszyjniki[9],
            'Szansa': 1
            }
        ]
    },
{
        'Nazwa': 'Potępiona dusza',
        'Poziom': 82,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Cmentarzysko',
        'Exp': 50000000,
        'Złoto': 40000,
        'Statystyki': {
            'HP': 180000,
            'HP MAX': 180000,
            'Mana': 5000,
            'Mana MAX': 5000,
            'Atak MIN': 8000,
            'Atak MAX': 10000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.0,
            'Obrona': 3000,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Zagubiona dusza',
            'Rodzaj': 'Materiał',
            'Cena': 10000,
            'Ilość': 1,
            'Szansa': 50
            },
{
            'Nazwa': 'Esencja mroku',
            'Rodzaj': 'Materiał',
            'Cena': 50000,
            'Ilość': 1,
            'Szansa': 0.2
            },
        ]
    },
{
        'Nazwa': 'Nieumarły wojownik',
        'Poziom': 83,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Cmentarzysko',
        'Exp': 51000000,
        'Złoto': 50000,
        'Statystyki': {
            'HP': 220000,
            'HP MAX': 220000,
            'Mana': 3000,
            'Mana MAX': 3000,
            'Atak MIN': 8500,
            'Atak MAX': 10500,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.0,
            'Obrona': 4000,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Zagubiona dusza',
            'Rodzaj': 'Materiał',
            'Cena': 10000,
            'Ilość': 1,
            'Szansa': 25
            },
{
            'Nazwa': 'Esencja mroku',
            'Rodzaj': 'Materiał',
            'Cena': 50000,
            'Ilość': 1,
            'Szansa': 0.1
            },
{
            'Nazwa': 'Gnijąca kość',
            'Rodzaj': 'Materiał',
            'Cena': 7500,
            'Ilość': 1,
            'Szansa': 50
            },
        ]
    },
{
        'Nazwa': 'Śmierć',
        'Poziom': 85,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Boss',
        'Mapa': 'Cmentarzysko',
        'Exp': 55000000,
        'Złoto': 80000,
        'Statystyki': {
            'HP': 250000,
            'HP MAX': 250000,
            'Mana': 10000,
            'Mana MAX': 10000,
            'Atak MIN': 11000,
            'Atak MAX': 14000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.5,
            'Obrona': 5000,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Zagubiona dusza',
            'Rodzaj': 'Materiał',
            'Cena': 10000,
            'Ilość MIN': 3,
            'Ilość MAX': 10,
            'Szansa': 50
            },
{
            'Nazwa': 'Esencja mroku',
            'Rodzaj': 'Materiał',
            'Cena': 50000,
            'Ilość': 1,
            'Szansa': 5
            },
{
            'Nazwa': 'Serce ciemności',
            'Rodzaj': 'Materiał',
            'Cena': 80000,
            'Ilość': 1,
            'Szansa': 3
            },
{
            **items.bron_wojownik[15],
            'Szansa': 1
            },
{
            **items.tarcze_wojownik[10],
            'Szansa': 1
            },
{
            **items.helmy_wojownik[10],
            'Szansa': 1
            },
{
            **items.zbroja_wojownik[10],
            'Szansa': 1
            },
{
            **items.buty_wojownik[10],
            'Szansa': 1
            },
{
            **items.zwoje_duszy[11],
            'Szansa': 1
            },
{
            **items.krysztaly_duszy[11],
            'Szansa': 1
            },
{
            **items.pierscienie[10],
            'Szansa': 1
            },
{
            **items.naszyjniki[10],
            'Szansa': 1
            }
        ]
    },
{
        'Nazwa': 'Boski strażnik',
        'Poziom': 89,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Niebiańskie Bramy',
        'Exp': 55000000,
        'Złoto': 90000,
        'Statystyki': {
            'HP': 300000,
            'HP MAX': 300000,
            'Mana': 5000,
            'Mana MAX': 5000,
            'Atak MIN': 11500,
            'Atak MAX': 14500,
            'Kryt szansa': 20,
            'Kryt mnożnik': 2.25,
            'Obrona': 5200,
            'Blok': 20},

        'Drop': [
{
            'Nazwa': 'Odłamek aureoli',
            'Rodzaj': 'Materiał',
            'Cena': 400000,
            'Ilość': 1,
            'Szansa': 0.1
            },
{
            'Nazwa': 'Esencja światłości',
            'Rodzaj': 'Materiał',
            'Cena': 80000,
            'Ilość': 1,
            'Szansa': 0.5
            },
{
            'Nazwa': 'Święty pył',
            'Rodzaj': 'Materiał',
            'Cena': 28000,
            'Ilość': 1,
            'Szansa': 10
            },
        ]
    },
{
        'Nazwa': 'Niebiański wojownik',
        'Poziom': 90,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Niebiańskie Bramy',
        'Exp': 56000000,
        'Złoto': 100000,
        'Statystyki': {
            'HP': 280000,
            'HP MAX': 280000,
            'Mana': 4000,
            'Mana MAX': 4000,
            'Atak MIN': 12000,
            'Atak MAX': 15000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.2,
            'Obrona': 6500,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Odłamek aureoli',
            'Rodzaj': 'Materiał',
            'Cena': 400000,
            'Ilość': 1,
            'Szansa': 0.2
            },
{
            'Nazwa': 'Esencja światłości',
            'Rodzaj': 'Materiał',
            'Cena': 80000,
            'Ilość': 1,
            'Szansa': 1
            },
{
            'Nazwa': 'Święty pył',
            'Rodzaj': 'Materiał',
            'Cena': 28000,
            'Ilość': 1,
            'Szansa': 20
            },
        ]
    },
{
        'Nazwa': 'Archanioł',
        'Poziom': 91,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Boss',
        'Mapa': 'Niebiańskie Bramy',
        'Exp': 61000000,
        'Złoto': 125000,
        'Statystyki': {
            'HP': 320000,
            'HP MAX': 320000,
            'Mana': 7000,
            'Mana MAX': 7000,
            'Atak MIN': 14000,
            'Atak MAX': 17000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.2,
            'Obrona': 7000,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Odłamek aureoli',
            'Rodzaj': 'Materiał',
            'Cena': 400000,
            'Ilość': 1,
            'Szansa': 1
            },
{
            'Nazwa': 'Esencja światłości',
            'Rodzaj': 'Materiał',
            'Cena': 80000,
            'Ilość': 1,
            'Szansa': 10
            },
{
            'Nazwa': 'Święty pył',
            'Rodzaj': 'Materiał',
            'Cena': 28000,
            'Ilość': 1,
            'Szansa': 30
            },
{
            'Nazwa': 'Pióro archanioła',
            'Rodzaj': 'Materiał',
            'Cena': 25000,
            'Ilość': 1,
            'Szansa': 50
            },
{
            **items.bron_wojownik[16],
            'Szansa': 0.5
            },
{
            **items.tarcze_wojownik[11],
            'Szansa': 0.5
            },
{
            **items.helmy_wojownik[11],
            'Szansa': 0.5
            },
{
            **items.zbroja_wojownik[11],
            'Szansa': 0.5
            },
{
            **items.buty_wojownik[11],
            'Szansa': 0.5
            },
{
            **items.zwoje_duszy[12],
            'Szansa': 1
            },
{
            **items.krysztaly_duszy[12],
            'Szansa': 1
            },
{
            **items.pierscienie[11],
            'Szansa': 0.5
            },
{
            **items.naszyjniki[11],
            'Szansa': 0.5
            }
        ]
    },
{
        'Nazwa': 'Bagienny jaszczur',
        'Poziom': 92,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Mgliste Bagna',
        'Exp': 60000000,
        'Złoto': 110000,
        'Statystyki': {
            'HP': 360000,
            'HP MAX': 360000,
            'Mana': 6000,
            'Mana MAX': 6000,
            'Atak MIN': 14000,
            'Atak MAX': 17500,
            'Kryt szansa': 25,
            'Kryt mnożnik': 3.0,
            'Obrona': 8000,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Łuska jaszczura',
            'Rodzaj': 'Materiał',
            'Cena': 22000,
            'Ilość': 1,
            'Szansa': 50
            },
{
            'Nazwa': 'Ogon jaszczura',
            'Rodzaj': 'Materiał',
            'Cena': 75000,
            'Ilość': 1,
            'Szansa': 10
            },
        ]
    },
{
        'Nazwa': 'Jadowity pełzacz',
        'Poziom': 93,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Mgliste Bagna',
        'Exp': 62000000,
        'Złoto': 120000,
        'Statystyki': {
            'HP': 400000,
            'HP MAX': 400000,
            'Mana': 5000,
            'Mana MAX': 5000,
            'Atak MIN': 16000,
            'Atak MAX': 20000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 2.5,
            'Obrona': 7000,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Łuska pełzacza',
            'Rodzaj': 'Materiał',
            'Cena': 25000,
            'Ilość': 1,
            'Szansa': 50
            },
{
            'Nazwa': 'Kieł pełzacza',
            'Rodzaj': 'Materiał',
            'Cena': 80000,
            'Ilość': 1,
            'Szansa': 10
            },
        ]
    },
{
        'Nazwa': 'Bazyliszek',
        'Poziom': 95,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Boss',
        'Mapa': 'Mgliste Bagna',
        'Exp': 66000000,
        'Złoto': 150000,
        'Statystyki': {
            'HP': 420000,
            'HP MAX': 420000,
            'Mana': 12000,
            'Mana MAX': 12000,
            'Atak MIN': 20000,
            'Atak MAX': 30000,
            'Kryt szansa': 30,
            'Kryt mnożnik': 3.0,
            'Obrona': 0,
            'Blok': 0},


        'Drop': [
{
            'Nazwa': 'Łuska bazyliszka',
            'Rodzaj': 'Materiał',
            'Cena': 30000,
            'Ilość': 1,
            'Szansa': 50
            },
{
            'Nazwa': 'Serce bazyliszka',
            'Rodzaj': 'Materiał',
            'Cena': 1000000,
            'Ilość': 1,
            'Szansa': 10
            },
{
            **items.bron_wojownik[17],
            'Szansa': 0.5
            },
{
            **items.tarcze_wojownik[12],
            'Szansa': 0.5
            },
{
            **items.helmy_wojownik[12],
            'Szansa': 0.5
            },
{
            **items.zbroja_wojownik[12],
            'Szansa': 0.5
            },
{
            **items.buty_wojownik[12],
            'Szansa': 0.5
            },
{
            **items.zwoje_duszy[13],
            'Szansa': 1
            },
{
            **items.krysztaly_duszy[13],
            'Szansa': 1
            },
{
            **items.pierscienie[12],
            'Szansa': 0.5
            },
{
            **items.naszyjniki[12],
            'Szansa': 0.5
            }
        ]
    },
{
        'Nazwa': 'Młody smok',
        'Poziom': 96,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Smocze Wzgórze',
        'Exp': 66000000,
        'Złoto': 160000,
        'Statystyki': {
            'HP': 600000,
            'HP MAX': 600000,
            'Mana': 10000,
            'Mana MAX': 10000,
            'Atak MIN': 18000,
            'Atak MAX': 22000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 3.0,
            'Obrona': 10000,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Łuska smoka',
            'Rodzaj': 'Materiał',
            'Cena': 50000,
            'Ilość': 1,
            'Szansa': 20
            },
{
            'Nazwa': 'Smoczy kieł',
            'Rodzaj': 'Materiał',
            'Cena': 200000,
            'Ilość': 1,
            'Szansa': 3
            },
        ]
    },
{
        'Nazwa': 'Dorodny smok',
        'Poziom': 97,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Zwykły',
        'Mapa': 'Smocze Wzgórze',
        'Exp': 68000000,
        'Złoto': 180000,
        'Statystyki': {
            'HP': 700000,
            'HP MAX': 700000,
            'Mana': 10000,
            'Mana MAX': 10000,
            'Atak MIN': 18000,
            'Atak MAX': 22000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 3.0,
            'Obrona': 12000,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Łuska smoka',
            'Rodzaj': 'Materiał',
            'Cena': 50000,
            'Ilość': 1,
            'Szansa': 30
            },
{
            'Nazwa': 'Smocze jajo',
            'Rodzaj': 'Inne',
            'Cena': 10000000,
            'Ilość': 1,
            'Szansa': 0.01
            },
        ]
    },
{
        'Nazwa': 'Pradawny smok',
        'Poziom': 99,
        'Klasa': 'Wojownik',
        'Rodzaj': 'Boss',
        'Mapa': 'Smocze Wzgórze',
        'Exp': 70000000,
        'Złoto': 250000,
        'Statystyki': {
            'HP': 1000000,
            'HP MAX': 1000000,
            'Mana': 20000,
            'Mana MAX': 20000,
            'Atak MIN': 16000,
            'Atak MAX': 22000,
            'Kryt szansa': 25,
            'Kryt mnożnik': 3.0,
            'Obrona': 14000,
            'Blok': 25},

        'Drop': [
{
            'Nazwa': 'Łuska smoka',
            'Rodzaj': 'Materiał',
            'Cena': 50000,
            'Ilość': 1,
            'Szansa': 50
            },
{
            'Nazwa': 'Smocze jajo',
            'Rodzaj': 'Inne',
            'Cena': 10000000,
            'Ilość': 1,
            'Szansa': 0.2
            },
{
            **items.bron_wojownik[18],
            'Szansa': 0.1
            },
{
            **items.tarcze_wojownik[13],
            'Szansa': 0.1
            },
{
            **items.helmy_wojownik[13],
            'Szansa': 0.1
            },
{
            **items.zbroja_wojownik[13],
            'Szansa': 0.1
            },
{
            **items.buty_wojownik[13],
            'Szansa': 0.1
            },
{
            **items.zwoje_duszy[14],
            'Szansa': 1
            },
{
            **items.krysztaly_duszy[14],
            'Szansa': 1
            },
{
            **items.pierscienie[13],
            'Szansa': 0.1
            },
{
            **items.naszyjniki[13],
            'Szansa': 0.1
            }
        ]
    }
        ]

mapy = [
{'Mapa': 'Stary Zagajnik',
     'Poziom': 1},
{'Mapa': 'Wilcza Knieja',
     'Poziom': 5},
{'Mapa': 'Dolina Poległych',
     'Poziom': 9},
{'Mapa': 'Obóz Rozbójników',
     'Poziom': 15},
{'Mapa': 'Gęsta Dżungla',
     'Poziom': 18},
{'Mapa': 'Dolina Orków',
     'Poziom': 22},
{'Mapa': 'Północ',
     'Poziom': 30},
{'Mapa': 'Tajemniczy Las',
     'Poziom': 40},
{'Mapa': 'Skalisko',
     'Poziom': 45},
{'Mapa': 'Pustynia Magdbi',
     'Poziom': 55},
{'Mapa': 'Dolina Krwawego Księżyca',
     'Poziom': 60},
{'Mapa': 'Cmentarzysko',
     'Poziom': 70},
{'Mapa': 'Niebiańskie Bramy',
     'Poziom': 75},
{'Mapa': 'Mgliste Bagna',
     'Poziom': 80},
{'Mapa': 'Smocze Wzgórze',
     'Poziom': 85},
]

def pobierz_moba(lista, mob1):
    for mob in lista:
        if mob['Nazwa'].lower() == mob1.lower():
            return mob
    return None

def pokaz_moba(lista):
    for klucz, wartosc in lista.items():
        if klucz == 'Nazwa':
            ui.wyswietl_tytul(wartosc)
        elif klucz == 'Poziom':
            print(f'{klucz}: {wartosc}')
        elif klucz == 'Klasa':
            print(f'{klucz}: {wartosc}')
        elif klucz == 'Rodzaj':
            print(f'{klucz}: {wartosc}')
        elif klucz == 'Mapa':
            print(f'{klucz}: {wartosc}')
        elif klucz == 'Exp':
            print(f'{klucz}: {wartosc}')
        elif klucz == 'Złoto':
            print(f'{klucz}: {wartosc}')
            print('━' * 75)
        elif klucz == 'Statystyki':
            ui.wyswietl_tytul('STATYSTYKI')
            for statystyka, ile in lista['Statystyki'].items():
                if statystyka == 'HP':
                    print(f'{statystyka}: {ile} / {lista['Statystyki']['HP MAX']}')
                elif statystyka == 'Mana':
                    print(f'{statystyka}: {ile} / {lista['Statystyki']['Mana MAX']}')
                elif statystyka == 'Atak MIN':
                    print(f'Atak: {lista['Statystyki']['Atak MIN']} - {lista['Statystyki']['Atak MAX']}')
                elif statystyka == 'Obrona':
                    print(f'{statystyka}: {ile}')
                elif statystyka == 'Kryt szansa':
                    print(f'Szansa na cios krytyczny: {ile}%')
                elif statystyka == 'Kryt mnożnik':
                    print(f'Cios krytyczny: {ile * 100:.0f}%')
                elif statystyka == 'Blok':
                    print(f'Blok: {ile}%')
            print('━' * 75)

def pokaz_liste_mobow(lista):
    ui.wyswietl_tytul('MOBY')
    for indeks, mob in enumerate(lista, start=1):
        if mob['Rodzaj'] == 'Boss':
            print(f'{indeks}. {mob['Nazwa']} [BOSS]')
        else:
            print(f'{indeks}. {mob['Nazwa']}')
    print('\n0. Powrót do menu')
    print('━' * 75)

def pokaz_mapy(lista):
    ui.wyswietl_tytul('MAPY')
    for indeks, mapa in enumerate(lista, start=1):
        print(f'{indeks}. {mapa['Mapa']} [Poziom: {mapa['Poziom']}]')
    print('\n0. Powrót do menu')
    print('━' * 75)

def wybierz_mape(lista, gracz):
    pokaz_mapy(lista)
    wybor = ui.pobierz_wybor(0, len(lista))
    if wybor == 0:
        return 0
    mapa = lista[wybor - 1]
    if mapa['Poziom'] <= gracz['Poziom']:
        return mapa
    print('\nZbyt niski poziom gracza!')
    return None


def moby_na_mapie(lista, mapa):
    dostepne_moby = []
    for mob in lista:
        if mob['Mapa'].lower() == mapa['Mapa'].lower():
            dostepne_moby.append(mob)
    return dostepne_moby

