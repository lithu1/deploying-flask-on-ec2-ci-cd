from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h2>Hello from Dr. ViKi DevOps Pipeline!</h2><p>Current Time: {now}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
