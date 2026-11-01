"""
Item system.

This file contains functions for item quality,
item upgrades, bonuses and changing
the quality of equipment.
"""

import random
import uuid

import ui

eliksiry = [
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

krysztaly_duszy = [
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 1,
                 'Cena': 15,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 6,
                 'Cena': 40,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 12,
                 'Cena': 95,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 18,
                 'Cena': 150,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 24,
                 'Cena': 250,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 32,
                 'Cena': 400,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 40,
                 'Cena': 550,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 48,
                 'Cena': 750,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 60,
                 'Cena': 1100,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 70,
                 'Cena': 1400,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 78,
                 'Cena': 1600,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 85,
                 'Cena': 1800,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 91,
                 'Cena': 2100,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 96,
                 'Cena': 2200,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Kryształ Duszy',
                 'Rodzaj': 'Zmiana jakości EQ',
                 'Poziom': 99,
                 'Cena': 2400,
                 'Ilość': 1
             },
]

zwoje_duszy = [
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 1,
                 'Cena': 20,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 6,
                 'Cena': 55,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 12,
                 'Cena': 100,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 18,
                 'Cena': 200,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 24,
                 'Cena': 350,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 32,
                 'Cena': 500,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 40,
                 'Cena': 750,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 48,
                 'Cena': 950,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 60,
                 'Cena': 1100,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 70,
                 'Cena': 1800,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 78,
                 'Cena': 2100,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 85,
                 'Cena': 2400,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 91,
                 'Cena': 2700,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 96,
                 'Cena': 2900,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Zwój Duszy',
                 'Rodzaj': 'Ulepszanie EQ',
                 'Poziom': 99,
                 'Cena': 3100,
                 'Ilość': 1
             },
]

bron_wojownik = [
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
                 'Nazwa': 'Zardzewiały Miecz',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 17,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 150,
                 'Kryt szansa': 8,
                 'Kryt mnożnik': 0.35,
                 'Cena': 1800,
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
                 'Nazwa': 'Miecz Zdobywcy',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 36,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 650,
                 'Kryt szansa': 10,
                 'Kryt mnożnik': 0.75,
                 'Cena': 17000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Miecz Bastionu',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 42,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 800,
                 'Kryt szansa': 12,
                 'Kryt mnożnik': 0.75,
                 'Cena': 32000,
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
             },
             {
                 'Nazwa': 'Ostrze Krwawego Księżyca',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 75,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 3800,
                 'Kryt szansa': 15,
                 'Kryt mnożnik': 1.5,
                 'Cena': 350000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Ostatnie Żniwo',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 85,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 4800,
                 'Kryt szansa': 20,
                 'Kryt mnożnik': 1.5,
                 'Cena': 700000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Ostrze Wiecznego Blasku',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 90,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 6200,
                 'Kryt szansa': 20,
                 'Kryt mnożnik': 1.8,
                 'Cena': 1000000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Wężowe Ostrze',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 93,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 8000,
                 'Kryt szansa': 25,
                 'Kryt mnożnik': 2,
                 'Cena': 1250000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Ostrze Pradawnego Smoka',
                 'Rodzaj': 'Broń',
                 'Klasa': 'Wojownik',
                 'Poziom': 99,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrażenia': 10000,
                 'Kryt szansa': 30,
                 'Kryt mnożnik': 2,
                 'Cena': 2000000,
                 'Ilość': 1
             }
]

