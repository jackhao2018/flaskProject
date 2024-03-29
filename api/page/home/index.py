from models.schedulemodels import SchedulesModel
from flask import Blueprint, request, render_template, jsonify
from models.figureSkatingmodels import FigureSkatingModel
# import jieba
# from flask import Blueprint,render_template,request,g,redirect,url_for,flash
# from stylecloud import stylecloud
# from config.base_config import BASE_DIR

bp = Blueprint('home', __name__, url_prefix="/")


# @bp.route('')
# def world_cloud():
#     with open(rf'{BASE_DIR}\static\test.txt', 'r', encoding='utf8') as f:
#         word_list = jieba.cut(f.read())
#         result = " ".join(word_list)  # 分词用空格隔开
#
#     stylecloud.gen_stylecloud(
#         text=result,  # 上面分词的结果作为文本传给text参数
#         size=200,
#         font_path='msyh.ttc',  # 字体设置
#         background_color='black',
#         palette='colorbrewer.diverging.Spectral_11',  # 调色方案选取，从palettable里选择
#         gradient='horizontal',  # 渐变色方向选了垂直方向
#         icon_name='fas fa-circle',  # 蒙版选取，从Font Awesome里选
#         output_name=f'{BASE_DIR}/static/img/ciyun.png')  # 输出词云图
#     return render_template('index.html', data='45')

@bp.route('')
def index():
    schedule_list = []
    schedules = SchedulesModel.query.order_by(SchedulesModel.mtime.asc()).all()
    for schedule in schedules:
        schedule_list.append(schedule.to_dict())

    figureskate_list = []
    figureskatings = FigureSkatingModel.query.order_by(FigureSkatingModel.id.desc()).all()
    for figureskate in figureskatings:
        figureskate_list.append(figureskate.to_dict())

    # print({'data': figureskate_list})
    # return jsonify({'data': figureskate_list, 'schedule_list': schedule_list})

    return render_template('index.html', result={'data': figureskate_list, 'schedule_list': schedule_list})

# @bp.route('/aliyun')
# def zhibo():
#     return render_template('aliyunplay.html')

# @bp.route("/search")
# def search():
#     # /search?q=xxx
#     q = request.args.get("put")
#     # filter_by：直接使用字段的名称
#     # filter：使用模型.字段名称
#     # questions =QuestionModel.query.filter(or_(QuestionModel.title.contains(q),QuestionModel.content.contains(q))).order_by(db.text("-create_time"))
#     # return render_template("index.html", data=q)
#     return {f"你搜索的内容是：{q}"}
