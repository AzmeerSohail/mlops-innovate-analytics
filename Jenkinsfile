pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Taloo123/https://github.com/Taloo123/mlops-innovate-analytics.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('taloo123/mlops-project')
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
                            docker.image('yourdockerhubusername/mlops-project').push()
                        }
                    }
                }
            }
        }
    }
}
