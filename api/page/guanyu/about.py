import datetime

from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from api.func import get_fans_info, viplevel
from logs.base_log import log
from models.fansmodels import FansDetailsModel, FeedbackModel
import time
from exts import db
from forms.about import FeedbackForm

bp = Blueprint("guanyu", __name__, url_prefix="/about")


@bp.route("/fans")
def all_fans():
    fans_name_list = []
    result = FansDetailsModel.query.all()
    for fans in result:
        fans_name_list.append(fans.to_dict())
    return jsonify({"code": "200", "fans_name_list": fans_name_list})


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
    return jsonify({"fans_list": fans_list, "total": result['data']['total']})


@bp.route("/")
def about():

    return render_template('/fankui/home.html')


@bp.route('feedback', methods=['POST'])
def feedbacks():
    # print(f'这是请求过来的数据：{request.form}')
    form_data = FeedbackForm(request.form)

    fans_name_list = []
    result = FansDetailsModel.query.all()

    for fans in result:
        fans_name_list.append(fans.to_dict()['fans_name'])

    if form_data.validate():
        username = form_data.username.data
        opinion = form_data.opinion.data
        fans = 1 if username in fans_name_list else 0

        opinions = FeedbackModel(username=username, opinion=opinion, fans=fans, submission_time=datetime.datetime.now())

        db.session.add(opinions)

        db.session.commit()
        return jsonify({'code': 200, 'msg': '提交成功！'})
    else:
        return jsonify({'code': 500, 'msg': '用户名/反馈意见不能为空！'})