tarcze_wojownik = [
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
                 'Cena': 25,
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
                 'Nazwa': 'Tarcza Poległego',
                 'Rodzaj': 'Tarcza',
                 'Klasa': 'Wojownik',
                 'Poziom': 17,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Blok': 15,
                 'Obrona': 5,
                 'HP': 350,
                 'Cena': 1300,
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
                 'Nazwa': 'Tarcza Zdobywcy',
                 'Rodzaj': 'Tarcza',
                 'Klasa': 'Wojownik',
                 'Poziom': 37,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Blok': 22,
                 'Obrona': 35,
                 'HP': 1250,
                 'Cena': 13500,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Tarcza Bastionu',
                 'Rodzaj': 'Tarcza',
                 'Klasa': 'Wojownik',
                 'Poziom': 44,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Blok': 25,
                 'Obrona': 50,
                 'HP': 1800,
                 'Cena': 26500,
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
             },
{
                 'Nazwa': 'Tarcza Krwawego Księżyca',
                 'Rodzaj': 'Tarcza',
                 'Klasa': 'Wojownik',
                 'Poziom': 77,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Blok': 25,
                 'Obrona': 350,
                 'HP': 5000,
                 'Cena': 290000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Tarcza Mroku',
                 'Rodzaj': 'Tarcza',
                 'Klasa': 'Wojownik',
                 'Poziom': 85,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Blok': 25,
                 'Obrona': 500,
                 'HP': 7000,
                 'Cena': 505000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Tarcza Wiecznego Blasku',
                 'Rodzaj': 'Tarcza',
                 'Klasa': 'Wojownik',
                 'Poziom': 90,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Blok': 25,
                 'Obrona': 750,
                 'HP': 10000,
                 'Cena': 720000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Tarcza z Łusek Bazyliszka',
                 'Rodzaj': 'Tarcza',
                 'Klasa': 'Wojownik',
                 'Poziom': 94,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Blok': 25,
                 'Obrona': 1000,
                 'HP': 15000,
                 'Cena': 1010000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Tarcza Pradawnego Smoka',
                 'Rodzaj': 'Tarcza',
                 'Klasa': 'Wojownik',
                 'Poziom': 99,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Blok': 25,
                 'Obrona': 1500,
                 'HP': 20000,
                 'Cena': 1440000,
                 'Ilość': 1
             }
]

helmy_wojownik = [
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
                 'Nazwa': 'Hełm Poległego',
                 'Rodzaj': 'Hełm',
                 'Klasa': 'Wojownik',
                 'Poziom': 18,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 8,
                 'HP': 400,
                 'Cena': 1100,
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
                 'Nazwa': 'Hełm Zdobywcy',
                 'Rodzaj': 'Hełm',
                 'Klasa': 'Wojownik',
                 'Poziom': 38,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 40,
                 'HP': 1500,
                 'Cena': 10000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Hełm Bastionu',
                 'Rodzaj': 'Hełm',
                 'Klasa': 'Wojownik',
                 'Poziom': 45,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 60,
                 'HP': 2000,
                 'Cena': 19000,
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
             },
             {
                 'Nazwa': 'Hełm Krwawego Księżyca',
                 'Rodzaj': 'Hełm',
                 'Klasa': 'Wojownik',
                 'Poziom': 78,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 400,
                 'HP': 6000,
                 'Cena': 215000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Hełm Mroku',
                 'Rodzaj': 'Hełm',
                 'Klasa': 'Wojownik',
                 'Poziom': 85,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 600,
                 'HP': 8000,
                 'Cena': 335000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Korona Wiecznego Blasku',
                 'Rodzaj': 'Hełm',
                 'Klasa': 'Wojownik',
                 'Poziom': 90,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 750,
                 'HP': 12000,
                 'Cena': 480000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Głowa Bazyliszka',
                 'Rodzaj': 'Hełm',
                 'Klasa': 'Wojownik',
                 'Poziom': 95,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 1000,
                 'HP': 18000,
                 'Cena': 720000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Korona Pradawnego Smoka',
                 'Rodzaj': 'Hełm',
                 'Klasa': 'Wojownik',
                 'Poziom': 99,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 1500,
                 'HP': 22000,
                 'Cena': 960000,
                 'Ilość': 1
             }
]

zbroja_wojownik = [
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
                 'Nazwa': 'Pancerz Poległego',
                 'Rodzaj': 'Zbroja',
                 'Klasa': 'Wojownik',
                 'Poziom': 18,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 10,
                 'HP': 500,
                 'Cena': 1900,
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
                 'Nazwa': 'Zbroja Zdobywcy',
                 'Rodzaj': 'Zbroja',
                 'Klasa': 'Wojownik',
                 'Poziom': 38,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 50,
                 'HP': 2000,
                 'Cena': 18000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Pancerz Bastionu',
                 'Rodzaj': 'Zbroja',
                 'Klasa': 'Wojownik',
                 'Poziom': 45,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 75,
                 'HP': 2500,
                 'Cena': 34000,
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
             },
             {
                 'Nazwa': 'Pancerz Krwawego Księżyca',
                 'Rodzaj': 'Zbroja',
                 'Klasa': 'Wojownik',
                 'Poziom': 78,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 500,
                 'HP': 7500,
                 'Cena': 380000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Pancerz Mroku',
                 'Rodzaj': 'Zbroja',
                 'Klasa': 'Wojownik',
                 'Poziom': 85,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 750,
                 'HP': 10000,
                 'Cena': 595000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Pancerz Wiecznego Blasku',
                 'Rodzaj': 'Zbroja',
                 'Klasa': 'Wojownik',
                 'Poziom': 90,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 1000,
                 'HP': 15000,
                 'Cena': 850000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Pancerz z Łusek Bazyliszka',
                 'Rodzaj': 'Zbroja',
                 'Klasa': 'Wojownik',
                 'Poziom': 95,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 1250,
                 'HP': 20000,
                 'Cena': 1280000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Pancerz Pradawnego Smoka',
                 'Rodzaj': 'Zbroja',
                 'Klasa': 'Wojownik',
                 'Poziom': 99,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 1750,
                 'HP': 25000,
                 'Cena': 1700000,
                 'Ilość': 1
             }
]

