# MiniProject4-OS

Team Members: Kofi Omari Asante (39932022) and Stacy Nyamekye Sarfo (55242022)


In this project, we are developing and deplying a web application using Docker. 
The web application must provide the following APIs:

/permissions?code=<number>
This API method accepts a code given by number and returns a JSON object specifying the permissions represented for owner, group and other. 
E.g., The request /permissions?code=744 should return 

{owner: [read, write, execute], group [read], other:[read]}.


/parity?b1=<bits>&b2=<bits>&b3=<bits>&b4=<bits>
This API method accepts the bits on corresponding disk blocks of a RAID-4 and returns the parity bits. Assume that each block has two bits. 
E.g., The request /parity?b1=00&b2=10&b3=11&b4=10 should return 11.

The goals of the project are to:
- Successfully deploy the web application using docker
- Create API methods created work correctly

# Running the Docker Application
  
  Assuming that you already have docker and the requirements.txt file created, 
  Create a dockerfile under the current directory and add the following code,
  
    FROM alpine:latest

    RUN apk update
    RUN apk add py-pip
    RUN apk add --no-cache python3-dev 
    RUN pip3 install --upgrade pip

    WORKDIR /app
    COPY . /app
    RUN pip3 --no-cache-dir install -r requirements.txt

    CMD ["python3", "main.py"]
  
  With the docker file created, the next step is to build and run the docker image.
  Use the code below to build the:
  
    docker build -t flask-rest-api .
  
  ##Note: the "flask-rest-api" can be changed to any name.
  
  You can use code below to verify the docker image
  
    docker images
  
  If the image is created, the code below is used to run it:
  
    docker run -d -p 5000:5000 flask-rest-api
  
  To check if the container is running, use:
  
    docker ps -a
  
  Using the line of code below, you can check the logs of the container to ensure the application is running:
  
    docker logs <CONTAINER ID OR CONTAINER NAME>
  
