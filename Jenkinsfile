pipeline {
    agent {
        docker {
            image 'python:latest'
        }
    }
    stages {
        stage('Initialise') {
            steps {
                sh 'chmod u+x ./jenkins'
                sh 'pip install -r ./requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh './jenkins/test.sh'
            }
        }
        stage('Deliver') {
            steps {
                sh 'echo Delivery!!'
            }
        }
    }
}