from flask import Flask, render_template, render_template_string
import subprocess
import datetime
import pytz
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/htop')
def htop():
    # Get the username
    username = os.getenv('USER', os.getenv('USERNAME', 'codespace'))
    
    # Get server time in IST
    ist_tz = pytz.timezone('Asia/Kolkata')
    server_time_ist = datetime.datetime.now(ist_tz).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    
    # Get top output
    top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    
    # Your name - replace with your full name
    your_name = "Harsh Tailor"  # Change this to your full name
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTOP Output</title>
        <style>
            body {
                font-family: monospace;
                margin: 0;
                padding: 10px;
                background-color: #000;
                color: #fff;
            }
            pre {
                white-space: pre-wrap;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <pre>Name: {{ name }}
user: {{ username }}
Server Time (IST): {{ server_time }}
TOP output:
{{ top_output }}</pre>
    </body>
    </html>
    """
    
    return render_template_string(html_template, 
                                 name=your_name,
                                 username=username,
                                 server_time=server_time_ist,
                                 top_output=top_output)

if __name__ == '__main__':
    # Run on port 5000 by default
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)