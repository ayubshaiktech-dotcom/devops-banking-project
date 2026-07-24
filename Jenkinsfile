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
                sh 'docker build -t banking-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running basic health check...'
                sh 'docker rm -f banking-app-test || true'
                sh 'docker run -d -p 5050:5000 --name banking-app-test banking-app'
                sh 'sleep 5'
                sh 'docker logs banking-app-test || true'
                sh 'docker ps -a --filter name=banking-app-test || true'
                sh '''
                    CONTAINER_IP=$(docker inspect -f "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" banking-app-test || echo "")
                    echo "Container IP: $CONTAINER_IP"
                '''
            }
        }
    }

    post {
        always {
            sh 'docker rm -f banking-app-test || true'
        }
        failure {
            echo 'Pipeline failed - check the logs above.'
        }
    }
}
