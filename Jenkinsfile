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
                sh 'docker run --rm -d -p 5050:5000 --name banking-app-test banking-app'
                sh 'sleep 5'
                sh '''
                  CONTAINER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' banking-app-test)
                  echo "Testing container at $CONTAINER_IP"
                  curl -f http://$CONTAINER_IP:5000/health
                '''
                sh 'docker stop banking-app-test'
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