from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Services2!"  # Change this for service 2 and 3

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
