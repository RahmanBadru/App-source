from flask import Flask , render_template
import os

app = Flask(__name__)
name = os.environ["name"]
environment = os.environ["environment"]

@app.route('/')
def hello_world():
    return render_template('index.html', name=name , environment=environment)

if __name__ == '__main__':
    app.run()