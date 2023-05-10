from flask import Flask, render_template, request
import os

app = Flask(__name__)
allowed_page = os.environ['ESERVICE_URL']

@app.route("/")
def landing_page():
    return render_template("landing_page.html")

@app.route("/not_installed")
def not_installed():
    return render_template("not_installed.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/what_apps_installed")
def check_bundesident():
    embedded_page = request.args.get("embeddedPages")
    if embedded_page != allowed_page:
        embedded_page = " "

    return render_template("check_bundesident.html", embedded_page=embedded_page)

@app.route("/check_ausweisapp")
def check_ausweisapp():
    embedded_page = request.args.get("embeddedPages")
    if embedded_page != allowed_page:
        embedded_page = " "

    return render_template("check_ausweisapp.html", embedded_page=embedded_page)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)