from flask import Blueprint, request, jsonify
from api.func import get_fans_info, viplevel
from logs.base_log import log
from models.fansmodels import FansDetailsModel
import time
from exts import db

bp = Blueprint("guanyu", __name__, url_prefix="/about")


@bp.route("/fans")
def all_fans():
    pass


@bp.route("/upgrade_fans", methods=['POST'])
def upgrade_fans():
    vmid = request.form.get("vmid")
    cookie = request.form.get("cookie")
    # db.get_engine().execute("select * from Bzhan.fans_detail")
    db.get_engine().execute("truncate table fans_detail")
    # fans_list = []
    # fans = []
    # pn = 1
    # while True:
    #     result = get_fans_info(vmid, cookie, pn)
    #
    #     if result['code'] == 0:
    #         log.info('*' * 90 + f'第{pn}页' + "*" * 90)
    #
    #         for user_detail in result['data']['list']:
    #             # fans.append(
    #             #     [user_detail['uname'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user_detail['mtime'])),
    #             #      viplevel(user_detail['vip']['vipType']), user_detail['sign']])
    #             fans_list.append(user_detail['uname'])
    #             fans_info = FansDetailsModel(fans_name=user_detail['uname'],
    #                                          mtime=time.strftime("%Y-%m-%d %H:%M:%S",
    #                                                              time.localtime(user_detail['mtime'])),
    #                                          vip_type=viplevel(user_detail['vip']['vipType']),
    #                                          sign=user_detail['sign'])
    #
    #             db.session.add(fans_info)
    #     else:
    #         break
    #     time.sleep(5)  # 一秒翻页等待
    #     pn += 1
    # print(fans)
    # db.session.commit()
    return "好了"
    # print(xx)
    return jsonify(
        {"fans_list": fans_list, "total": result['data']['total'] if result['code'] == 0 else result['message']})
