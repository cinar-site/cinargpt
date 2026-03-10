from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    mesaj = ""
    if request.method == "POST":
        mesaj = request.form["mesaj"]
    return render_template("index.html", mesaj=mesaj)

app.run()