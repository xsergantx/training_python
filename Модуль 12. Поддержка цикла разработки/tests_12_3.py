"""
Цель: понять на практике как объединять тесты при помощи TestSuite. Научиться пропускать тесты при помощи встроенных в unittest декораторов.

Задача "Заморозка кейсов":
Подготовка:
В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.
Часть 1. TestSuit.
Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
Создайте объект класса TextTestRunner, с аргументом verbosity=2.
Часть 2. Пропуск тестов.
Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение 'Тесты в этом кейсе заморожены'.
Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
"""
import unittest
import inspect
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        peshehod = Runner('Пешеход')
        for i in range(10):
            peshehod.walk()
        self.assertEqual(peshehod.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        begun = Runner('Бегун')
        for i in range(10):
            begun.run()
        self.assertEqual(begun.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        peshehod = Runner('Пешеход')
        begun = Runner('Бегун')
        for i in range(10):
            peshehod.walk()
            begun.run()
        self.assertNotEqual(peshehod.distance, begun.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({k: str(v) for k, v in cls.all_results[test].items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_nik(self):
        tour = Tournament(90, self.usain, self.nik)
        results = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_nik(self):
        tour = Tournament(90, self.andrey, self.nik)
        results = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_nik(self):
        tour = Tournament(90, self.usain, self.andrey, self.nik)
        results = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)


if __name__ == '__main__':
    unittest.main()