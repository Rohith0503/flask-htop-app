from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get your full name, system username, and current server time in IST
    full_name = "Rohith Adiga T R"
    username = 'rohithadiga19'  # Update to your actual Windows username
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Get the top command output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    return f"""
    <h1>Name: {full_name}</h1>
    <h2>User: {username}</h2>
    <h3>Server Time: {server_time}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')