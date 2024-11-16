from dotenv import load_dotenv
import os
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'defaultsecret')

@app.route('/')
def home():
    return 'Hello, Flask with .env!'

if __name__ == '__main__':
    app.run(debug=True)
