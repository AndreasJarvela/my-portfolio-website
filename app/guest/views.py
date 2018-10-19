from flask import render_template
from . import guest

@guest.route("/")
@guest.route("/home")
def main():
    return render_template("guest/main.html")


@guest.route("/lol")
def lol():
    return render_template("guest/lol.html")