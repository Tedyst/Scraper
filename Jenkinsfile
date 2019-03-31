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
        if (env.BRANCH_NAME == 'master') {
            stage('Build and Push to Docker') {
                steps {
                    script {
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
