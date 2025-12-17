from fask import Flask

app = Flask__name__)

@app.route)
def hello():
    return "Hello World, PROJECT 2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
