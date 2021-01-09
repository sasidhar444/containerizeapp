# containerizeapp

step1: Basically, here we will take one sample python Flask web app

step2: We will containerize that web app using Docker

Step3: We will push that docker image to Google Container Registry

Step4: Then we will deploy that image in Google Kubernetes Engine

#Commands

git clone https://github.com/sasidhar444/containerizeapp.git

sudo docker image build -t pythonwebapp .

sudo docker run -p 5000:5000 -d pythonwebapp

[ sudo docker ps
  curl 0.0.0.0:5000
  # you should get the status
]

#Now push it GCR

sudo docker tag pythonwebapp gcr.io/PROJECT_ID/pythonwebapp

(MAKE SURE YOUR VM HAS PROPER ACCESS TO GCR  Ex:ServiceAccounts)
( Follow this for authentication issues :  "https://cloud.google.com/container-registry/docs/advanced-authentication#linux-macos_1")

sudo docker push gcr.io/PROJECT_ID/pythonwebapp:latest

Now connect to kubernetes cluster and use the YAML file from this repository

kubectl apply -f app.yaml

kubectl get deployments

kubectl expose deployment flask-app-tutorial --type=LoadBalancer --port 5000 --target-port 5000

kubectl get svc
