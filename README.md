# Docker-python-flask
Docker Python Flask Login App

This is a simple login and registration web application built with Python Flask and containerized using Docker. The application uses SQLite for database and Docker volume for persistent storage.

Requirements

Python 3.9+

Docker

Git

Installation
Clone the repository
git clone https://github.com/KuldeepSahoo917/Docker-python-flask.git
cd Docker-python-flask
Build the Docker Image
docker build -t pythonapp .
Run the Docker Container
docker run -d -p 5000:5000 -v $(pwd):/app --name flask-container pythonapp
Access the Application

Open your browser and go to:

http://localhost:5000

If running on a server:

http://<server-ip>:5000
