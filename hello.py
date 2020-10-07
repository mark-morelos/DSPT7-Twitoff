from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/new page')
def new_page():
    return 'This is another page!'

# On Mac:
# FLASK_APP=hello.py flask run

# On Windows:
# export FLASK_APP=hello.py (in different terminals may be "set")
# flask run

# If you add this, you can run the flask app as:
# python hello.py
if __name__ == '__main__':
    app.run(debug=True) 