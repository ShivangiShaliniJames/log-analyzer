pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Run Log Analyzer') {
            steps {
                sh 'python3 src/log_analyzer.py'
            }
        }
    }
}
