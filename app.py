from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from logs.base_log import log
from flask import render_template
from api.page.home.index import bp as home_bp
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(home_bp)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
# @app.route('/ceshi')
# def test():
#     # 写一个测试代码来验证是否连接成功
#     engine = db.get_engine()
#     with engine.connect() as conn:
#         result = conn.execute("select 1")
#         print(result.fetchone())
#     return 'Hello World! '


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True, port=8888)
