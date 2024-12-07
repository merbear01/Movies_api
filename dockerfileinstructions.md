# The Creation of The Dockerfile and Docker compose file

You need to first ensure that you have Docker installed on your machine. If you don't have Docker installed, you can download it from the official Docker website [here](https://www.docker.com/products/docker-desktop).
Once you have Docker installed, you can create a Dockerfile in the root directory of your project. The Dockerfile is a text file that contains all the commands needed to build a Docker image. Here is an example of a Dockerfile for a Python application:

```Dockerfile
# Use the official Python image as the base image
# You can have a look at the available Python images on Docker Hub: https://hub.docker.com/_/python
FROM python:3.8-slim 

# Set the working directory in the container
WORKDIR /movieapi

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Run the application
CMD ["python", "app.py"]
```

# Creating a Docker-compose file

To create the Docker-compose file, you need to create a new file named `docker-compose.yml` in the root directory of your project. The Docker-compose file is a YAML file that defines services, networks, and volumes for your application. Here is an example of a Docker-compose file for a Python application:

```yaml
version: '3.8'

services:
  movieapi:
    build: .
    ports:
      - "5000:5000"
```

In this Dockerfile:
- We are using the official Python image as the base image. You can choose a different base image depending on your application's requirements.
- We set the working directory in the container to `/movieapi`.
- We copy the `requirements.txt` file to the working directory and install the dependencies using `pip`.
- We copy the rest of the application code to the working directory.
- We specify the command to run the application when the container starts.
- You can customize this Dockerfile based on your application's requirements.
- Once you have created the Dockerfile, you can build the Docker image using the `docker build` command. 
In this Docker-compose file:
- We define a service named `movieapi` that builds the Docker image using the Dockerfile in the current directory.
- We map port 5000 on the host machine to port 5000 in the container.
- You can customize this Docker-compose file based on your application's requirements.
- Once you have created the Docker-compose file, you can run the Docker container using the `docker-compose up` command. 


Run the following command in the root directory of your project:

```bash
docker build -t movieapi .
```
```bash
docker-compose up
```

This command builds a Docker image with the tag `movieapi` based on the Dockerfile in the current directory. You can replace `movieapi` with any name you prefer for your Docker image.

After the Docker image is built successfully, you can run the Docker container using the `docker run` command. Run the following command to start the container:

```bash
docker run -p 5000:5000 movieapi
```

This command starts a Docker container based on the `movieapi` image and maps port 5000 on the host machine to port 5000 in the container. You can access your application at `http://localhost:5000`.

That's it! You have successfully created a Docker image for your Python application and run it in a Docker container. You can now deploy your Docker image to any platform that supports Docker containers.

