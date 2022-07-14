from flask import Flask

app = Flask(__name__)
app.config['ENV'] = 'development'

@app.route('/')
def world_cloud():
    with open(r'D:\测试用例数据\textfiles\test-点云.txt', 'r', encoding='utf8') as f:
        word_list = jieba.cut(f.read())
        result = " ".join(word_list)  # 分词用空格隔开

    stylecloud.gen_stylecloud(
        text=result,  # 上面分词的结果作为文本传给text参数
        size=200,
        font_path='msyh.ttc',  # 字体设置
        background_color='black',
        palette='colorbrewer.diverging.Spectral_11',  # 调色方案选取，从palettable里选择
        gradient='horizontal',  # 渐变色方向选了垂直方向
        icon_name='fas fa-circle',  # 蒙版选取，从Font Awesome里选
        output_name='../static/img/ciyun.png')  # 输出词云图
