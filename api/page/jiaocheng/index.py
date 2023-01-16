from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models.softwaremodels import SoftwareModel
import datetime
from exts import db

bp = Blueprint("jiaocheng", __name__, url_prefix="/jiaocheng")

@bp.route("/")
def index():
    page = request.args.get('page')
    downtype = request.args.get('downtype')

    if page is None:
        page = 1

    software_list = []
    if downtype == 'pr':
        data = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + 'Premiere' + '%')).paginate(page=int(page), per_page=12)
    elif downtype == 'ps':
        data = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + 'Photoshop' + '%')).paginate(page=int(page), per_page=12)
    elif downtype == 'ae':
        data = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + 'after' + '%')).paginate(page=int(page), per_page=12)
    elif downtype == 'me':
        data = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + 'media' + '%')).paginate(page=int(page), per_page=12)
    else:
        data = SoftwareModel.query.paginate(page=int(page), per_page=12)

    for software in data.items:
        software_list.append(software.to_dict())

    return render_template('/jiaocheng/index.html', paginate=data, pagedata=software_list)


@bp.route("/search")
def search():
    software_list = []
    page = request.args.get('page')
    text = request.args.get('text')

    data = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + text + '%')).paginate(page=page, per_page=12)

    for software in data.items:
        software_list.append(software.to_dict())

    return render_template('/jiaocheng/index.html', paginate=data, pagedata=software_list)

@bp.route("/pr/<softname>")
def prdownload(softname):
    result = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + softname + '%')).first()
    return render_template('/jiaocheng/software-download.html', result={"downloadTP": "PR下载", 'data': result.to_dict()})


@bp.route("/ps/<softname>")
def psdownload(softname):
    result = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + softname + '%')).first()
    return render_template('/jiaocheng/software-download.html', result={"downloadTP": "PS下载", 'data': result.to_dict()})

@bp.route("/ae/<softname>")
def aedownload(softname):
    result = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + softname + '%')).first()
    return render_template('/jiaocheng/software-download.html', result={"downloadTP": "AE下载", 'data': result.to_dict()})

@bp.route("/me/<softname>")
def medownload(softname):
    result = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + softname + '%')).first()
    return render_template('/jiaocheng/software-download.html', result={"downloadTP": "ME下载", 'data': result.to_dict()})

@bp.route("/c4d")
def c4ddownload():
    return render_template('/jiaocheng/software-download.html', downloadTp={"type": "C4D下载"})