buty_wojownik = [
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
                 'Nazwa': 'Trzewiki Poległego',
                 'Rodzaj': 'Buty',
                 'Klasa': 'Wojownik',
                 'Poziom': 18,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 5,
                 'HP': 350,
                 'Cena': 900,
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
                 'Nazwa': 'Trzewiki Zdobywcy',
                 'Rodzaj': 'Buty',
                 'Klasa': 'Wojownik',
                 'Poziom': 38,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 35,
                 'HP': 1250,
                 'Cena': 8400,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Trzewiki Bastionu',
                 'Rodzaj': 'Buty',
                 'Klasa': 'Wojownik',
                 'Poziom': 45,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 50,
                 'HP': 1800,
                 'Cena': 16000,
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
             },
             {
                 'Nazwa': 'Trzewiki Krwawego Księżyca',
                 'Rodzaj': 'Buty',
                 'Klasa': 'Wojownik',
                 'Poziom': 78,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 350,
                 'HP': 5000,
                 'Cena': 180000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Trzewiki Mroku',
                 'Rodzaj': 'Buty',
                 'Klasa': 'Wojownik',
                 'Poziom': 85,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 500,
                 'HP': 7000,
                 'Cena': 280000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Trzewiki Wiecznego Blasku',
                 'Rodzaj': 'Buty',
                 'Klasa': 'Wojownik',
                 'Poziom': 90,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 750,
                 'HP': 10000,
                 'Cena': 400000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Trzewiki z Łusek Bazyliszka',
                 'Rodzaj': 'Buty',
                 'Klasa': 'Wojownik',
                 'Poziom': 95,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 1000,
                 'HP': 15000,
                 'Cena': 600000,
                 'Ilość': 1
             },
             {
                 'Nazwa': 'Trzewiki Pradawnego Smoka',
                 'Rodzaj': 'Buty',
                 'Klasa': 'Wojownik',
                 'Poziom': 99,
                 'Jakość': 50,
                 'Ulepszono': 0,
                 'Obrona': 1500,
                 'HP': 20000,
                 'Cena': 800000,
                 'Ilość': 1
             }
]

pierscienie = [
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
                 'Nazwa': 'Pierścień Poległego',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 18,
                 'Kryt redukcja szansy': 3,
                 'Kryt redukcja obrażeń': 7,
                 'Cena': 900,
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
                 'Nazwa': 'Pierścień Zdobywcy',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 38,
                 'Kryt redukcja szansy': 5,
                 'Kryt redukcja obrażeń': 17,
                 'Cena': 8800,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Pierścień Bastionu',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 45,
                 'Kryt redukcja szansy': 6,
                 'Kryt redukcja obrażeń': 21,
                 'Cena': 17000,
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
             },
{
                 'Nazwa': 'Pierścień Krwawego Księżyca',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 78,
                 'Kryt redukcja szansy': 9,
                 'Kryt redukcja obrażeń': 36,
                 'Cena': 190000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Pierścień Mroku',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 85,
                 'Kryt redukcja szansy': 10,
                 'Kryt redukcja obrażeń': 40,
                 'Cena': 295000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Pierścień Wiecznego Blasku',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 90,
                 'Kryt redukcja szansy': 11,
                 'Kryt redukcja obrażeń': 44,
                 'Cena': 420000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Pierścień Bazyliszka',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 95,
                 'Kryt redukcja szansy': 11,
                 'Kryt redukcja obrażeń': 47,
                 'Cena': 630000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Pierścień Pradawnego Smoka',
                 'Rodzaj': 'Pierścień',
                 'Poziom': 99,
                 'Kryt redukcja szansy': 12,
                 'Kryt redukcja obrażeń': 50,
                 'Cena': 840000,
                 'Ilość': 1
             }
]

