node {
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('greenhouse.firebase.json')
        SECRET_KEY = credentials('SECRET_KEY')
    }
    stage('Cleanup') {
        step([$class: 'WsCleanup'])
    }
    stage('Checkout SCM') {
        checkout scm
    }
    def pythonImage
    stage('build docker image') {
        pythonImage = docker.build("maxsum:build")
    }
    stage('test') {
        pythonImage.inside {
            sh '. /tmp/venv/bin/activate && python -m pytest --junitxml=build/results.xml'
        }
    }
    stage('collect test results') {
        junit 'build/results.xml'
    }
}