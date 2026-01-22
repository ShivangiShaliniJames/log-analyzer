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
                sh '''
                    export PYTHONPATH=$(pwd)
                    python3 -m pytest
                '''
    }
}

        stage('Run Log Analyzer') {
            steps {
                sh '''
                    export PYTHONPATH=$(pwd)

                    mkdir -p logs
                    echo "INFO Application started" > logs/app.log
                    echo "WARNING Disk space low" >> logs/app.log
                    echo "ERROR Failed to connect to DB" >> logs/app.log
                    python3 src/log_analyzer.py
                '''
            }
        }
    }
}
