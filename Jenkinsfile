pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout the code from Git
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    # Create and activate a virtual environment
                    python3 -m venv mlip
                    source mlip/bin/activate

                    # Upgrade pip and install required dependencies
                    pip install --upgrade pip
                    pip install -r requirements.txt || {
                        echo "requirements.txt not found, installing manually"
                        pip install pandas numpy scikit-learn pytest
                    }
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    # Activate the virtual environment
                    source mlip/bin/activate

                    # Install scikit-learn in case it isn't in requirements.txt
                    pip install scikit-learn

                    # Run tests using pytest
                    pytest
                '''
            }
        }

        stage('Deploy') {
            when {
                // Deploy stage is skipped if there are earlier failures
                not {
                    failed()
                }
            }
            steps {
                sh '''
                    # Deployment steps (if any)
                    echo "Deployment goes here."
                '''
            }
        }
    }

    post {
        always {
            // Archive the test results and cleanup if necessary
            junit '**/test-results.xml'
            cleanWs()
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}
