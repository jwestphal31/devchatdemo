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
                   sh "docker build -t 507385280051.dkr.ecr.us-east-1.amazonaws.com/devchatdemo:latest ."
              }
          }

          stage('Push Docker Image to AWS ECR'){
           steps{
                script{
                    docker.withRegistry('507385280051.dkr.ecr.us-east-1.amazonaws.com/devchatdemo', 'ecr:us-east-1:ecr-credentials') {
                        docker.image('507385280051.dkr.ecr.us-east-1.amazonaws.com/devchatdemo:latest').push('latest')
                    }
                }
            }
          }


           stage('Initiate Trend Micro SmartCheck Container Image Assurance Scan'){
             steps{
                sh "python3 /home/ubuntu/jenkins_plugin.py"
             }
          }



            stage('Deploy to EKS'){
                steps{
                    sh "kubectl plugin ds assign_policy PCI"
                    sh "kubectl --kubeconfig=/home/ubuntu/kubeconfig delete --namespace=devchatdemo deployment devchatdemo"
                    sh "kubectl --kubeconfig=/home/ubuntu/kubeconfig apply -f devchatdemo-deployment.yaml"
                 }
          }

    }

}