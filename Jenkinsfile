pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh '''
                    # Create and activate a virtual environment
                    python3 -m venv mlip
                    . mlip/bin/activate  # Use dot instead of source

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
                    . mlip/bin/activate  # Use dot instead of source

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
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                sh '''
                    # Deployment steps (if any)
                    echo "Deployment goes here."
                '''
            }
        }
    }
}
