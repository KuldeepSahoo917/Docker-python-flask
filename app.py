from flask import Flask, request, redirect, url_for, session, render_template_string
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# Initialize Database
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

init_db()

# HTML Templates
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body { font-family: Arial; background: linear-gradient(to right, #4facfe, #00f2fe); }
        .box { width: 300px; margin: 150px auto; padding: 20px; background: white; border-radius: 10px; text-align: center; }
        input { width: 90%; padding: 10px; margin: 10px; }
        button { padding: 10px 20px; background: #4facfe; border: none; color: white; }
        a { text-decoration: none; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
            <p>New user? <a href="/register">Register</a></p>
        </form>
    </div>
</body>
</html>
"""

register_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
    <style>
        body { font-family: Arial; background: linear-gradient(to right, #43e97b, #38f9d7); }
        .box { width: 300px; margin: 150px auto; padding: 20px; background: white; border-radius: 10px; text-align: center; }
        input { width: 90%; padding: 10px; margin: 10px; }
        button { padding: 10px 20px; background: #43e97b; border: none; color: white; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Register</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Register</button>
            <p><a href="/login">Back to Login</a></p>
        </form>
    </div>
</body>
</html>
"""

dashboard_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
    <style>
        body { font-family: Arial; background: #f2f2f2; text-align: center; margin-top: 200px; }
        a { text-decoration: none; color: red; }
    </style>
</head>
<body>
    <h1>Welcome {{user}}</h1>
    <h3>Flask App Running Inside Docker</h3>
    <a href="/logout">Logout</a>
</body>
</html>
"""

# Routes
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials"

    return render_template_string(login_page)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (admin, admin123)", (username, password))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template_string(register_page)

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template_string(dashboard_page, user=session['user'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)