
# Docker Python Flask Login App

This is a simple login and registration web application built with Python Flask and Docker. The application uses SQLite database and runs inside a Docker container.

---

## Requirements

1. Python 3.9
2. Docker
3. Git

---

## Installation

### 1. Clone the repository

git clone https://github.com/KuldeepSahoo917/Docker-python-flask.git

cd Docker-python-flask


### 2. Build the app

docker build -t pythonapp .


### 3. Run the app

docker run -d -p 5000:5000 -v $(pwd):/app --name flask-container pythonapp


---

## Access the Application

Open your browser and go to:

http://localhost:5000


If running on a server:

http://<server-ip>:5000


---

## Application Usage

1. Open /register
2. Create a new username and password
3. Go to /login
4. Login using registered credentials
5. After login, dashboard will open
6. Click logout to exit

---

## Nginx

Install Nginx reverse proxy to make this application available on port 80.


sudo apt-get update
sudo apt-get install nginx


Edit Nginx configuration file:

sudo nano /etc/nginx/sites-available/default


Add this inside the server block:

location / {
proxy_pass http://127.0.0.1:5000
;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
}


Restart Nginx:

sudo systemctl restart nginx


Now access the application using:

http://<server-ip>


---

## Docker Commands

Stop container:

docker stop flask-container


Remove container:

docker rm flask-container


Rebuild container:

docker build -t pythonapp .
docker rm -f flask-container
docker run -d -p 5000:5000 -v $(pwd):/app --name flask-container pythonapp


---

## Technologies Used

- Python
- Flask
- SQLite
- Docker
- Nginx
- HTML
- CSS
- GitHub
