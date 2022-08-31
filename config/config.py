# 设置返回json支持中文
JSON_AS_ASCII = False

# 设置环境
ENV = 'development'

DEBUG = True

SECRET_KEY = "sdfsadfs123123rfj12334343553345"

SQLALCHEMY_TRACK_MODIFICATIONS = True
# static_folder

STATIC_FOLDER = "./static"

#数据库的配置变量
HOSTNAME = '47.107.96.20'
PORT = '3306'
DATABASE = 'Bzhan'
USERNAME = 'root'
PASSWORD = 'haoge666'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

