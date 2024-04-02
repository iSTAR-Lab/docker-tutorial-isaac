# Build image
`docker build -t image_view .`

Builds the `Dockerfile` with an image tag of `image_view`

# Basic Docker Run
`docker run -p 5000:5000 -e FLASK_SECRET_KEY=lsdkjffodsfj0wes --name picture_website image_view`

### Explanation of command
- `-p 5000:500` exposes port 5000 from the application. Allows us to access the website on http://127.0.0.1:5000
- `-e FLASK_SECRET_KEY=...` sets an environment variable (add link to wikipedia) that our website uses
- `--name picture_wbsite` gives the container a specific name we can use to refer to it
- `image_view` the docker image we want to run

# Stop container
Press `^C` (Ctrl-C) if the terminal is showing logs

or `docker stop picture_website`

# Start a stopped container
`docker start picture_website`

# Destroy (remove) a container
`docker rm picture_website`

Note: This will remove all data stored within the container. We'll see how to prevent this soon

# Docker run with Volumes
`docker run -p 5000:5000 -e FLASK_SECRET_KEY=lsdkjffodsfj0wes -v pictures:/uploads --name picture_website image_view`

Note `-v pictures:/uploads` 
- `-v volume_name:MOUNT_POINT` specifies a volume name and where to mount it in the container

# Docker Compose
`docker compose up` - runs the compose.yml file

# Docker Compose with custom file
`docker compose -f custom_compose.yml up` - runs `custom_compose.yml`