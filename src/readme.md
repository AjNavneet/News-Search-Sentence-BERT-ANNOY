# Getting Started

1. Running the codes locally: Python 3.8
    - Create a virtual environment: In the terminal or command prompt, use the following command to create a new virtual environment:

        - For Windows:
            `python -m venv venv`

        - For macOS and Linux:
            `python3 -m venv venv`
        This command creates a new virtual environment named "venv" in the current directory.

    - Activate the virtual environment:

        - For Windows (Command Prompt):
            `venv\Scripts\activate.bat`


        - For macOS and Linux (Terminal) :
            `source venv/bin/activate`
    
    Once the virtual environment is activated, you should see the environment name (e.g., (venv)) in the terminal or command prompt.

    - Install project requirements: With the virtual environment active, you can now install the required packages for your project. Typically, the required packages are listed in a requirements.txt file. Make sure you have the requirements.txt file for your project.

    - To install the requirements, use the following command:
        `pip install -r requirements.txt`

    - Run Jupyter Notebooks
    - Run docker-compose.yml:
        - Install Docker on your system
        - Open cmd with Administrative rights
        - Change Directory to the directory where docker-compose.yml file is present
        - Run the commands:
            - `docker-compose build` - It should take around 15 -20 minutes if running for the first time.
            - `docker-compose up -d`
            


# Deploy to AWS
- Assumption
    - You already have EC2 Instance created with Docker Installed
    - Familiarity with Postman


- Push local changes to github
    - We understand that many users may want to share their work and collaborate with others. We encourage you to experiment with the code provided in our project and create your unique version of the project. 
    
    - However, we kindly request that you cite and acknowledge the ProjectPro website as a reference in your work. We appreciate your cooperation and hope this project inspires you to explore the exciting world of data science further.

    - Change config.ENV = "prod" before pushing


- SSH into EC2
    - ssh url

- Clone Repo 
    - git clone <your github repository url>

    - git fetch --all
    - git checkout <your branch name>

- Review required files
    - tree data
    - tree models
    - logs
    - tree src
    - ls server.py requirements.txt docker*

- Build and launch container
    - sudo docker-compose build
    - sudo docker-compose up -d


---

# Create EC2 instance
- Ubuntu 22.04 LTS
- t2.xlarge (4CPUs, 16GB)
- Ensure the security group expose port 5001 (or another port you want the service being reached on)

# Install Git
```
sudo apt-get update
sudo apt-get install git tree
```

# Install Docker and Docker Compose
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker

# Adding docker-compose-plugin
sudo apt install python3-pip
pip install --upgrade pip
sudo pip install docker-compose
```
# Clone repo and checkout in the right branch 
```
git clone your_repo_url
git fetch --all
git checkout branchname
```

# Launch app with docker-compose
```
sudo docker-compose build
sudo docker-compose up -d
```



