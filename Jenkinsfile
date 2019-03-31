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
                        pip3 install -r requirements.txt
                        pytest --junitxml=text.xml
                    '''
                }
            }
        }
        
        stage('Build and Push to Docker') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'master') {
                        docker.build("tedyst/scraper")
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
