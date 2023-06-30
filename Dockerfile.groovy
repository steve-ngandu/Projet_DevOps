pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my-flask-app .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -p 9000:9000 -d my-flask-app'
            }
        }
    }
}