pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                checkout scm
            }
        }

        stage('Unit Testing') {
            steps {
                script {
                    sh '''
                        PYENV_HOME=$WORKSPACE/.pyenv/
                        virtualenv --no-site-packages $PYENV_HOME
                        source $PYENV_HOME/bin/activate
                        pip install -U pytest
                        pip install -r requirements.txt
                        pytest --junitxml=text.xml
                        deactivate
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                docker.build("tedyst/scraper")
            }
        }

        stage('Push Docker Image') {
            steps {
                docker.withRegistry('https://registry.hub.docker.com', 'docker') {
                    app.push("latest")
                }
            }
        }
    }

    post {
        always {
            junit 'text.xml'
        }
    }
}
