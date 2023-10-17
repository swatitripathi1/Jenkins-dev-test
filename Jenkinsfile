pipeline {
    agent {
        label 'ubuntu'
    }

    stages {
        stage('Build-1') {
            steps {
                sh 'uname -a'
                sh 'ls'
                sh 'pwd'
                sh 'ifconfig'

            }
        }
        stage('Test2') {
    stages {

        stage('_stage_1') {
            steps{

                echo "_stage_1"
                sh "sleep 20"
            }
        }

        stage('_stage_2'){
            steps{

                echo "_stage_2"
                sh "sleep 20"
            }

        }
      // One or more stages need to be included within the stages block.

    }
  }
    }
}
