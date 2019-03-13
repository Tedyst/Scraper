node {
    def app

    stage('Clone') {
        checkout scm
    }

    stage('Build') {
        app = docker.build("tedyst/scraper")
    }

    stage('Unit Testing') {
        app.inside {
            sh '''
                PYENV_HOME=$WORKSPACE/.pyenv/
                virtualenv --no-site-packages $PYENV_HOME
                source $PYENV_HOME/bin/activate
                pip install -U pytest
                pip install -r requirements.txt
                pytest
                deactivate
            '''
        }
    }

    stage('Push') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}
