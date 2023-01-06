#!/bin/python3
from flask import flash, render_template, request, redirect, url_for
from app.utilities import bp

#####


@bp.route("/", methods=["GET", "POST"])
@bp.route("/home", methods=["GET", "POST"])
def index():
    """
    Landing Page
    """

    if request.method == "POST":
        flash("Post request successful!")
        return redirect(url_for("utilities.index"))

    return render_template("index.html")
