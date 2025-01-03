# Часть 2. Пропуск тестов.
import unittest
from module_12_0_2 import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Mike')
        for walk in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = Runner('Bob')
        for run in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = Runner('Maks')
        runner_4 = Runner('Billy')
        for run in range(10):
            runner_3.run()
        for walk in range(10):
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # словарь в который будут сохраняться результаты всех тестов
    def setUp(self):
        self.run_1 = Runner('Усейн', 10)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):  # метод, где выводятся all_results по очереди в столбец
        for result in cls.all_results.values():
            res = {}
            for place, runner in result.items():
                res[place] = runner.name
                print(res)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        self.tournament_1 = Tournament(90, self.run_1, self.run_3)
        self.all_results = self.tournament_1.start()  # словарь записываем результат функции
        last_name = self.all_results[max(self.all_results.keys())].name  # имя с максимальным местом
        self.assertTrue(last_name, self.run_3)  # сравнение
        TournamentTest.all_results[1] = self.all_results  # словарь

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        self.tournament_2 = Tournament(90, self.run_2, self.run_3)
        self.all_results = self.tournament_2.start()  # словарь записываем результат функции
        last_name = self.all_results[max(self.all_results.keys())].name  # имя с максимальным местом
        self.assertTrue(last_name, self.run_3.name)  # сравнение
        TournamentTest.all_results[2] = self.all_results  # словарь

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        self.tournament_3 = Tournament(90, self.run_1, self.run_2, self.run_3)
        self.all_results = self.tournament_3.start()  # словарь записываем результат функции
        last_name = self.all_results[max(self.all_results.keys())].name  # имя с максимальным местом
        self.assertTrue(last_name, self.run_3)  # сравнение
        TournamentTest.all_results[3] = self.all_results  # словарь




if __name__ == "__main__":
    unittest.main()