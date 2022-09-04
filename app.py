from flask import Flask

from config import config
from exts import db
from api.page.home.index import bp as home_bp
from api.page.guanyu.about import bp as guanyu_bp
from flask_migrate import Migrate
from models.fansmodels import FansDetailsModel, FeedbackModel

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

migrate = Migrate(app, db)


app.register_blueprint(home_bp)
app.register_blueprint(guanyu_bp)


# 出现山下文报错时用到

@app.route('/111')
def hello_world():
    # db = SQLAlchemy(app)
    engine = db.get_engine()
    with engine.connect() as coon:
        result = coon.execute("select 1")
        print(result.fetchone())
    return "hello world"


# with app.app_context():
#
#
#     # db.init_app(app)
#     db.create_all()


if __name__ == '__main__':
    # app.debug = True
    #
    app.run(debug=True, port=8888)
    # with app.app_context():
    #     from models.fansmodels import FansDetailsModel
    #     from models.fansmodels import FeedbackModel
    #
    #     db.init_app(app)
    #     db.create_all()

