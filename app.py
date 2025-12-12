from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "This is the project created by me Shrest Saha, for my second round of interview in Bees solution PVT LTD"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
