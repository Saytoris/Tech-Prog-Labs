# product_stack.py

class Product:
    """Клас, який представляє товар."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} (₴{self.price}, {self.quantity} шт.)"


class ProductStack:
    """Клас для управління товарами на основі стеку."""
    def __init__(self):
        self.stack = []

    def add_product(self, product):
        """Додає товар до стеку (операція push)."""
        if not isinstance(product, Product):
            raise TypeError("Можна додавати лише об’єкти класу Product.")
        self.stack.append(product)

    def remove_product(self):
        """Видаляє останній доданий товар (операція pop)."""
        if not self.stack:
            raise IndexError("Стек порожній. Немає товарів для видалення.")
        return self.stack.pop()

    def edit_product(self, index, name=None, price=None, quantity=None):
        """Редагує товар за індексом."""
        if index < 0 or index >= len(self.stack):
            raise IndexError("Неправильний індекс товару.")
        product = self.stack[index]
        if name is not None:
            product.name = name
        if price is not None:
            product.price = price
        if quantity is not None:
            product.quantity = quantity

    def change_price(self, index, new_price):
        """Змінює ціну товару."""
        if new_price < 0:
            raise ValueError("Ціна не може бути від’ємною.")
        self.stack[index].price = new_price

    def change_quantity(self, index, new_quantity):
        """Змінює кількість товару."""
        if new_quantity < 0:
            raise ValueError("Кількість не може бути від’ємною.")
        self.stack[index].quantity = new_quantity

    def get_all_products(self):
        """Повертає список усіх товарів."""
        return self.stack
    

