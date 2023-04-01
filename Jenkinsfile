pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my-image .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run my-image pytest'
            }
        }
    }
}
