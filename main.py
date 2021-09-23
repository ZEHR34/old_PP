from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello world</h1>"

@app.route("/api/v1/hello-world-1")
def task():
    return "<h1>hello student</h1>"

if __name__ == "__main__":
    app.run()
