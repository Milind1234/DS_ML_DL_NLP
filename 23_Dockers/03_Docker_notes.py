# ============================================================
# DOCKER BEGINNER TO INTERVIEW CHEAT SHEET
# ============================================================

# ------------------------------------------------------------
# WHAT IS DOCKER?
# ------------------------------------------------------------
# Docker is a containerization platform.
# It packages an application along with all its dependencies
# into a lightweight container that can run anywhere.

# Image      -> Blueprint/Template
# Container  -> Running instance of an image
# Dockerfile -> Instructions to build an image
# Volume     -> Persistent storage
# Network    -> Communication between containers
# Registry   -> Storage for Docker images (Docker Hub)


# Docker
# - Containerization platform.
# - Packages application + dependencies into containers.

# Image
# - Read-only blueprint/template used to create containers.

# Container
# - Running instance of an image.

# Dockerfile
# - Text file containing instructions to build an image.

# Docker Compose
# - Runs multi-container applications using compose.yaml.

# Docker Hub
# - Public registry for Docker images.

# Registry
# - Storage location for Docker images.

# Volume
# - Persistent storage independent of container lifecycle.

# Bind Mount
# - Maps a host folder into a container.

# Network
# - Allows containers to communicate.

# ============================================================
# 2. INSTALLATION & HEALTH
# ============================================================

# docker --version
# Purpose: Show Docker version.

# docker compose version
# Purpose: Show Compose version.

# docker info
# Purpose: Show Docker daemon information.

# docker help
# Purpose: Show all commands.

# docker <command> --help
# Purpose: Help for one command.

# ============================================================
# BASIC COMMANDS
# ============================================================

# docker --version
# Definition:
# Shows the installed Docker version.
# --- $ docker --version


# docker info
# Definition:
# Displays detailed Docker information.
# Usage:
# Check whether Docker daemon is running.
# --- $ docker info


# docker help
# Definition:
# Shows all Docker commands.
# --- $ docker help


# ============================================================
# IMAGE COMMANDS
# ============================================================

# docker pull <image>
# Definition:
# Downloads an image from Docker Hub.
# --- $ docker pull nginx


# docker images
# Definition:
# Lists all downloaded images.
# --- $ docker images


# docker build -t <image-name> .
# Definition:
# Builds an image from a Dockerfile.
# --- $ docker build -t flask-app .


# docker rmi <image>
# Definition:
# Deletes an image.
# --- $ docker rmi flask-app


# docker image prune
# Definition:
# Removes unused images.
# --- $ docker image prune


# ============================================================
# CONTAINER COMMANDS
# ============================================================

# docker run <image>
# Definition:
# Creates and starts a container.
# --- $ docker run nginx


# docker run -d <image>
# Definition:
# Runs the container in background.
# --- $ docker run -d nginx


# docker run -p host:container image
# Definition:
# Maps host port to container port.
# --- $ docker run -p 5000:5000 flask-app


# docker run --name <container-name> image
# Definition:
# Assigns a custom name.
# --- $ docker run --name myapp flask-app


# docker ps
# Definition:
# Shows running containers.
# --- $ docker ps


# docker ps -a
# Definition:
# Shows all containers.
# --- $ docker ps -a


# docker stop <container>
# Definition:
# Stops a running container.
# --- $ docker stop myapp


# docker start <container>
# Definition:
# Starts a stopped container.
# --- $ docker start myapp


# docker restart <container>
# Definition:
# Restarts a container.
# --- $ docker restart myapp


# docker rm <container>
# Definition:
# Removes a container.
# --- $ docker rm myapp


# docker logs <container>
# Definition:
# Displays container logs.
# --- $ docker logs myapp


# docker logs -f <container>
# Definition:
# Shows logs continuously.
# --- $ docker logs -f myapp


# docker exec -it <container> sh
# Definition:
# Opens a shell inside the container.
# --- $ docker exec -it myapp sh


