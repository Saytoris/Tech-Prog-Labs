# main.py
import unittest
from product_stack import Product, ProductStack

# --- 1. Імпортуємо ваш готовий файл з тестами ---
try:
    # Намагаємось імпортувати ваш файл test_product_stack.py
    import test_product_stack
except ImportError:
    print("ПОМИЛКА: Не вдалося знайти файл 'test_product_stack.py'.")
    print("Переконайтеся, що він знаходиться в тій самій папці.")
    test_product_stack = None


# --- 2. Демонстрація роботи класів ---

def demonstrate_all_functions():
    """
    Демонструє послідовний виклик всіх функцій 
    з класів Product та ProductStack.
    """
    print("--- 1. Демонстрація класу Product ---")
    
    # 1.1 Створення екземпляру класу Product (виклик __init__)
    p1 = Product("Ноутбук", 25000.0, 10)
    
    # 1.2 Демонстрація __repr__ (через print)
    print(f"Створено товар: {p1}")
    
    # 1.3 Доступ до атрибутів
    print(f"Назва товару: {p1.name}")
    print(f"Ціна товару: {p1.price}")
    print(f"Кількість: {p1.quantity}")
    
    print("\n--- 2. Демонстрація класу ProductStack ---")
    
    # 2.1 Створення екземпляру ProductStack (виклик __init__)
    stack = ProductStack()
    print("Створено порожній стек.")

    # 2.2 Виклик get_all_products() (на порожньому стеку)
    print(f"Товари у стеку: {stack.get_all_products()}")

    # 2.3 Виклик add_product()
    print(f"\nДодаємо '{p1.name}'...")
    stack.add_product(p1)
    
    p2 = Product("Монітор", 8000.0, 15)
    print(f"Додаємо '{p2.name}'...")
    stack.add_product(p2)

    # 2.4 Виклик get_all_products() (зі списком товарів)
    print(f"\nТовари у стеку зараз:")
    for i, product in enumerate(stack.get_all_products()):
        print(f"  [{i}] {product}")

    # 2.5 Виклик edit_product()
    print(f"\nРедагуємо товар з індексом 0 (Ноутбук)...")
    stack.edit_product(0, name="Ноутбук Pro", price=30000.0, quantity=5)
    print(f"Результат: {stack.get_all_products()[0]}")

    # 2.6 Виклик change_price()
    print(f"\nЗмінюємо ціну товару з індексом 1 (Монітор) на 8500.0...")
    stack.change_price(1, 8500.0)
    print(f"Результат: {stack.get_all_products()[1]}")

    # 2.7 Виклик change_quantity()
    print(f"\nЗмінюємо кількість товару з індексом 0 (Ноутбук Pro) на 7...")
    stack.change_quantity(0, 7)
    print(f"Результат: {stack.get_all_products()[0]}")

    print(f"\nФінальний стан стеку:")
    for product in stack.get_all_products():
        print(f"  {product}")

    # 2.8 Виклик remove_product() (Pop)
    print("\nВидаляємо останній доданий товар (Монітор)...")
    removed_product = stack.remove_product()
    print(f"Видалено: {removed_product}")
    
    print(f"\nТовари у стеку після видалення:")
    for product in stack.get_all_products():
        print(f"  {product}")
        
    print("\n--- Демонстрацію завершено ---")


# --- 3. Запуск тестів ---

def run_tests():
    """
    Запускає тести, імпортовані з 'test_product_stack.py'.
    """
    print("\n=============================================")
    print("           ЗАПУСК ЮНІТ-ТЕСТІВ")
    print("=============================================")
    
    if test_product_stack:
        # Створюємо завантажувач та набір тестів з імпортованого модуля
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(test_product_stack)
        
        # Створюємо виконавця тестів (Test Runner)
        runner = unittest.TextTestRunner(verbosity=2)
        
        # Запускаємо тести
        runner.run(suite)
    else:
        print("Тести не запущено, оскільки файл 'test_product_stack.py' не знайдено.")

    print("--- Тестування завершено ---")


# --- Головна функція запуску ---

if __name__ == "__main__":
    
    # 1. Спочатку запускаємо демонстрацію
    demonstrate_all_functions()
    
    # 2. Після демонстрації запускаємо тести
    run_tests()