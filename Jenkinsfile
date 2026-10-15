pipeline {
    agent any
    stages {
        stage('Run JMeter') {
            steps {
                bat 'jmeter -n -t "silicon-drive-load-test-10k.jmx" -l results.jtl'
            }
        }
    }
}

