pipeline{

    agent { label 'master' }
    stages {
          stage('Checkout'){
            steps{
                checkout scm
            }
          }

          stage('Package Docker Image'){
              steps{
                   sh "docker build -t 529505258873.dkr.ecr.us-east-1.amazonaws.com/devchatdemo:latest ."
              }
          }

          stage('Push Docker Image to ECR'){
           steps{
                script{
                    docker.withRegistry('https://us.gcr.io', 'gcr:gcr-284') {
                        docker.image('529505258873.dkr.ecr.us-east-1.amazonaws.com/devchatdemo').push('latest')
                    }
                }
            }
          }

           stage('Initiate Trend Micro SmartCheck Container Image Assurance Scan'){
             steps{
                sh './scan.sh'
             }
          }

            stage('Deploy to K8s'){
                steps{
                    sh ". /home/decvchatdemo/venv/bin/activate"
                    sh "kubectl --kubeconfig=/home/gce-test/.kube/config apply -f jeffsbooks-deployment-gcp.yaml"
                 }
          }

    }

}
