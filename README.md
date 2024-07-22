# End-to-End-Basic-Machine-Learning-Project - House Price Prediction

Steps:
Creating conda environment
----------------------------------------
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/ (use cmd in vscode)
```
or
```
conda activate venv
```
```
(cntrl+shift + p) to set the interpreter 
```
```
pip install -r requirements.txt
```
```
pip freeze > requirements.txt
```
----------------------------------------
To setup CI/CD pipeline in heroku we need 3 information

1. heroku email id.
2. heroku api key.
3. heroku app name.

>Note: Without these three information, we cannot deploy our project

---------------------------------------------------------------------
Build the Docker image
```
Docker build -t <image name>:<tag name> .
```
>Note: Image name always be in small letter.

To list docker images
```
Docker images
```
Run docker image
```
Docker run -p 5000:5000 -e PORT=5000 <image id >
```
To check running container
```
docker ps
```
To stopdocker container
```
docker stop <container id>
```
App url is 
```
https://ml-project-reg.herokuapp.com/hello
```
