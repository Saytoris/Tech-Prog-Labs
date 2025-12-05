# test_app.py
import unittest
import xmlrunner # Імпортуємо бібліотеку для генерації XML-звітів
from app import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Набір тестів для перевірки калькулятора."""

    def setUp(self):
        """Цей метод запускається перед кожним тестом."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Перевірка операції додавання."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
   
    @unittest.expectedFailure
    def test_add_unsuported_format(self):
             self.assertEqual(self.calc.add("a",-1), -1)
             self.assertEqual(self.calc.add("a",-1), "a")

    def test_subtract(self):
        """Перевірка операції віднімання."""
        self.assertEqual(self.calc.subtract(10, 5), 5)

if __name__ == '__main__':
    # Налаштовуємо запуск тестів так, щоб результати зберігалися у папку 'test-reports'
    # Це необхідно для того, щоб Jenkins міг зчитати результати.
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)