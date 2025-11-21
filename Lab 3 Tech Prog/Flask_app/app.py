"""
To run this app:
docker build -t product-flask-app . ( за відусутності образу )
docker run --rm -p 5000:5000 product-flask-app
http://localhost:5000 (зайти сюди в браузері )

 """
import os
from flask import Flask, request, redirect, url_for, render_template_string
from product_stack import Product, ProductStack

app = Flask(__name__)

# Створюємо глобальний екземпляр стеку, щоб зберігати дані
stack = ProductStack()

# Додаємо початкові дані для демонстрації
stack.add_product(Product("Хліб", 20, 15))
stack.add_product(Product("Молоко", 30, 10))

# Використовуємо один рядок HTML як шаблон для простоти
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Менеджер Товарів</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 20px auto; padding: 20px; background-color: #f4f4f4; }
        h1, h2 { color: #333; }
        ul { list-style: none; padding: 0; }
        li { background: #fff; border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 5px; }
        form { background: #fff; padding: 20px; border: 1px solid #ddd; border-radius: 5px; margin-bottom: 20px; }
        input[type="text"], input[type="number"] { width: 95%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 3px; }
        button { background-color: #007bff; color: white; padding: 10px 15px; border: none; border-radius: 3px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .error { color: #d9534f; background: #f2dede; border: 1px solid #ebccd1; padding: 10px; border-radius: 3px; }
    </style>
</head>
<body>
    <h1>Менеджер Товарів (Стек)</h1>

    <!-- 1. Відображення товарів -->
    <h2>Поточні товари (Останній - зверху)</h2>
    <ul>
        {% for i, product in products_reversed %}
            <li>
                <b>[Індекс: {{ i }}] {{ product.name }}</b> - ₴{{ product.price }}, {{ product.quantity }} шт.
            </li>
        {% else %}
            <li>Стек порожній.</li>
        {% endfor %}
    </ul>

    <!-- 2. Відображення помилки (якщо є) -->
    {% if error %}
        <div class="error"><b>Помилка:</b> {{ error }}</div>
    {% endif %}

    <!-- 3. Форма додавання товару -->
    <h2>Додати товар (Push)</h2>
    <form action="/add" method="POST">
        Назва: <input type="text" name="name" required>
        Ціна: <input type="number" name="price" step="0.01" min="0" required>
        Кількість: <input type="number" name="quantity" min="0" required>
        <button type="submit">Додати</button>
    </form>

    <!-- 4. Кнопка видалення товару -->
    <h2>Видалити останній товар (Pop)</h2>
    <form action="/remove" method="POST">
        <button type="submit">Видалити останній</button>
    </form>

    <!-- 5. Форма оновлення ціни -->
    <h2>Оновити ціну (за індексом)</h2>
    <form action="/update_price" method="POST">
        Індекс товару: <input type="number" name="index" min="0" required>
        Нова ціна: <input type="number" name="price" step="0.01" min="0" required>
        <button type="submit">Оновити ціну</button>
    </form>

    <!-- 6. Форма оновлення кількості -->
    <h2>Оновити кількість (за індексом)</h2>
    <form action="/update_quantity" method="POST">
        Індекс товару: <input type="number" name="index" min="0" required>
        Нова кількість: <input type="number" name="quantity" min="0" required>
        <button type="submit">Оновити кількість</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    """Головна сторінка, що відображає всі товари та форми."""
    # Отримуємо список і реверсуємо його, щоб останній доданий був зверху
    products_reversed = list(enumerate(stack.get_all_products()))
    products_reversed.reverse()
    
    # Отримуємо повідомлення про помилку з URL, якщо воно є
    error = request.args.get('error')
    return render_template_string(HTML_TEMPLATE, products_reversed=products_reversed, error=error)

@app.route('/add', methods=['POST'])
def add_product():
    """Обробляє додавання нового товару."""
    try:
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        
        if price < 0 or quantity < 0:
            raise ValueError("Ціна та кількість не можуть бути від'ємними.")
            
        product = Product(name, price, quantity)
        stack.add_product(product)
    except Exception as e:
        # У разі помилки, перенаправляємо на головну та показуємо її
        return redirect(url_for('index', error=str(e)))
    
    # У разі успіху, просто оновлюємо головну сторінку
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove_product():
    """Обробляє видалення останнього товару."""
    try:
        stack.remove_product()
    except Exception as e:
        return redirect(url_for('index', error=str(e)))
    return redirect(url_for('index'))

@app.route('/update_price', methods=['POST'])
def update_price():
    """Обробляє зміну ціни товару за індексом."""
    try:
        index = int(request.form['index'])
        price = float(request.form['price'])
        stack.change_price(index, price)
    except Exception as e:
        return redirect(url_for('index', error=str(e)))
    return redirect(url_for('index'))

@app.route('/update_quantity', methods=['POST'])
def update_quantity():
    """Обробляє зміну кількості товару за індексом."""
    try:
        index = int(request.form['index'])
        quantity = int(request.form['quantity'])
        stack.change_quantity(index, quantity)
    except Exception as e:
        return redirect(url_for('index', error=str(e)))
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Встановлюємо порт 5000, стандартний для Flask
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' ОБОВ'ЯЗКОВИЙ для того, щоб Docker міг "бачити" додаток
    app.run(debug=True, host='0.0.0.0', port=port)
