pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t banking-app .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running basic health check...'
                bat 'docker run --rm -d -p 5050:5000 --name banking-app-test banking-app'
                bat 'timeout /t 5'
                bat 'curl http://localhost:5050/health'
                bat 'docker stop banking-app-test'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed - check the logs above.'
        }
    }
}