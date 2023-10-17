pipeline {
    agent {
        label 'server'
    }

    stages {
        stage('Commands') {
            steps {

                sh "ls"
                sh 'uname -a'
                sh "pwd"

                sh "python3 sum.py"

            }
        }
        stage('test1') {
    parallel {
        stage('parallel_stage_1') {
            steps{
                sh "sleep 20"
                echo "parallel_stage_1"

            }
        }

        stage('parallel_stage_2'){
            steps{
                echo "parallel_stage_2"
                sh "sleep 30"
            }

        }
      // One or more stages need to be included within the parallel block.
    }
  }
    }
}
