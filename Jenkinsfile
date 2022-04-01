pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building'
                bat '.\\myEnv\\Scripts\\python3 manage.py runserver'
            }
        }
    }
}