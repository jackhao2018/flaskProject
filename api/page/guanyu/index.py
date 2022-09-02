from flask import Blueprint, request, jsonify
from api.func import get_fans_info, viplevel
from logs.base_log import log
from models.fansmodels import FansDetailsModel
import time
from exts import db

bp = Blueprint("guanyu", __name__, url_prefix="/about")


@bp.route("/fans")
def all_fans():
    fans_name_list = []
    result = FansDetailsModel.query.all()
    for fans in result:
        fans_name_list.append(fans.fans_name)
    return jsonify({"code": 200, "fans_name_list": fans_name_list})


# TODO：这里暂时采用的是清库再插入数据的方式，后面需要优化采用比对新旧列表懒删除的方式
@bp.route("/upgrade_fans", methods=['POST'])
def upgrade_fans():
    vmid = request.form.get("vmid")
    cookie = request.form.get("cookie")
    db.get_engine().execute("truncate table fans_detail")
    fans_list = []
    pn = 1
    while True:
        result = get_fans_info(vmid, cookie, pn)

        if result['code'] == 0 and len(result['data']['list']) >= 1:
            log.info('*' * 90 + f'第{pn}页' + "*" * 90)

            for user_detail in result['data']['list']:
                fans_list.append(user_detail['uname'])
                fans_info = FansDetailsModel(fans_name=user_detail['uname'],
                                             mtime=time.strftime("%Y-%m-%d %H:%M:%S",
                                                                 time.localtime(user_detail['mtime'])),
                                             vip_type=viplevel(user_detail['vip']['vipType']),
                                             sign=user_detail['sign'])

                db.session.add(fans_info)
        else:
            break
        time.sleep(5)  # 一秒翻页等待
        pn += 1
    db.session.commit()
    return jsonify(
        {"fans_list": fans_list, "total": result['data']['total']})
