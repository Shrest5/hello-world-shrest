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
                    withEnv(["PATH+SONAR=${tool 'MySonarScanner'}/bin"]) {  
                        sh '''
                            sonar-scanner \
                            -Dsonar.projectKey=hello-world-shrest \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://13.50.17.10:9000
                        '''
                    }
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
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {

                    sh '''
                        echo "Logging into Docker Hub..."
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
    post {
        success {
            emailext(
            subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """Job '${env.JOB_NAME} [#${env.BUILD_NUMBER}]' succeeded. Build URL: ${env.BUILD_URL}""",
            to: "amrendra0918@gmail.com"
            )
        }
        failure {
            emailext(
            subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """Job '${env.JOB_NAME} [#${env.BUILD_NUMBER}]' failed. Build URL: ${env.BUILD_URL}""",
            to: "amrendra0918@gmail.com"
            )
        }
    }
}



    }
}


