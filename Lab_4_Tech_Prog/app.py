# app.py
class SimpleCalculator:
    """
    Простий клас калькулятора для демонстрації CI/CD.
    """
    
    def add(self, a, b):
        """Повертає суму двох чисел."""
        return a + b

    def subtract(self, a, b):
        """Повертає різницю двох чисел."""
        return a - b

if __name__ == "__main__":
    print("Calculator app is running...")