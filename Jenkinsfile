pipeline {
    agent any

    environment {
        SONARQUBE = 'My-SonarQube'   // name configured in Jenkins
        DOCKER_IMAGE = "hello-world-app:latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv(SONARQUBE) {
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=hello-world-app \
                        -Dsonar.sources=. \
                        -Dsonar.python.version=3.9
                    '''
                }
            }
        }

        stage("Build Docker Image") {
            steps {
                sh '''
                    docker build -t ${DOCKER_IMAGE} .
                '''
            }
        }

        stage("Deploy using Docker Compose") {
            steps {
                sh '''
                    docker-compose down || true
                    docker-compose up -d --build
                '''
            }
        }
    }
}