# docker inspect <container>
# Definition:
# Shows detailed information in JSON format.
# --- $ docker inspect myapp


# docker stats
# Definition:
# Shows CPU, RAM and network usage.
# --- $ docker stats


# ============================================================
# VOLUME COMMANDS
# ============================================================

# docker volume create <volume>
# Definition:
# Creates a volume.
# --- $ docker volume create myvolume


# docker volume ls
# Definition:
# Lists all volumes.
# --- $ docker volume ls


# docker volume inspect <volume>
# Definition:
# Displays volume details.
# --- $ docker volume inspect myvolume


# docker volume rm <volume>
# Definition:
# Deletes a volume.
# --- $ docker volume rm myvolume


# ============================================================
# NETWORK COMMANDS
# ============================================================

# docker network ls
# Definition:
# Lists Docker networks.
# --- $ docker network ls


# docker network create <network>
# Definition:
# Creates a custom network.
# --- $ docker network create mynetwork


# docker network inspect <network>
# Definition:
# Displays network details.
# --- $ docker network inspect mynetwork


# docker network rm <network>
# Definition:
# Deletes a network.
# --- $ docker network rm mynetwork


# ============================================================
# DOCKER COMPOSE COMMANDS
# ============================================================

# docker compose up
# Definition:
# Starts all services.
# --- $ docker compose up


# docker compose up -d
# Definition:
# Starts services in background.
# --- $ docker compose up -d


# docker compose up --build
# Definition:
# Rebuilds image before starting.
# --- $ docker compose up --build


# docker compose down
# Definition:
# Stops and removes services.
# --- $ docker compose down


# docker compose ps
# Definition:
# Lists Compose containers.
# --- $ docker compose ps


# docker compose logs
# Definition:
# Shows logs.
# --- $ docker compose logs


# docker compose logs -f
# Definition:
# Continuously streams logs.
# --- $ docker compose logs -f


# docker compose stop
# Definition:
# Stops services.
# --- $ docker compose stop


# docker compose start
# Definition:
# Starts stopped services.
# --- $ docker compose start


# docker compose restart
# Definition:
# Restarts services.
# --- $ docker compose restart


# ============================================================
# CLEANUP COMMANDS
# ============================================================

# docker system df
# Definition:
# Shows Docker disk usage.
# --- $ docker system df


# docker system prune
# Definition:
# Removes unused containers, networks and images.
# --- $ docker system prune


# docker system prune -a
# Definition:
# Removes everything unused including images.
# --- $ docker system prune -a


# ============================================================
# IMPORTANT FLAGS
# ============================================================

# -d
# Detached mode (background)

# -p
# Port mapping
# Example:
# --- $ docker run -p 5000:5000 flask-app

# -v
# Mount volume
# --- $ docker run -v myvolume:/app/data flask-app

# --name
# Give custom container name

# -it
# Interactive terminal

# --rm
# Remove container automatically after exit

# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

# What is Docker?
# Containerization platform.

# What is an Image?
# Blueprint used to create containers.

# What is a Container?
# Running instance of an image.

# Difference between VM and Container?
# VM:
#   - Has Guest OS
#   - Heavy
#   - Slow startup
#
# Container:
#   - Shares Host OS kernel
#   - Lightweight
#   - Starts in seconds

# What is Dockerfile?
# File containing instructions to build an image.

# What is Docker Compose?
# Tool to run multiple containers using docker-compose.yml.

# What is a Volume?
# Persistent storage outside the container.

# What is Docker Hub?
# Public registry to store Docker images.

# ============================================================
# MOST COMMON INTERVIEW COMMANDS
# ============================================================
"""
docker build -t app .
docker images
docker run -p 5000:5000 app
docker ps
docker ps -a
docker logs <container>
docker exec -it <container> sh
docker stop <container>
docker rm <container>
docker rmi <image>
docker compose up --build
docker compose down
docker system prune -a
"""
# ============================================================
# END OF CHEAT SHEET
# ============================================================