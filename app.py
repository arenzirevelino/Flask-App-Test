from flask import Flask, render_template, url_for
from models import HelloWorld
app = Flask(__name__)

@app.route("/")
def main():
    model = HelloWorld()
    return render_template('index.html',model=model)

if __name__ == "__main__":
    app.run()