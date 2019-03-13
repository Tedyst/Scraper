node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build') {
        app = docker.build("tedyst/scraper")
    }

    stage('Unit Testing') {
        app.inside {
            sh '''
                pip3 install virtualenv
                PYENV_HOME=$WORKSPACE/.pyenv/
                virtualenv --no-site-packages $PYENV_HOME
                source $PYENV_HOME/bin/activate
                pip3 install -U pytest
                pip3 install -r requirements.txt
            '''
            sh 'pytest'
            sh 'deactivate'
        }
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}