naszyjniki = [
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
                 'Nazwa': 'Amulet Poległego',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 18,
                 'Kryt redukcja szansy': 2,
                 'Kryt redukcja obrażeń': 9,
                 'Cena': 900,
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
                 'Nazwa': 'Amulet Zdobywcy',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 38,
                 'Kryt redukcja szansy': 3,
                 'Kryt redukcja obrażeń': 22,
                 'Cena': 8800,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Medalion Bastionu',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 45,
                 'Kryt redukcja szansy': 4,
                 'Kryt redukcja obrażeń': 27,
                 'Cena': 17000,
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
{
                 'Nazwa': 'Amulet Krwawego Księżyca',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 78,
                 'Kryt redukcja szansy': 6,
                 'Kryt redukcja obrażeń': 44,
                 'Cena': 190000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Medalion Mroku',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 85,
                 'Kryt redukcja szansy': 7,
                 'Kryt redukcja obrażeń': 49,
                 'Cena': 295000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Amulet Wiecznego Blasku',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 90,
                 'Kryt redukcja szansy': 8,
                 'Kryt redukcja obrażeń': 54,
                 'Cena': 420000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Naszyjnik z Kła Bazyliszka',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 95,
                 'Kryt redukcja szansy': 9,
                 'Kryt redukcja obrażeń': 57,
                 'Cena': 630000,
                 'Ilość': 1
             },
{
                 'Nazwa': 'Serce Pradawnego Smoka',
                 'Rodzaj': 'Naszyjnik',
                 'Poziom': 99,
                 'Kryt redukcja szansy': 10,
                 'Kryt redukcja obrażeń': 60,
                 'Cena': 840000,
                 'Ilość': 1
             }
]

def nadaj_id(przedmiot):
    przedmiot['ID'] = str(uuid.uuid4())
    return przedmiot

def sprawdz_jakosc(jakosc):
    if jakosc <= 5:
        return 'Zniszczony', -40
    elif jakosc <= 25:
        return 'Uszkodzony', -20
    elif jakosc <= 49:
        return 'Niskiej Jakości', -10
    elif jakosc == 50:
        return 'Zwykły', 0
    elif jakosc <= 74:
        return 'Dobry', 10
    elif jakosc <= 84:
        return 'Jakościowy', 15
    elif jakosc <= 95:
        return '\033[94mUnikalny\033[0m', 25
    elif jakosc <= 99:
        return '\033[95mMajestatyczny\033[0m', 35
    elif jakosc == 100:
        return '\033[93mHeroiczny\033[0m', 50

def losuj_jakosc(przedmiot):
    rodzaj = przedmiot['Rodzaj']
    rodzaje_eq = ['Broń', 'Hełm', 'Zbroja', 'Buty', 'Tarcza']
    if rodzaj not in rodzaje_eq:
        return False, '\nNieprawidłowy rodzaj przedmiotu!'
    kopia = przedmiot.copy()
    jakosc = random.randint(0, 100)
    kopia['Jakość'] = jakosc
    return True, kopia

def sprawdz_ulepszenie(poziom):
    if poziom < 0:
        return None, None
    if poziom > 9:
        return None, None

    if poziom == 0:
        return 0, None
    elif poziom == 1:
        return 5, 100
    elif poziom == 2:
        return 10, 90
    elif poziom == 3:
        return 15, 80
    elif poziom == 4:
        return 20, 70
    elif poziom == 5:
        return 30, 60
    elif poziom == 6:
        return 40, 50
    elif poziom == 7:
        return 50, 25
    elif poziom == 8:
        return 75, 8
    elif poziom == 9:
        return 100, 3


