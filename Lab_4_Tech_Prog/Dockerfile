# Використовуємо легкий Python образ
FROM python:3.9-slim

# Встановлюємо робочу папку всередині контейнера
WORKDIR /app

# Копіюємо файли з поточної папки (Lab_4_Tech_Prog) в контейнер
COPY . /app

# Встановлюємо залежності (якщо вони є)
RUN pip install flask unittest-xml-reporting

# Команда запуску (хоча для бібліотеки це не обов'язково, але для образу треба)
CMD ["python", "app.py"]