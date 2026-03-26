#   TRAVELLING SALESMAN PROBLEM WITH GENETIC ALGORITHM
#   TO-DO:
#   1. Random pontok generálása, ezek lesznek a városok
#       1.1 Megnézni, hogy egy random pont körül van-e X értékű közelségben másik pont (ne legyenek túl közel a pontok egymáshoz)
#   2. Kezdeti út generálása a random pontok között -> random pontok sorrendje, ez lesz mutálva

import random

class individual():
    def __init__(self)->individual:
        