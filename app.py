from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from logs.base_log import log
from flask import render_template
from api.page.home.index import bp as home_bp

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(home_bp)

#数据库的配置变量
HOSTNAME = '47.107.96.20'
PORT = '3306'
DATABASE = 'Bzhan'
USERNAME = 'root'
PASSWORD = 'haoge666'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD , HOSTNAME, PORT, DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)

@app.route('/ceshi')
def test():
    # 写一个测试代码来验证是否连接成功
    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute("select 1")
        print(result.fetchone())
    return 'Hello World! '


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True, port=8888)
