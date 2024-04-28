pipeline {
    environment {
        //- update your credentials ID after creating credentials for connecting to Docker Hub
        registryCredential = 'docker-hub'
    }
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-python-app:${env.BUILD_ID}", '.').run('-p 8000:8000 --name my-running-app')
                }
            }
        }

        stage('Stop Container') {
            steps {
                script {
                    docker.stop('my-running-app')
                    docker.rm('my-running-app')
                }
            }
        }
    }
}
