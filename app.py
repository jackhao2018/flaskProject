from flask import Flask
from config import config
from exts import db
from api.page.home.index import bp as home_bp
from api.page.guanyu.index import bp as guanyu_bp
from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(config)


db.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(home_bp)
app.register_blueprint(guanyu_bp)


# 出现山下文报错时用到
with app.app_context():
    # from models.fansmodels import FansDetailsModel
    db.init_app(app)
    db.create_all()

@app.route('/111')
def hello_world():
    # db = SQLAlchemy(app)
    engine = db.get_engine()
    with engine.connect() as coon:
        result = coon.execute("select 1")
        print(result.fetchone())
    return "hello world"


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True, port=8888)
