FROM jenkins/jenkins:lts
USER root
# Встановлення базових утиліт
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
# Додавання ключів Docker
RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
# Додавання репозиторію
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
# Встановлення Docker CLI
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
# Встановлення плагінів
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"