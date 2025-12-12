from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi this is my project for the second round of interview in Bees solution PVT LTD"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
