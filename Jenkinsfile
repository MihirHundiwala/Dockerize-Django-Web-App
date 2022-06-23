pipeline {
    agent any

    stages {
        stage('Create Environment') {
            steps {
                bat '''
                if exist env\\ (
                  echo "Python virtual environment exists." 
                ) else (
                  python -m venv env
                )
                '''
            }
        }
        stage('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MihirHundiwala/gameison.git'
            }
        }
        stage('Build') {
            steps {
                bat """
                pip install -r requirements.txt
                cd src
                python manage.py make migrations
                python manage.py migrate
                python manage.py collectstatic
                """
            }
        }
        stage('Checklist') {
            steps {
                bat 'python manage.py check --deploy'
            }
        }
        stage('Style Check') {
            steps {
                bat 'flake8 main --max-line-length=127'
            }
        }
        stage('Docker Build Image') {
            steps {
                bat '''
                cd ..
                docker build -t django-app-gameison .
                docker image prune --filter="dangling=true"
                '''
            }
        }
        stage('Push image to registry') {
            steps {
                bat 'docker image push django-app-gameison'
            }
        }
    }
}