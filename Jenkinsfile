pipeline {
    agent any

    environment {
        SONARQUBE = 'My-SonarQube'                // Name from Jenkins → Configure System
        DOCKER_IMAGE = "hello-world-image"          // Image name
        DOCKERHUB_USER = "your-dockerhub-username"
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
                withSonarQubeEnv(SONARQUBE) {
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
                        echo "Logging in..."
                        echo $PASS | docker login -u $USER --password-stdin

                        echo "Tagging image..."
                        docker tag ${DOCKER_IMAGE}:latest $USER/${DOCKER_IMAGE}:latest

                        echo "Pushing image..."
                        docker push $USER/${DOCKER_IMAGE}:latest

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
