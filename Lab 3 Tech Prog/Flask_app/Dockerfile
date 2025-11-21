# 1. Базовий образ (легкий Alpine Linux)
FROM alpine

# 2. Встановлення Python 3 та Pip
RUN apk add --update python3 py-pip

# 3. Встановлення Flask
# Використовуємо --break-system-packages, як було у вашому прикладі,
# щоб уникнути конфліктів з системними пакетами Alpine
RUN pip3 install flask --break-system-packages

# 4. Створення та перехід у робочу директорію
WORKDIR /app

# 5. Копіювання файлів
# Копіюємо всі .py файли (app.py, product_stack.py, test_product_stack.py)
COPY *.py /app/

# 6. (Рекомендовано) Запуск тестів під час збірки
# Цей крок перевіряє, що основна логіка працює коректно,
# перш ніж образ буде успішно зібрано.
RUN python3 -m unittest test_product_stack.py

# 7. "Відкриваємо" порт, який слухає Flask
# Це повідомляє Docker, що контейнер буде слухати порт 5000
EXPOSE 5000

# 8. Команда запуску
# Вказуємо, як запустити наш веб-додаток, коли контейнер стартує
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
