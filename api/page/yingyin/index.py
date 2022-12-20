from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models.mediamodels import MediaModel
from models.fansmodels import FansDetailsModel
import json


bp = Blueprint("yingyin", __name__, url_prefix="/yingyin")

@bp.route("/")
def index():
    fans_name_list = []
    result = FansDetailsModel.query.all()
    for fans in result:
        fans = fans.to_dict()
        fans_name_list.append(fans['fans_name'])

    # print(fans_name_list)
    return render_template('/test2.html', result={'fans_list': fans_name_list})

@bp.route("/img_info")
def get_img_info():
    """获取图片媒体信息"""
    result = MediaModel.query.all()
    img_info_list = [dict(i) for i in result]

    return jsonify({"code": "200", "img_info_list": img_info_list})
