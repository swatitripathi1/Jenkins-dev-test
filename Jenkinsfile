pipeline {
    agent {
        label 'main'
    }

    stages {
        stage('Hello') {
            steps {
                sh "ls"
                sh "python aes_des.py"
            }
        }
    }
}
