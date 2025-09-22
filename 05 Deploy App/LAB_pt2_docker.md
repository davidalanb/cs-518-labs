# Containerize app with Docker

Refs:

- https://docs.docker.com/guides/python/containerize/
- https://docs.docker.com/get-started/introduction/build-and-push-first-image/
- https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli

Submit: 

- submit URL for your docker hub PUBLIC repo to Canvas

## Initialize

0. Be sure your app is connecting to your cloud DB.

1. Initialize:
    - in the terminal, cd to the root of your app (where app.py is located)
    - Issue init command: 
        ```docker init```
    - set run command:
        ```flask run --port=80 --host=0.0.0.0 ```

2. Add requirements to requirements.txt
    - should be already done from part 1.

## Build and run

3. Build:
    - make sure Docker Desktop is running
    - open a terminal in your app's root
    - issue build command:
        ```docker compose up --build```

* List your images:
    - you can view them in Docker Desktop
    - or list with ```docker image ls```
    - note the image name

## Push your image to a container registry

* Option A. Push to Docker hub
    - login ```docker login```
    - tag the image with your username ```docker tag <IMAGE_NAME> <USERNAME>/<IMAGE_NAME>```
    - push the image ```docker push <USERNAME>/<IMAGE_NAME>```

## BONUS: deploy app with ACR and ACA

* Option B. Azure container registry
    - Bonus:deploy your app using Azure container apps 