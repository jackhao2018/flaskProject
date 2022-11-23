from flask import Blueprint, request, jsonify, render_template, redirect, url_for


bp = Blueprint("jiaocheng", __name__, url_prefix="/jiaocheng")

@bp.route("/")
def index():

    return render_template('/jiaocheng/index.html')

@bp.route("/")
def index():

    return render_template('/jiaocheng/index.html')

