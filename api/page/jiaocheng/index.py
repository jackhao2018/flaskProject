from flask import Blueprint, request, jsonify, render_template, redirect, url_for


bp = Blueprint("jiaocheng", __name__, url_prefix="/jiaocheng")

@bp.route("/")
def index():

    return render_template('/jiaocheng/index.html')

@bp.route("/pr")
def prdownload():

    return render_template('/jiaocheng/software-download.html', downloadTp={"type": "PR下载"})

@bp.route("/ps")
def psdownload():

    return render_template('/jiaocheng/software-download.html', downloadTp={"type": "PS下载"})

