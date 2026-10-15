pipeline {
    agent any
    stages {
        stage('Run JMeter') {
            steps {
                bat '"C:\\apache-jmeter-5.6.3\\bin\\jmeter.bat" -n -t "silicon-drive-load-test-10k.jmx" -l results.jtl'
            }
        }
    }
}
