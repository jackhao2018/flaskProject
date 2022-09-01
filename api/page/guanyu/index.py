from flask import Blueprint, request
from api.func import get_fans_info, viplevel
from logs.base_log import log
from models.fansmodels import FansDetailsModel
import time
from exts import db

bp = Blueprint("guanyu", __name__, url_prefix="/about")

@bp.route("/fans")
def all_fans():
    pass


# def insert_fans(up_mid, fans_mid, uname, sign, viptype, mtime):
#     cursor = db.cursor()
#     sql = 'INSERT INTO fans(up_id,fans_id,fans_name, sign, viplevel, mtime) values(%s, %s, %s, %s, %s, %s)'
#     val = (up_mid, fans_mid, uname, sign, viptype, mtime)
#     try:
#         cursor.execute(sql, val)
#         db.commit()
#     except Exception as e:
#         print(e)
#         db.rollback()
#     db.close()

@bp.route("/upgrade_fans", methods=['POST'])
def upgrade_fans():
    vmid = request.form.get("vmid")
    cookie = request.form.get("cookie")
    pn = 1
    while True:
        result, total = get_fans_info(vmid, cookie, pn)
        log.debug(result)

        if type(result) is list:
            log.info('*' * 90 + f'第{pn}页' + "*" * 90)

            for user_detail in result:

                fans_info = FansDetailsModel(fans_name=user_detail['uname'],
                                             mtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user_detail['mtime'])),
                                             vip_type=viplevel(user_detail['vip']['vipType']),
                                             sign=user_detail['sign'])

                log.info(vmid, user_detail['mid'], user_detail['uname'], user_detail['sign'],
                         user_detail['vip']['vipType'],
                         time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user_detail['mtime'])))
                db.session.add(fans_info)
        else:
            log.info(result, end='\n\n')
            break
        time.sleep(5)  # 一秒翻页等待
        pn += 1

    db.session.commit()
