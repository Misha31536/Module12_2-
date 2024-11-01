from unittest import TestCase

import Module_12_2Git as R

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_variants = []


    def setUp(self):
        self.first = Runner("Усэйн", 10)
        self.second = Runner("Андрей", 9)
        self.third = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_variants):
            print(i, elem)

    def test(self):
        tournament1 = R.Tournament(90, self.first, self.third)
        results1 = tournament1.start()
        TournamentTest.all_variants.append(results1)
        self.assertTrue(results1[2] == 'Ник')
    def test1(self):
        tournament2 = R.Tournament(90, self.second, self.third)
        results2 = tournament2.start()
        TournamentTest.all_variants.append(results2)
        self.assertTrue(results2[2] == 'Ник')
    def test2(self):
        tournament3 = R.Tournament(90, self.first, self.second, self.third)
        results3 = tournament3.start()
        print(results3)
        TournamentTest.all_variants.append(results3)
        self.assertTrue(results3[3] == 'Ник')


