#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker not found. Installing Docker..."
    # Install Docker 
    sudo apt-get update
    sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install docker-ce
    sudo usermod -aG docker ${USER}
    sudo systemctl enable docker
    sudo systemctl start docker
    echo "Docker installed successfully."
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose not found. Installing Docker Compose..."
    # Install Docker Compose
    sudo apt install docker-compose
fi

# Run Docker Compose in the current folder
docker compose build
# Check if the containers are running
if [ $? -eq 0 ]; then
    echo "Docker containers are running."
else
    echo "Failed to start Docker containers."
fi

# Activate the virtual environment if it exists else create it
if [ ! -d "env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv env
fi
# Activate the virtual environment
source env/bin/activate
# Check if the virtual environment is activated
if [ $? -eq 0 ]; then
    echo "Virtual environment activated."
else
    echo "Failed to activate virtual environment."
fi
# install required python packages
pip3 install -r requirements.txt
# ask for permission to run the script
chmod +x run.sh
# prompt the user to run the script
while true; do
    read -p "Do you want to run the script? (y/n): " yn
    case $yn in
        [Yy]* ) sudo ./run.sh; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done