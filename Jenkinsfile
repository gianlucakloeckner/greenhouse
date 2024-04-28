pipeline {
    environment {
        //- update your credentials ID after creating credentials for connecting to Docker Hub
        registryCredential = 'docker-hub'
    }
    agent {
        dockerfile {
            filename 'Dockerfile'
            reuseNode true
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-python-app:${env.BUILD_ID}", '.')
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
