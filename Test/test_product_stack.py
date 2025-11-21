# test_product_stack.py
import unittest
import product_stack as ps

class TestProductStack(unittest.TestCase):

    def setUp(self):
        """Викликається перед кожним тестом."""
        self.stack = ps.ProductStack()
        self.product1 = ps.Product("Хліб", 20, 15)
        self.product2 = ps.Product("Молоко", 30, 10)
        self.stack.add_product(self.product1)
        self.stack.add_product(self.product2)

    def test_add_product(self):
        self.assertEqual(len(self.stack.get_all_products()), 2)
        self.stack.add_product(ps.Product("Цукор", 40, 5))
        self.assertEqual(len(self.stack.get_all_products()), 3)

    def test_remove_product(self):
        removed = self.stack.remove_product()
        self.assertEqual(removed.name, "Молоко")
        self.assertEqual(len(self.stack.get_all_products()), 1)

    def test_edit_product(self):
        self.stack.edit_product(0, name="Булка", price=25)
        self.assertEqual(self.stack.stack[0].name, "Булка")
        self.assertEqual(self.stack.stack[0].price, 25)

    def test_change_price(self):
        self.stack.change_price(1, 45)
        self.assertEqual(self.stack.stack[1].price, 45)

    def test_change_quantity(self):
        self.stack.change_quantity(0, 100)
        self.assertEqual(self.stack.stack[0].quantity, 100)

    def test_add_invalid_type(self):
        with self.assertRaises(TypeError):
            self.stack.add_product("не товар")

    @unittest.expectedFailure
    def test_remove_from_empty_stack(self):
        empty_stack = self.stack
        with self.assertRaises(IndexError):
            empty_stack.remove_product()

    def test_invalid_price_or_quantity(self):
        with self.assertRaises(ValueError):
            self.stack.change_price(0, -5)
        with self.assertRaises(ValueError):
            self.stack.change_quantity(0, -10)

if __name__ == '__main__':
    unittest.main()
