pipeline {
    agent any  // Use any available agent for the pipeline

    environment {
        DOCKERHUB_CREDENTIALS = 'docker-c'  // Define credentials ID for Docker Hub
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Checkout the code from the GitHub repository
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image with a tag using the current Git commit ID
                    def image = docker.build("bhargavram458/service-${env.BRANCH_NAME}:${GIT_COMMIT}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push the image to Docker Hub using the credentials
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        image.push()  // Push the Docker image to Docker Hub
                    }
                }
            }
        }
    }
}
