pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building'
                bat '.\\myEnv\\Scripts\\pip install -r requirements.txt'
                bat '.\\myEnv\\Scripts\\python manage.py runserver'
            }
        }
    }
}