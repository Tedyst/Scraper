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
                        pip install -r requirements.txt
                        pytest --junitxml=text.xml
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'master') {
                        docker.build("tedyst/scraper")
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'master') {
                        docker.withRegistry('https://registry.hub.docker.com', 'docker') {
                            app.push("latest")
                        }
                    }
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
