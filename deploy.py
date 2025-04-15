import os
import subprocess
import sys


BASE_DIR = "./services"


def build_and_deploy(service_name):
    service_dir = os.path.join(BASE_DIR, service_name)
    

    if not os.path.isdir(service_dir):
        print(f"Service '{service_name}' does not exist in {BASE_DIR}.")
        return
    
    # Build the Docker image for the service
    image_name = f"{service_name}-image:latest"
    print(f"Building Docker image for {service_name}...")
    
    
    subprocess.run(["docker", "build", "-t", image_name, "-f", os.path.join(service_dir, "dockapi.dockerfile"), service_dir], check=True)

    for file in ["k8sdeploy.yml", "k8service.yml"]:
        file_path = os.path.join(service_dir, file)
        with open(file_path, "r") as f:
            content = f.read().replace("{{SERVICE_NAME}}", service_name).replace("{{IMAGE_NAME}}", image_name)
        with open(file_path, "w") as f:
            f.write(content)

    print(f"Applying Kubernetes deployment and service for {service_name}...")
    subprocess.run(["kubectl", "apply", "-f", os.path.join(service_dir, "k8sdeploy.yml")], check=True)
    subprocess.run(["kubectl", "apply", "-f", os.path.join(service_dir, "k8service.yml")], check=True)

    print(f"Service '{service_name}' deployed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python deploy.py <service_name>")
        sys.exit(1)
    
    service_name = sys.argv[1]
    build_and_deploy(service_name)
