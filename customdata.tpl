#!/bin/bash

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

# Run the nginx container
sudo docker run -d -p 80:80 nginx

# Get HTML site from github repo and store in /var/www/html
sudo curl -o /var/www/landing.html https://raw.githubusercontent.com/terraform_cloud/containerfiles/landing.html

#curl -o /terraform_cloud/.ssh/mtcazurekey.pub https://raw.githubusercontent.com/terraform_cloud/.ssh/mtcazurekey.pub
