# Capstone Server
Set up the environment necessary to host the BlackHorse OSINT/PAI course capstone CTFs. 


## Deployment
### Clone this repository
Clone this repository:
```
git clone https://github.com/ssblackhorse/capstone 
```

---
# Docker
This needs Docker and Docker Compose installed. 
These can be installed by running [install_docker.sh](/setup/install_docker.sh) or by following the instructions here:

[Docker](https://docs.docker.com/engine/install/ubuntu/)

[Docker Compose](https://docs.docker.com/compose/install/linux/#install-using-the-repository)

[Post Install Instructions](https://docs.docker.com/engine/install/linux-postinstall/ )

---
## Add a docker user
Add a non-root user for this server. The user is going to be named 'dockeruser'.

Add the user:
```
adduser dockeruser
```

Add the user to the sudo group:
```
adduser dockeruser sudo
```

Add the user to the docker group:
```
sudo usermod -aG docker dockeruser
```

Make the changes happen:
```
newgrp docker 
```

Change to the new user:
```
su dockeruser
```
--- 
## Setup the necessary folders and networks
We're going to front load some of the volumes and networks that need created. To do this easily, just run [create_environment.sh](/setup/create_environment.sh) or run these commands:

```
docker volume create swag
docker volume create classes
docker volume create ctfd
docker volume create portainer_data
docker network create swag_default
```
---
## Install Portainer
Change the directory to compose_files
```
cd compose_files
```

Run portainer-compose.yml
```
docker compose -f portainer-compose.yml
```

Portainer can now be accessed at https://{IP-ADDRESS}:9443. 

If you do not know the IP address for the server, try:

```
curl -s ifconfig.me
```

Open the Portainer web interface and you'll be asked to provide a password for the admin user. 

--- 
## Setting up SWAG
SWAG is the reverse proxy for this server. 

In Portainer, navigate to 'Stacks' and create a new stack called 'swag'.
Paste the contents of [swag.yml](/compose_files/swag.yml) into the box. 

In the SUBDOMAINS field, remove 'wildcard' and add any of the subdomains we'll be using (ie, caso,dwi,etc). 

Below that box, add [example.env](/config_files/example.env) as Environmental Variables. 
Add the values to 'PUID', 'PGID', 'DOMAIN', and 'EMAIL'.

Make sure you are 'dockeruser' and to find the PUID and PGID, type:
```
id $USER
```

Toggle 'Enable access control' to off and hit 'Deploy the stack.'

After a few minutes, test that it's working by going to your domain. 

In the swag directory (/var/lib/docker/volumes/swag/config/dns-conf) modify the appropriate .ini file for the dns provider. 

---
## Clone the CTFd repo
We also need to clone the CTFd repo to the appropriate location. 

```
sudo git clone https://github.com/CTFd/CTFd /var/lib/docker/volumes/ctfd/CTFd
```

---
## Building the CTFd Image
In order for this configuration to work, we need to build our own CTFd image. 

In Portainer, navigate to Images and select 'Build a new image'. 

Give the image the name 'ctf' and paste the contents of [ctfd-dockerfile](/config_files/ctfd-dockerfile) into the web editor box. 

Below the web editor, upload [requirements.txt](/config_files/requirements.txt) and [docker-entrypoint.sh](/config_files/docker-entrypoint.sh). 

Select 'Build the image' and wait. This takes a few minutes. 

---

# Creating Capstones
For any capstones that will be made, the following needs to be done:

## Prep the folders and confs
To set up courses, run [create_courses.sh](/setup/create_courses.sh). This will ask for a course name (ie, caso) and build the necessary folder structures. It will also generate the subfolder.conf files necessary for SWAG. 

```
courses
  └─$coursename
    ├─ uploads
    ├─ logs
    ├─ redis
    │  └─ data
    └─ db
       └─ mysql
```

## Creating the stack
Just like with swag, we need to add the capstone stacks in Portainer. 

Create a new stack and give it the name of the course. Copy the contents of [classes.yml](/compose_files/classes.yml) into the editor. 

Upload the .env file again and modify the variables 'COURSE' and 'EXTERNAL_PORT' to reflect the name of the course and increment one up from the last course (ie, if the EXTERNAL_PORT for the last created course was '8001', give this one '8002'.)

This may take a while to get going, but you can watch the logs by going to Containers > Coursename > Logs. 

If the {coursename} container is stuck on 'Waiting for the db', run the troubleshooting script. 

Once the stack has started and there's feedback in the {coursename} logs, you should be able to access the set up page by going to https://coursename.yourdomain.tld. 

