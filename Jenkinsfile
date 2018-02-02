pipeline {
    agent {
        docker {
            image 'python:latest'
        }
    }
    stages {
        stage('Initialise') {
            steps {
                sh 'pip install -r ./requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python ./diveguide/manage.py test'
            }
        }
        stage('Deliver') {
            steps {
                sh 'echo Delivery!!'
            }
        }
    }
}