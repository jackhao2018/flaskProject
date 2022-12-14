import datetime
import os
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, json
from api.func import get_fans_info, viplevel
from logs.base_log import log
from models.fansmodels import FansDetailsModel, FeedbackModel
import time
from exts import db
from forms.about import FeedbackForm
from models.softwaremodels import SoftwareModel
from models.updatemodels import UpdateModel, UpdateChildrenModel
from models.schedulemodels import SchedulesModel
from models.figureSkatingmodels import FigureSkatingModel

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

def upload_conf():
    # if request.method == 'GET':
    menuinfo = UpdateModel.query.all()
    menulist = []
    childrenmunulist = []

    for menu in menuinfo:
        menulist.append(menu.to_dict())

    childrenmunu = UpdateChildrenModel.query.all()

    for children in childrenmunu:
        childrenmunulist.append(children.to_dict())

    return {'menuInfo': menulist, 'childrenmunulist': childrenmunulist}

@bp.route("/upload")
def upload():

    if request.method == 'GET':
        menu = upload_conf()
        print(f"这里是菜单信息：{menu['childrenmunulist']}")
        return render_template('/fankui/upload.html', result={'menu': menu['childrenmunulist']})

@bp.route("/figure_skating", methods=['GET', 'POST'])
def figure_skating():

    if request.method == 'GET':
        pass

        # menu = upload_conf()
        # print(f"这里是菜单信息：{menu['childrenmunulist']}")
        # return render_template('/fankui/upload.html', result={'menu': menu['childrenmunulist']})

    if request.method == 'POST':
        data = request.form

        figureskating = FigureSkatingModel(name=data['name'], rules=data['rules'])

        db.session.add(figureskating)

        db.session.commit()
        return jsonify({"code": "200", "softwareInfo": data})

@bp.route("/software_upload", methods=['GET', 'POST'])
def soft_upload():

    if request.method == 'GET':
        return render_template('/fankui/softupload.html')

    if request.method == 'POST':
        data = request.form
        software_info = SoftwareModel(softName=data['softName'], softDesc=data['details'],softSize=data['softSize'],
                                 softLanguage=data['softwareLanguage'], issue=data['issue'], copyright=data['copyright'], baiduLink=data['baiduLink'],
                                 baiduLinkPwd=data['baiduLinkPwd'], aliyunLink=data['aliyunLink'],
                                 aliyunLinkPwd=data['aliyunLinkPwd'], kuakeLink=data['kuakeLink'],
                                 kuakeLinkPwd=data['kuakeLinkPwd'], install=data['install'], feature=data['features'],
                                 mtime=datetime.datetime.now())

        db.session.add(software_info)

        db.session.commit()
        return jsonify({"code": "200", "softwareInfo": data})

@bp.route('schedule', methods=['GET', 'POST'])
def schedule_upload():

    if request.method == 'POST':
        import datetime
        data = json.loads(json.dumps(request.form))

        schedule = SchedulesModel(title=data['competitionName'], mtime=data['starttime'], endtime=data['endtime'])
        db.session.add(schedule)
        db.session.commit()
        return jsonify({"code": "200", "scheduleInfo": data})


# @bp.route("/json")
if __name__ == '__main__':
    timestamp = 1670947200000

    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    print(dt)



