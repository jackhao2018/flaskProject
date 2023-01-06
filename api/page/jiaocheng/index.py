from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models.softwaremodels import SoftwareModel
import datetime
from exts import db


bp = Blueprint("jiaocheng", __name__, url_prefix="/jiaocheng")

@bp.route("/")
def index():
    downtype = request.args.get('downtype')
    software_list = []
    # print(downtype)
    if downtype == 'pr':
        result = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + 'Premiere' + '%')).all()
    elif downtype == 'ps':
        result = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + 'Photoshop' + '%')).all()
    else:
        result = SoftwareModel.query.all()

    for software in result:
        software_list.append(software.to_dict())
    return render_template('/jiaocheng/index.html', result={'softwarInfo': software_list, 'total': len(result)})

@bp.route("/pr/<softname>")
def prdownload(softname):
    result = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + softname + '%')).first()
    return render_template('/jiaocheng/software-download.html', result={"downloadTP": "PR下载", 'data': result.to_dict()})

@bp.route("/ps/<softname>")
def psdownload(softname):
    result = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + softname + '%')).first()
    return render_template('/jiaocheng/software-download.html', result={"downloadTP": "PS下载", 'data': result.to_dict()})

@bp.route("/ae")
def aedownload():

    return render_template('/jiaocheng/software-download.html', downloadTp={"type": "AE下载"})

@bp.route("/c4d")
def c4ddownload():

    return render_template('/jiaocheng/software-download.html', downloadTp={"type": "C4D下载"})


