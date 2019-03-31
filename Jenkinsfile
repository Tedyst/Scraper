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
                        script{
                            sh '''
                                docker build . -t tedyst/scraper
                                docker push tedyst/scraper
                            '''
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