def oblicz_dmg_przedmiotu(przedmiot):
    rodzaj = przedmiot['Rodzaj']
    if rodzaj != 'Broń':
        return False, '\nMusisz wybrać broń!'
    nazwa, bonus = sprawdz_jakosc(przedmiot['Jakość'])
    dmg_jakosci = (przedmiot['Obrażenia'] * bonus) / 100
    dmg_jakosci = int(dmg_jakosci)
    bonus_ulepszenia = oblicz_bonus_ulepszenia(przedmiot)
    dmg_ulepszenia = (przedmiot['Obrażenia'] * bonus_ulepszenia) / 100
    dmg_ulepszenia = int(dmg_ulepszenia)
    laczny_dmg = przedmiot['Obrażenia'] + dmg_jakosci + dmg_ulepszenia
    return True, laczny_dmg

def oblicz_obrone_przedmiotu(przedmiot):
    rodzaje_eq = ['Hełm', 'Zbroja', 'Buty', 'Tarcza']
    rodzaj = przedmiot['Rodzaj']
    if rodzaj not in rodzaje_eq:
        return False, '\nMusisz wybrać hełm, zbroję, buty lub tarczę!'
    nazwa, bonus = sprawdz_jakosc(przedmiot['Jakość'])
    obrona_jakosc = (przedmiot['Obrona'] * bonus) / 100
    obrona_jakosc = int(obrona_jakosc)
    bonus_obrona_ulepszenia = oblicz_bonus_ulepszenia(przedmiot)
    obrona_ulepszenia = (przedmiot['Obrona'] * bonus_obrona_ulepszenia) / 100
    obrona_ulepszenia = int(obrona_ulepszenia)
    laczna_obrona = przedmiot['Obrona'] + obrona_jakosc + obrona_ulepszenia
    return True, laczna_obrona

def ulepsz_przedmiot(poziom):
    bonus, szansa = sprawdz_ulepszenie(poziom)
    los = random.uniform(0, 100)
    if los <= szansa:
        return True, bonus
    return False, None

def oblicz_bonus_ulepszenia(przedmiot):
    poziom = przedmiot['Ulepszono']
    bonus, szansa = sprawdz_ulepszenie(poziom)
    return bonus

def ulepszanie(gracz, przedmiot):
    if przedmiot.get('Ulepszono') is not None:
        if przedmiot['Ulepszono'] >= 9:
            print('\nNie możesz ulepszyć przedmiotu do +10!')
            return False, None
        status, bonus = ulepsz_przedmiot(przedmiot['Ulepszono'] + 1)
        if status:
            unikalnosc, bonus = sprawdz_jakosc(przedmiot['Jakość'])
            print(f'\nPomyślnie ulepszono "[{unikalnosc}] {przedmiot['Nazwa']}" z +{przedmiot['Ulepszono']} do +{przedmiot['Ulepszono'] + 1}!')
            przedmiot['Ulepszono'] += 1
            return True, przedmiot
        else:
            ochrona = False
            for przedmiot1 in gracz['Ekwipunek']:
                if przedmiot1.get('Rodzaj') == 'Ulepszanie EQ':
                    if przedmiot['Poziom'] <= przedmiot1['Poziom']:
                        ochrona = True
                        przedmiot1['Ilość'] -= 1
                        if przedmiot1['Ilość'] == 0:
                            gracz['Ekwipunek'].remove(przedmiot1)
                        break
            if ochrona:
                print(f'\nUlepszenie nie powiodło się, ale zwój ochronił Twój przedmiot!')
                return False, przedmiot
            else:
                unikalnosc, bonus = sprawdz_jakosc(przedmiot['Jakość'])
                print(f'\nPrzedmiot "[{unikalnosc}] {przedmiot['Nazwa']} +{przedmiot['Ulepszono']}" spalił się!')
                gracz['Ekwipunek'].remove(przedmiot)
                return False, None
    print('\nNie możesz ulepszyć tego przedmiotu!')
    return False, None

def pobierz_eq_do_zmiany_jakosci(gracz):
    znalezione = []
    for przedmiot in gracz['Ekwipunek']:
        if przedmiot.get('Jakość') is not None:
            zalozone = False
            for zalozony in gracz['Założone'].values():
                if zalozony is not None and przedmiot['ID'] == zalozony['ID']:
                    zalozone = True
                    break
            if zalozone:
                continue
            znalezione.append(przedmiot)
    return znalezione

