from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("topPage.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/tt")
def tt():
    return render_template("tt.html")

if __name__ == "__main__":
    app.run(debug=True)