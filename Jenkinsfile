pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                echo 'In C or Java, we can compile our program in this step'
                echo 'In Python, we can build our package here or skip this step'
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''#!/bin/bash
                echo 'Test Step: We run testing tool like pytest here'

                # Create the virtual environment if it doesn't exist
                if [ ! -d "mlip" ]; then
                    python3 -m venv mlip
                fi

                # Activate the virtual environment
                source mlip/bin/activate

                # Install dependencies (pytest, pandas, numpy, etc.)
                pip install --upgrade pip
                pip install pytest pandas numpy

                # Run pytest in the virtual environment
                pytest

                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'In this step, we deploy our project'
                echo 'Depending on the context, we may publish the project artifact or upload pickle files'
            }
        }
    }
}
