from flask import Flask
from logs.base_log import log
from flask import render_template

app = Flask(__name__)
app.config['ENV'] = 'development'


@app.route('/')
def index():
    log.info('进入首页')
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
