#!groovy
pipeline{
	agent {
		   label 'agent-1'
		 	}
	environment{
		registry = 'robolab.innopolis.university:5000/ttsdemo'
		tag_test = 'test'
		tag_beta = 'latest'
	}
	stages{
		stage('Docker'){
			steps{
				script{

					def image = docker.build("${env.registry}:${env.tag_test}", "./")
					image.inside('-u 0:0'){
						    sh 'python3 manage.py test'
					    }
					
					image.tag("${env.tag_beta}")

					withDockerRegistry([credentialsId: "jenkins-service", url: "https://robolab.innopolis.university:5000"]){
						image.push('latest')
					}
				}
			}
		}
		stage('Clean'){
			steps{
			    sh "docker image rm ${env.registry}:${env.tag_test}"
			}
		}
	}
}

