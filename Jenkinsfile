pipeline {
    agent {
        label 'main'
    }

    stages {
        stage('Hello') {
            steps {
                sh "ls"
                def result = sh "python aes_des.py"
                println result
            }
        }
    }
}
