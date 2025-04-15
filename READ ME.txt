FastAPI Microservice Deployment

This Repo demonstrates a simple FastAPI microservice deployed using Docker and Kubernetes. It includes a Python script to automate containerization and deployment steps to your cluster.

Project Structure

microservices_deployment/
├── services/
│   └── service1/
│       ├── api.py
│       ├── dockapi.dockerfile
│       ├── k8sdeploy.yml
│       ├── k8service.yml
│       └── requirements.txt
├── deploy.py
├── LICENSE
└── READ ME.txt


Features

• FastAPI microservice
• Dockerized with Python 3.9-slim
• Kubernetes deployment and NodePort service
• deploy.py automation script:
      Builds Docker image
      Replace placeholders in YAML files
      Applies Kubernetes manifests

Requirements

• Docker
• Python 3.9+
• Kubernetes cluster (local or cloud)
• kubectl installed & configured


API Endpoints

/
Returns a welcome message.
Response:
{ "message": "Hello, Kubernetes!" }

/health
Health check endpoint.
Response:
{ "status": "healthy" }

License
This Repo is licensed under the Prem Sai Konduru Custom License. See the LICENSE file for details.
