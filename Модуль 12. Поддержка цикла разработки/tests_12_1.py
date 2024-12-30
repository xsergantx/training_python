"""
Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

Пункты задачи:
Скачайте исходный код для тестов.
Создайте класс RunnerTest и соответствующие описанию методы.
Запустите RunnerTest и убедитесь в правильности результатов.

"""

import Test_1
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Test_1.Runner('Кот')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        run = Test_1.Runner('Собака')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        walker2 = Test_1.Runner('Крокодил')
        run2 = Test_1.Runner('Ёж')
        for i in range(10):
            walker2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walker2.distance)
