from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models.softwaremodels import SoftwareModel
import datetime
from exts import db


bp = Blueprint("jiaocheng", __name__, url_prefix="/jiaocheng")

@bp.route("/")
def index():

    result = SoftwareModel.query.all()
    software_list = []
    software_dict = {'name': '', 'url': ''}

    for software in result:
        software_dict['name'] = software['softName']
        software_dict['url'] = software['softURL']
        software_list.append(software_dict)

    return render_template('/jiaocheng/index.html', result={'softwarInfo': software_list, 'total': len(result)})

@bp.route("/pr")
def prdownload():
    result = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + 'Adobe_Premiere_Pro' + '%')).first()
    return render_template('/jiaocheng/software-download.html', result={"downloadTP": "PR下载", 'data': result.to_dict()})

@bp.route("/ps")
def psdownload():
    data = SoftwareModel.query.all()
    result = SoftwareModel.query.filter(SoftwareModel.softName.like('%' + 'photoshop' + '%')).all()

    return render_template('/jiaocheng/software-download.html', downloadTp={"type": "PS下载"})

@bp.route("/ae")
def aedownload():

    return render_template('/jiaocheng/software-download.html', downloadTp={"type": "AE下载"})

@bp.route("/c4d")
def c4ddownload():

    return render_template('/jiaocheng/software-download.html', downloadTp={"type": "C4D下载"})


