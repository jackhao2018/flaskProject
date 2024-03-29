from flask import Flask
from config import config
from exts import db
from api.page.home.index import bp as home_bp
from api.page.guanyu.about import bp as guanyu_bp
from api.page.jiaocheng.index import bp as jiaocheng_bp
from api.page.yingyin.index import bp as yingyin_bp
from flask_migrate import Migrate
from models.autoUpdataTable import auto_alter_tables
# from flask_script import Manager
from models.fansmodels import FansDetailsModel, FeedbackModel
from models.mediamodels import MediaModel
from models.softwaremodels import SoftwareModel
from models.schedulemodels import SchedulesModel
from models.figureSkatingmodels import FigureSkatingModel
from models.updatemodels import UpdateModel

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)


app.register_blueprint(home_bp)
app.register_blueprint(guanyu_bp)
app.register_blueprint(jiaocheng_bp)
app.register_blueprint(yingyin_bp)

@app.template_test('start_with')
def start_with(matchstr, suffix):
    return matchstr.lower().startswith(suffix.lower())


# 出现上下文报错时用到

@app.route('/111')
def hello_world():
    engine = db.get_engine()
    with engine.connect() as coon:
        result = coon.execute("select 1")
        print(result.fetchone())
    return "hello world"


#新增表时打开
with app.app_context():

    db.init_app(app)
    db.create_all()

auto_alter_tables(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


