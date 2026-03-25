
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
```
git clone https://github.com/KuldeepSahoo917/Docker-python-flask.git
```
```
cd Docker-python-flask
```

### 2. Build the app
```
docker build -t pythonapp .
```

### 3. Run the app
```
docker run -d -p 5000:5000 -v $(pwd):/app --name flask-container pythonapp
```

---

## Access the Application

Open your browser and go to:
```
http://localhost:5000
```

If running on a server:
```
http://<server-ip>:5000
```

---
If someone asks how Docker Flask works, say this:

Flow:
```
User Browser → Port 5000 → Docker Container → Flask App → Response → Browser
```
---
Dockerfile → Builds image

Image → Template

Container → Running app

requirements.txt → Installs dependencies

app.py → Application code

