# Requirements:

    python3, Docker

# Build and run container

    docker build .
    docker images
    docker run -p 8000:80 #image_id

# Fast API provides swagger documentation, once container is up
    http://localhost:8000/docs

# Userful docker commands

kill all running containers with docker kill $(docker ps -q)
delete all stopped containers with docker rm $(docker ps -a -q)