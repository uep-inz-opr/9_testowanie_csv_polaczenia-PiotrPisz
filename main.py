from calendar import c
import csv
from subprocess import call
import unittest
from unittest import TestCase
from venv import create

class SprawdzDwoniacegoTest(TestCase):
    def test_czy_najwiecej_minut():
        mp = Polaczenia("phoneCalls.csv")
        wynik = mp.pobierz_najczesciej_dzwoniacego()
        self.assertEqual((226,5), wynik)

class Polaczenia:
    def __init__(self, name):
        self.name = name
        self.data_dict = self.create_dict()
    
    def create_dict(self):
        calls_sum_dict = dict()
        with open(self.name, 'r') as fin:
            reader = csv.reader(fin, delimiter=",")
            headers = next(reader)
            for row in reader:
                client = int(row[0])
                if client not in calls_sum_dict:
                    calls_sum_dict[client] = 0
                value = 1
                calls_sum_dict[client] += value
        return calls_sum_dict

    def pobierz_najczesciej_dzwoniacego(self):
        return  max(self.data_dict.items(), key= lambda x: x[1])



if __name__ == '__main__':
    print(Polaczenia(input()).pobierz_najczesciej_dzwoniacego())