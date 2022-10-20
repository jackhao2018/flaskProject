from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models.mediamodels import MediaModel
import json


bp = Blueprint("yingyin", __name__, url_prefix="/media")

@bp.route("/")
def index():

    return render_template('/yingyin/home.html')

@bp.route("/img_info")
def get_img_info():
    """获取图片媒体信息"""
    result = MediaModel.query.all()
    img_info_list = [dict(i) for i in result]

    return jsonify({"code": "200", "img_info_list": img_info_list})
