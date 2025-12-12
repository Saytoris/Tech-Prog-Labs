pipeline {
    agent none
    
    // Глобальні змінні для зручності
    environment {
        // Логін Dockerhub
        DOCKERHUB_USERNAME = 'saytoris' 
        // Назва образу
        APP_NAME = 'lab4-calculator'
        // ID ключа, який ми створили в Jenkins 
        DOCKERHUB_CREDENTIALS_ID = 'docker-hub-login'
    }

    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        }
        
        stage('Test') {
            agent {
                docker {
                    image 'python:3.9-alpine'
                    args '-u="root"'
                }
            }
            steps {
                dir('Lab_4_Tech_Prog') {
                    sh 'rm -rf test-reports'
                    sh 'pip install unittest-xml-reporting'
                    sh 'python test_app.py'
                }
            }
            post {
                always {
                    junit 'Lab_4_Tech_Prog/test-reports/*.xml'
                }
            }
        }
        
        stage('Build & Push to Docker Hub') {
            // Цей крок виконується на головному агенті (де є доступ до docker socket)
            agent any 
            steps {
                dir('Lab_4_Tech_Prog') {
                    script {
                        echo "Building Docker Image..."
                        
                        // Авторизуємося в Docker Hub, використовуючи збережений ключ
                        docker.withRegistry('', DOCKERHUB_CREDENTIALS_ID) {
                            
                            // Формуємо повну назву образу: логін/назва:номер_збірки
                            // наприклад: saytoris/lab4-calculator:15
                            def customImage = docker.build("${DOCKERHUB_USERNAME}/${APP_NAME}:${env.BUILD_ID}")
                            
                            echo "Pushing Docker Image..."
                            // Відправляємо на Docker Hub
                            customImage.push()
                            
                            // Також бажано ставити тег 'latest', щоб це була найсвіжіша версія
                            customImage.push('latest')
                        }
                    }
                }
            }
        }
    }
}