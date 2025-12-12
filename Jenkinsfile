pipeline {
    agent any

    environment {
        SONARQUBE = 'My-SonarQube'
        DOCKER_IMAGE = "hello-world-image"
        DOCKERHUB_USER = "shrest5"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Shrest5/hello-world-shrest.git'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('My-SonarQube') {
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=hello-world-shrest \
                        -Dsonar.sources=. \
                        -Dsonar.python.version=3.9
                    '''
                }
            }
        }

        stage("Build Docker Image") {
            steps {
                sh '''
                    docker build -t ${DOCKER_IMAGE}:latest .
                '''
            }
        }

        stage("Push to Docker Hub") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker',
                    usernameVariable: 'dockerHubUser',
                    passwordVariable: 'dockerHubPass'
                )]) {

                    sh '''
                        echo $dockerHubPass | docker login -u $dockerHubUser --password-stdin

                        docker tag ${DOCKER_IMAGE}:latest $dockerHubUser/${DOCKER_IMAGE}:latest
                        docker push $dockerHubUser/${DOCKER_IMAGE}:latest

                        docker logout
                    '''
                }
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

