# 🐧 Ubuntu Bash Practice Lab with Docker
#A clean, ready-to-use Ubuntu environment for practicing Bash scripting, Linux commands, and DevOps skills running inside Docker on Windows, macOS, or Linux.Perfect for beginners and intermediate users who want a safe sandbox without dual-booting or messing up their main machine.

## ✨ Features

- ✅ Full Ubuntu latest image
- ✅ Pre-installed essential tools (`curl`, `git`, `vim`, `htop`, `tree`, etc.)
- ✅ Non-root `satyalab` with sudo privileges (best security practice)
- ✅ Works perfectly on **Windows + Docker Desktop**
- ✅ One-command startup
- ✅ Persistent practice (optional volume)

## 🚀 Quick Start 

### 1. Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- At least 2 GB RAM allocated to Docker

### 2. Pull & Run

```bash
# Pull the latest Ubuntu image
docker pull ubuntu

# Run the practice(In my case satyalab) lab container
docker run -it --name ubuntu-satyalab ubuntu

Step-2 -: Inside the Container — First Time Setup (From root user you should install all below )

# Update system
apt update && apt upgrade -y

# Install useful tools
apt install -y bash curl wget git nano vim tree htop sudo net-tools iputils-ping dnsutils

# Create a normal user (highly recommended you can give here your own userid )
adduser satya
usermod -aG sudo satya

# Switch to the normal user
su - satya

Now you have a clean, realistic Ubuntu environment to practice


Full Step-by-Step Guide in detailed order 


1- Start the container 
#docker run -it --name ubuntu-satyalab ubuntu bash

2- Run the setup script as below step by step(can run all below commands at a time or individually) :

#

apt update && apt upgrade -y && \
apt install -y bash curl wget git nano vim tree htop sudo net-tools iputils-ping dnsutils && \
adduser satya && \
usermod -aG sudo satya && \
su - satya


step-3 :(Optional) Make it persistent (so files survive container restart)

#docker run -it --name ubuntu-satyalab -v ubuntu-satyalab-data:/home/satyalab ubuntu

Exit & Re-enter anytime:


exit          # leaves container
docker start ubuntu-satyalab && docker attach ubuntu-satyalab


Stop & Remove (when you want a fresh start):

docker stop ubuntu-satyalab
docker rm ubuntu-satyalab

Common Commands You will Practice 

#File System-: ls, cd, pwd, mkdir, touch, cp, mv, rm, tree
#Text Editing- nano, vim
#Networking - ping, curl, wget, ip addr
#Process - ps, htop, kill
#User Management - whoami, sudo, su
# Package Mgmt- apt update, apt install


# What You Can Practice HereBash scripting (for, while, functions, arguments)
Shell scripting projects
Git workflows
Linux system administration
DevOps tool installation
Networking & troubleshooting

Feel free to open issues or pull requests!
Ideas for improvement:Add a setup.sh script
Docker Compose version
Pre-installed popular tools (jq, fzf, ripgrep, etc.)








