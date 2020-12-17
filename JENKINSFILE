pipeline{
    agent any
    stages{
        stage('SCM Checkout'){
            steps{
                git 'https://github.com/MikolajLuczyszyn/ansible'
            }
        }
         stage('Execute Ansible'){
            steps{
                ansiblePlaybook credentialsId: 'private-key3', disableHostKeyChecking: true, installation: 'ansible', playbook: 'third.yml'
            }
        }
    }
    
    
}
