from flask import Flask, render_template, request
import os

app = Flask(__name__)
embedded_page = os.environ['ESERVICE_URL']

@app.route("/")
def landing_page():
    base_url = request.base_url
    return render_template("landing_page.html", baseUrl=base_url)

@app.route("/not_installed")
def not_installed():
    return render_template("not_installed.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/what_apps_installed")
def check_bundesident():
    return render_template("check_bundesident.html", embedded_page=embedded_page)

@app.route("/check_ausweisapp")
def check_ausweisapp():

    return render_template("check_ausweisapp.html", embedded_page=embedded_page)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)