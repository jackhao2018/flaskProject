from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models.softwaremodels import SoftwareModel
import datetime
from exts import db


bp = Blueprint("jiaocheng", __name__, url_prefix="/jiaocheng")

@bp.route("/")
def index():

    return render_template('/jiaocheng/index.html')

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
@bp.route("/upload", methods=['GET', 'POST'])
def software_upload():

    if request.method == 'GET':
        return render_template('/jiaocheng/software-upload.html')

    if request.method == 'POST':
        data = request.form
        software_info = SoftwareModel(softName=data['softName'], softDesc=data['details'],softSize=data['softSize'],
                                 issue=data['issue'], copyright=data['copyright'], baiduLink=data['baiduLink'],
                                 baiduLinkPwd=data['baiduLinkPwd'], aliyunLink=data['aliyunLink'],
                                 aliyunLinkPwd=data['aliyunLinkPwd'], kuakeLink=data['kuakeLink'],
                                 kuakeLinkPwd=data['kuakeLinkPwd'], install=data['install'], feature=data['features'],
                                 mtime=datetime.datetime.now())

        db.session.add(software_info)

        db.session.commit()
        return jsonify({"code": "200", "softwareInfo": data})


