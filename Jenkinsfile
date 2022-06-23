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
                cd env\\Scripts
                activate
                '''
            }
        }
        stage('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MihirHundiwala/Dockerize-Django-Web-App.git'
            }
        }
        stage('Build') {
            steps {
                bat """
                pip install -r requirements.txt
                cd src
                python manage.py makemigrations
                python manage.py migrate
                python manage.py collectstatic -c --no-input
                """
            }
        }
        stage('Checklist') {
            steps {
                bat '''
                cd src
                python manage.py check --deploy
                '''
            }
        }
        stage('Style Check') {
            steps {
                bat '''
                cd src
                flake8 main --max-line-length=127
                '''
            }
        }
        stage('Docker Build Image') {
            steps {
                bat '''
                docker build -t mihirhundiwala/django-app-gameison .
                docker image prune --filter="dangling=true" --force
                '''
            }
        }
        stage('Push image to registry') {
            steps {
                withCredentials([usernamePassword( credentialsId: 'dockerhub-credentials', usernameVariable: 'USER', passwordVariable: 'PASSWORD')]) {
                    bat '''
                    docker login -u %USER% -p %PASSWORD%
                    docker push mihirhundiwala/django-app-gameison
                    docker logout
                    '''
                }
            }
        }
    }
}