def pokaz_eq_do_zmiany_jakosci(gracz):
    eq = pobierz_eq_do_zmiany_jakosci(gracz)
    if not eq:
        print('\nBrak przedmiotów do zmiany jakości!')
        return eq
    ui.wyswietl_tytul('ZMIANA JAKOŚCI PRZEDMIOTU')
    for indeks, przedmiot in enumerate(eq, start=1):
        unikalnosc, bonus = sprawdz_jakosc(przedmiot['Jakość'])
        print(f'{indeks}) "[{unikalnosc}] {przedmiot['Nazwa']} +{przedmiot['Ulepszono']}"')
    print('\n0) - Powrót')
    return eq

def wybierz_eq_do_zmiany_jakosci(gracz):
    eq = pokaz_eq_do_zmiany_jakosci(gracz)
    if not eq:
        return
    print('\nPodaj numer przedmiotu: ')
    numer_przedmiotu = ui.pobierz_wybor(0, len(eq))
    if numer_przedmiotu < 0 or numer_przedmiotu > len(eq):
        print('\nWybierz poprawny numer przedmiotu!')
        return
    if numer_przedmiotu == 0:
        return
    wybrany_przedmiot = eq[numer_przedmiotu - 1]
    status, przedmiot = zmiana_jakosci(gracz, wybrany_przedmiot)

def losuj_nowa_jakosc_przedmiotu(przedmiot):
    nowa_jakosc = random.randint(0, 100)
    przedmiot['Jakość'] = nowa_jakosc
    return przedmiot

def zmiana_jakosci(gracz, przedmiot):
    if przedmiot.get('Jakość') is not None:
        krysztal = False
        for przedmiot1 in gracz['Ekwipunek']:
            if przedmiot1.get('Rodzaj') == 'Zmiana jakości EQ':
                if przedmiot['Poziom'] <= przedmiot1['Poziom']:
                    krysztal = True
                    przedmiot1['Ilość'] -= 1
                    if przedmiot1['Ilość'] == 0:
                        gracz['Ekwipunek'].remove(przedmiot1)
                    break
        if not krysztal:
            print(f'\nBrak kryształu!!')
            return False, przedmiot
        unikalnosc, bonus = sprawdz_jakosc(przedmiot['Jakość'])
        przed_zmiana = przedmiot.copy()
        po_zmianie = losuj_nowa_jakosc_przedmiotu(przedmiot)
        print(f'\nPomyślnie zmieniono jakość "[{unikalnosc}] {przedmiot['Nazwa']} +{przedmiot['Ulepszono']}" z {przed_zmiana['Jakość']} na {po_zmianie['Jakość']}!')
        return True, przedmiot
    print('\nNie możesz zmienić jakości tego przedmiotu!')
    return False, None

def pobierz_eq_do_ulepszenia(gracz):
    znalezione = []
    for przedmiot in gracz['Ekwipunek']:
        if przedmiot.get('Ulepszono') is not None:
            if przedmiot['Ulepszono'] < 9:
                zalozone = False
                for zalozony in gracz['Założone'].values():
                    if zalozony is not None and przedmiot['ID'] == zalozony['ID']:
                        zalozone = True
                        break
                if zalozone:
                    continue
                znalezione.append(przedmiot)
    return znalezione

def pokaz_eq_do_ulepszenia(gracz):
    eq = pobierz_eq_do_ulepszenia(gracz)
    if not eq:
        print('\nBrak przedmiotów do ulepszenia!')
        return eq
    ui.wyswietl_tytul('ULEPSZANIE PRZEDMIOTU')
    for indeks, przedmiot in enumerate(eq, start=1):
        unikalnosc, bonus = sprawdz_jakosc(przedmiot['Jakość'])
        print(f'{indeks}) "[{unikalnosc}] {przedmiot['Nazwa']} +{przedmiot['Ulepszono']}"')
    print('\n0) - Powrót')
    return eq

def wybierz_eq_do_ulepszenia(gracz):
    eq = pokaz_eq_do_ulepszenia(gracz)
    if not eq:
        return
    print('\nPodaj numer przedmiotu: ')
    numer_przedmiotu = ui.pobierz_wybor(0, len(eq))
    if numer_przedmiotu < 0 or numer_przedmiotu > len(eq):
        print('\nWybierz poprawny numer przedmiotu!')
        return
    if numer_przedmiotu == 0:
        return
    wybrany_przedmiot = eq[numer_przedmiotu - 1]
    status, przedmiot = ulepszanie(gracz, wybrany_przedmiot)