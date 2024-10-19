import Test
import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.a1 = Test.Runner('Усэйн', 10)
        self.a2 = Test.Runner('Андрей', 9)
        self.a3 = Test.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(test_key)
            for key, value in test_value.items():
                print(f'{key}: {value.name}')

    def test_run(self):
        run1 = Test.Tournament(90, self.a1, self.a3)
        win = run1.start()

        self.assertTrue(win[list(win.keys())[-1]] == "Ник")
        self.all_results['1) Результат'] = win

    def test_run2(self):
        run2 = Test.Tournament(90, self.a2, self.a3)
        win = run2.start()

        self.assertTrue(win[list(win.keys())[-1]] == 'Ник')
        self.all_results['\n2) Результат'] = win

    def test_run3(self):
        run3 = Test.Tournament(90, self.a1, self.a2, self.a3)
        win = run3.start()

        self.assertTrue(win[list(win.keys())[-1]] == 'Ник')
        self.all_results['\n3) Результат'] = win


if __name__ == '__main__':
    unittest.main()
