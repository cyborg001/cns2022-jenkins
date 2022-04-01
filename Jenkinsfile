pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building'
                bat 'python3 manage.py runserver'
            }
        // }
        // stage('Test') {
        //     steps {
        //         echo 'Testing'
        //     }
        // }
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying'
        //     }
        // }
    }
}