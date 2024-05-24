from flask import Flask
# WSGI Application
app = Flask(__name__)

@app.route('/')
def hi():
    return "Hello Shakti.hi"

@app.route('/new')
def new():
    return "New Page"

# Debug = True used to dynamically save the changes made in the code.
if __name__ == "__main__":
    app.run(debug=True) 

