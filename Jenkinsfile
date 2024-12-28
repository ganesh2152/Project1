pipeline {
    agent any
    stages {
        stage("checkout Code") {
            steps{
                git url:'https://github.com/ganesh2152/Project1.git',branch:'main'
            }
        }
        stage("Build Docker image") {
            steps {
                sh'docker build -t myimage .'
            }
        }
        stage("Create Container") {
            steps {
                sh'docker run -d -p 8501:8501 myimage'
            }
        }
    }
}
