FROM jenkins/jenkins:lts
USER root

# 1. Оновлюємо та встановлюємо лише базові утиліти (без software-properties-common)
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# 2. Створюємо папку для ключів
RUN mkdir -p /etc/apt/keyrings

# 3. Завантажуємо GPG ключ Docker
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# 4. Додаємо репозиторій Docker вручну (використовуючи echo та tee)
RUN echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. Оновлюємо apt та встановлюємо Docker CLI
RUN apt-get update && apt-get install -y docker-ce-cli

# 6. Повертаємося до користувача jenkins та ставимо плагіни
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"