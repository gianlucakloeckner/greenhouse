
pipeline {
    agent any
    environment {
        //once you sign up for Docker hub, use that user_id here
        registry = 'gianlucakloeckner/mypythonapp'
        //- update your credentials ID after creating credentials for connecting to Docker Hub
        registryCredential = 'docker-hub'
        dockerImage = ''
    }

    stages {
        stage('Cloning Git') {
            steps {
                checkout scm
            }
        }

        // Building Docker images
        stage('Building image') {
            steps {
                script {
                    dockerImage = docker.build registry
                }
            }
        }

        // Uploading Docker images into Docker Hub
        stage('Upload Image') {
            steps {
                script {
                    /* groovylint-disable-next-line NestedBlockDepth */
                    docker.withRegistry('', registryCredential) { dockerImage.push() }
                }
            }
        }

        // Running Docker container, make sure port 8096 is opened in
        stage('Docker Run') {
            steps {
                script {
                    dockerImage.run('-p 8096:8000 — rm — name mypythonappContainer')
                }
            }
        }
    }
}
