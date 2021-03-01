node
{
    stage('Get Source')
    {
        git ('https://github.com/mattydit/FlaskNBA.git')
        if (!fileExists("Dockerfile")) 
        {
            error('Dockerfile missing.')
        }
    }
    stage('Build Docker')
    {
        sh "sudo docker build -t flask-nba ."
    }
    stage("run docker container")
    {
        sh " sudodocker run --name flask-app-nba -p 5001:5001 -d flask-nba"
    }
}