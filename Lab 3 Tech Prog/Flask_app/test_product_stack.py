import unittest
from product_stack import Product, ProductStack

class TestProductStack(unittest.TestCase):

    def setUp(self):
        """
        Метод налаштування (fixture). 
        Викликається АВТОМАТИЧНО перед запуском *кожного* тестового методу.
        Створює "чистий" екземпляр ProductStack та два продукти для тестів.
        """
        self.stack = ProductStack()
        self.product1 = Product("Хліб", 20, 15)
        self.product2 = Product("Молоко", 30, 10)
        self.stack.add_product(self.product1)
        self.stack.add_product(self.product2)

    def test_add_product(self):
        """
        Тестує додавання нових продуктів у стек.
        Перевіряє, що початковий розмір стеку == 2.
        Додає новий продукт і перевіряє, що розмір стеку збільшився до 3.
        """
        self.assertEqual(len(self.stack.get_all_products()), 2)
        self.stack.add_product(Product("Цукор", 40, 5))
        self.assertEqual(len(self.stack.get_all_products()), 3)

    def test_remove_product(self):
        """
        Тестує видалення продукту зі стеку (за принципом LIFO - Last In, First Out).
        Перевіряє, що видалений продукт - це "Молоко" (останній доданий).
        Також перевіряє, що розмір стеку зменшився до 1.
        """
        removed = self.stack.remove_product()
        self.assertEqual(removed.name, "Молоко")
        self.assertEqual(len(self.stack.get_all_products()), 1)

    def test_edit_product(self):
        """
        Тестує редагування існуючого продукту за індексом.
        Змінює назву та ціну продукту з індексом 0 ("Хліб").
        Перевіряє, що і назва, і ціна коректно оновилися.
        """
        self.stack.edit_product(0, name="Булка", price=25)
        self.assertTrue(self.stack.stack[0].name == "Булка")
        self.assertTrue(self.stack.stack[0].price == 25)

    def test_change_price(self):
        """
        Тестує часткове редагування - зміну тільки ціни продукту.
        Змінює ціну продукту з індексом 1 ("Молоко").
        Перевіряє, що нова ціна == 45.
        """
        self.stack.change_price(1, 45)
        self.assertTrue(self.stack.stack[1].price == 45)

    def test_change_quantity(self):
        """
        Тестує часткове редагування - зміну тільки кількості продукту.
        Змінює кількість продукту з індексом 0 ("Хліб").
        Перевіряє, що нова кількість == 100.
        """
        self.stack.change_quantity(0, 100)
        # Стверджуємо, що вираз "кількість == 100" є істинним
        self.assertTrue(self.stack.stack[0].quantity == 100)
        
    @unittest.expectedFailure
    def test_add_invalid_type(self):
        """
        Тест, який *очікує на провал* (expectedFailure).
        Перевіряє, чи генерує метод add_product помилку ValueError
        при спробі додати об'єкт, який не є екземпляром класу Product.
        Позначений як @expectedFailure, бо ми *припускаємо*, що код
        ще не реалізував цю перевірку (містить баг).
        """
        with self.assertRaises(ValueError):
            self.stack.add_product("не товар") # Це має викликати ValueError

    def test_remove_from_empty_stack(self):
        """
        Тестує поведінку при спробі видалити продукт з порожнього стеку.
        Створює новий порожній стек і перевіряє, що виклик
        remove_product() коректно генерує помилку IndexError.
        """
        empty_stack = ProductStack()
        with self.assertRaises(IndexError):
            empty_stack.remove_product()

    
    def test_invalid_price_or_quantity(self):
        """
        Тест, який *очікує на провал* (expectedFailure).
        Перевіряє, чи генерують методи change_price та change_quantity
        помилку ValueError при спробі встановити негативні значення.
        """
        with self.assertRaises(ValueError):
            # Цей блок очікує ValueError, але через "баг"
            # метод його не кидає, тому assertRaises "падає".
            self.stack.change_price(0, -5)
        
        with self.assertRaises(ValueError):
            # Аналогічно тут.
            self.stack.change_quantity(0, -10)

if __name__ == '__main__':
    unittest.main()