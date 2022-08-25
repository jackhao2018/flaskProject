import jieba
import stylecloud




def ciyun():
    with open(r'E:\Program Files (x86)\SogouInput\11.6.0.5419\crash\errorlog.txt', 'r', encoding='utf8') as f:
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


def main():
    ciyun()


if __name__ == '__main__':
    main()