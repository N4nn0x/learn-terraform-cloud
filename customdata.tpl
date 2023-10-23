#!/bin/bash
curl -o /terraform_cloud/.ssh/mtcazurekey.pub https://raw.githubusercontent.com/terraform_cloud/.ssh/mtcazurekey.pub

# Update the package database
sudo apt update

# Install required packages
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add the Docker repository to package sources
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package database again
sudo apt update

# Install Docker
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Start the Docker service and enable it to start on boot
sudo systemctl start docker
sudo systemctl enable docker

# Run the lab container image
sudo docker run -d -p 80:80 --name nano nanogk/dockerrepo:lab

# Run the Pumba container
sudo docker run -d -v /var/run/docker.sock:/var/run/docker.sock gaiaadm/pumba:master 

#Pumba command to stop 'nano' container... to be embedded into HTML and triggered through lambda
#pumba kill --signal SIGTERM ^nano

# To access a container:
# sudo docker exec -it nano /bin/bash
#
# Location of html in container: /usr/share/nginx/html
# src="https://github.com/N4nn0x/terraform_cloud/blob/N4nn0x-patch-1/containerfiles/lab_diagram.png?raw=true"
