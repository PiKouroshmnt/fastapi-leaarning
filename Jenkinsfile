pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Start with Docker Compose') {
            steps {
                sh 'docker compose -f docker-compose.yml up -d --build'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker compose exec web pytest .'
                sh 'docker compose exec web flake8 .'
                sh 'docker compose exec web black . --check'
                sh 'docker compose exec web isort . --check-only'
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
        }
    }
}
