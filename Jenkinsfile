pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                app = docker.build("tedyst/scraper")
            }
        }

        stage('Unit Testing') {
            steps {
                app.inside {
                    sh '''
                        pip3 install virtualenv
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

        stage('Push image') {
            steps {
                docker.withRegistry('https://registry.hub.docker.com', 'docker') {
                    app.push("${env.BUILD_NUMBER}")
                    app.push("latest")
                }
            }
        }
    }

    post {
        always {
            junit 'text.xml'
            archiveArtifacts artifacts: 'text.xml'
        }
    }
}
