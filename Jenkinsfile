pipeline{

    agent { label 'node1' }
    stages {
          stage('Checkout'){
            steps{
                checkout scm
            }
          }


          stage('Package Docker Image'){
              steps{
                   sh "docker build -t 529505258873.dkr.ecr.us-east-1.amazonaws.com/devchatdemo ."
              }
          }

          stage('Push Docker Image to AWS ECR'){
           steps{
                script{
                    docker.withRegistry('https://529505258873.dkr.ecr.us-east-1.amazonaws.com/devchatdemo', 'ecr:us-east-1:ecr-credentials') {
                        docker.image('529505258873.dkr.ecr.us-east-1.amazonaws.com/devchatdemo').push('latest')
                    }
                }
            }
          }


           stage('Initiate Trend Micro SmartCheck Container Image Assurance Scan'){
             steps{
                sh "whoami"
                sh "pip3.6 install -r requirements_jenkins.txt"
                sh "python3.6 /home/centos/jenkins_plugin.py"
             }
          }



            stage('Deploy to EKS'){
                steps{
                    sh "kubectl --kubeconfig=/home/ubuntu/kubeconfig delete --namespace=default deployment devchatdemo"
                    sh "kubectl --kubeconfig=/home/centos/kubeconfig apply -f devchatdemo-deployment.yaml"
                 }
          }

    }

}
