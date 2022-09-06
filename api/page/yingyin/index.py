from flask import Blueprint, request, jsonify, render_template, redirect, url_for


bp = Blueprint("yingyin", __name__, url_prefix="/media")

@bp.route("/")
def index():

    return render_template('/yingyin/home.html')
