from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("landing_page.html")

@app.route("/timeout")
def timeout():
    return render_template("timeout_exec_break.html")

@app.route("/not_installed")
def not_installed():
    return render_template("not_installed.html")

@app.route("/what_apps_installed")
def check_bundesident():
    return render_template("check_bundesident.html")

@app.route("/check_ausweisapp")
def check_ausweisapp():
    return render_template("check_ausweisapp.html")


@app.route("/what_apps_installed/redirect")
def check_bundesident_redirect():
    return render_template("check_bundesident_redirect.html")

@app.route("/check_ausweisapp/redirect")
def check_ausweisapp_redirect():
    return render_template("check_ausweisapp_redirect.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)