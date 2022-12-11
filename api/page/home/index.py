import jieba
# from flask import Blueprint,render_template,request,g,redirect,url_for,flash
from flask import Blueprint, request, render_template
from stylecloud import stylecloud
from config.base_config import BASE_DIR
from models.schedulemodels import SchedulesModel

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

x = """
<div class="news-item__content js-mediator-article"><p class="text" _msthash="3655873" _msttexthash="366432209">11月23日至27日，彼尔姆将举办俄罗斯花样滑冰大奖赛第六赛“为彼尔姆地区总督颁奖”。</p>
<p class="text" _msthash="3655990" _msttexthash="34898981">成人比赛第二天结果</p>
<p class="text"><strong _msthash="3656107" _msttexthash="7116512">十一月 27</strong></p>
<p class="text"><strong _msthash="3656224" _msttexthash="52615290">11：00 – 冰舞，自由舞</strong></p>
<ol>
<li _msthash="4224077" _msttexthash="81651336">索菲亚秋秋尼娜 – 安德烈·巴金 – 119，38</li>
<li _msthash="4224207" _msttexthash="109237245">伊丽莎白·帕塞奇尼克 – 马克西姆·涅克拉索夫 – 113.90</li>
<li _msthash="4224337" _msttexthash="146308656">亚历山德拉·克拉夫琴科 – 亚历山大·舒斯蒂茨基 – 102，83</li>
<li _msthash="4224467" _msttexthash="146518619">亚历山德拉·普罗科佩茨 – 亚历山大·瓦斯科维奇 – 100，66</li>
<li _msthash="4224597" _msttexthash="96547347">波琳娜·乌索娃 – 米哈伊尔·安东诺夫 – 98，94</li>
<li _msthash="4224727" _msttexthash="108347772">弗拉达·帕夫莱尼娜 – 亚历山大·阿列克萨尼扬 – 91.23</li>
<li _msthash="4224857" _msttexthash="163169643">瓦尔瓦拉·日丹诺娃 – 帖木尔·巴巴耶夫-斯米尔诺夫 – 90，39</li>
<li _msthash="4224987" _msttexthash="100417798">索菲亚·卡尔塔绍娃 – 伊利亚·卡尔波夫 – 87，77</li>
<li _msthash="4225117" _msttexthash="102359556">叶卡捷琳娜·赫拉布里赫 – 米龙·苏斯洛夫 – 85.76</li>
<li _msthash="4317755" _msttexthash="97757582">雅娜·特鲁比诺娃 – 弗拉迪斯拉夫·舍夫宁 – 69.79</li>
</ol>
<p _msthash="3656458" _msttexthash="19457516">舞侣最终排名</p>
<ol>
<li _msthash="4224468" _msttexthash="81647475">索菲亚秋秋尼娜 – 安德烈·巴金 – 200，26</li>
<li _msthash="4224598" _msttexthash="136384508">伊丽莎白·帕塞奇尼克 – 马克西姆·涅克拉索夫 – 192，95</li>
<li _msthash="4224728" _msttexthash="146306186">亚历山德拉·克拉夫琴科 – 亚历山大·舒斯蒂茨基 – 170，10</li>
<li _msthash="4224858" _msttexthash="97410248">波琳娜·乌索娃 – 米哈伊尔·安东诺夫 – 165，24</li>
<li _msthash="4224988" _msttexthash="157578291">亚历山德拉·普罗科佩茨 – 奥列克桑德·瓦斯科维奇 – 162，80</li>
<li _msthash="4225118" _msttexthash="164043945">瓦尔瓦拉·日丹诺娃 – 帖木尔·巴巴耶夫-斯米尔诺夫 – 155，88</li>
<li _msthash="4225247" _msttexthash="97638944">弗拉达·帕夫莱尼娜 – 亚历山大·阿列克桑扬 – 153.99</li>
<li _msthash="4225377" _msttexthash="102375117">叶卡捷琳娜·赫拉布里赫 – 米龙·苏斯洛夫 – 142.61</li>
<li _msthash="4225507" _msttexthash="101284027">索菲亚·卡尔塔绍娃 – 伊利亚·卡尔波夫 – 141，99</li>
<li _msthash="4318171" _msttexthash="97770205">雅娜·特鲁比诺娃 – 弗拉迪斯拉夫·舍夫宁 – 110.36</li>
</ol>
<p class="text"><strong _msthash="3656692" _msttexthash="36065146">12：45 – 女子自由滑</strong></p>
<ol>
<li _msthash="4224859" _msttexthash="43174586">伊丽莎白·图克塔米舍娃 – 161.20</li>
<li _msthash="4224989" _msttexthash="51937366">索菲亚·穆拉维耶娃 – 157，56</li>
<li _msthash="4225119" _msttexthash="29564210">阿丽娜·戈尔巴乔娃 – 145.43</li>
<li _msthash="4225248" _msttexthash="49621065">克塞尼亚·西尼琴纳 – 136，73</li>
<li _msthash="4225378" _msttexthash="37461918">安娜·弗罗洛娃 – 124，74</li>
<li _msthash="4225508" _msttexthash="37259625">维多利亚·费迪亚尼娜 – 124.48</li>
<li _msthash="4225637" _msttexthash="64778974">叶卡捷琳娜·阿尼西莫娃 – 120，16</li>
<li _msthash="4225767" _msttexthash="54277990">维多利亚·内斯特罗娃 – 119，14</li>
<li _msthash="4225897" _msttexthash="50858236">维罗妮卡·马利舍娃 – 115，92</li>
<li _msthash="4318587" _msttexthash="46585617">克塞尼亚·戈沃洛娃 – 103，91</li>
<li _msthash="4318730" _msttexthash="60418384">叶卡捷琳娜·斯库尔金娜 – 86，62</li>
</ol>
<p _msthash="3656926" _msttexthash="18820971">女子最终排名</p>
<ol>
<li _msthash="4314947" _msttexthash="61839934">伊丽莎白·图克塔米舍娃 – 239，94</li>
<li _msthash="4315077" _msttexthash="51936235">索菲亚·穆拉维耶娃 – 239，15</li>
<li _msthash="4315207" _msttexthash="46528404">阿丽娜·戈尔巴乔娃 – 210，86</li>
<li _msthash="4315337" _msttexthash="49621702">克塞尼亚·西尼琴纳 – 207，67</li>
<li _msthash="4315467" _msttexthash="55071315">维多利亚·费迪亚尼娜 – 189，10</li>
<li _msthash="4315597" _msttexthash="37461658">安娜·弗罗洛娃 – 183，60</li>
<li _msthash="4315727" _msttexthash="64779260">叶卡捷琳娜·阿尼西莫娃 – 180，30</li>
<li _msthash="4315857" _msttexthash="54699528">维多利亚·涅斯捷罗娃 – 179，90</li>
<li _msthash="4315987" _msttexthash="50857924">维罗妮卡·马利舍娃 – 170，27</li>
<li _msthash="4409210" _msttexthash="46587151">克塞尼亚·戈沃洛娃 – 161，57</li>
<li _msthash="4409353" _msttexthash="61283508">叶卡捷琳娜·斯库尔金娜 – 137，88</li>
</ol>
<p class="text"><strong _msthash="3743831" _msttexthash="56729426">14：45 – 双人滑，自由滑</strong></p>
<ol>
<li _msthash="4315363" _msttexthash="130139555">阿纳斯塔西娅·米希娜 – 亚历山大·加利亚莫夫 – 156，75</li>
<li _msthash="4315493" _msttexthash="131363791">叶卡捷琳娜·奇克马列娃 – 马特维·扬琴科夫 – 135，53</li>
<li _msthash="4315623" _msttexthash="144508117">阿纳斯塔西娅·穆霍托娃——德米特里·叶夫根尼耶夫——128.87</li>
<li _msthash="4315753" _msttexthash="109604144">伊丽莎白·奥索金娜 – 阿尔乔姆·格里萨延科 – 116.93</li>
<li _msthash="4315883" _msttexthash="101540075">泰西亚·索比尼娜 – 伊利亚·米罗诺夫 – 114，72</li>
<li _msthash="4316013" _msttexthash="82706221">瓦尔瓦拉·切雷姆尼赫 – 丹尼尔·布坚科 – 114.39</li>
<li _msthash="4316143" _msttexthash="116262029">玛丽亚·迪布科娃 – 阿列克谢·赫瓦尔科 – 113，16</li>
<li _msthash="4316273" _msttexthash="88600200">玛雅·谢盖 – 伊戈尔·沙姆舒罗夫 – 112，55</li>
</ol>
<p _msthash="3744091" _msttexthash="18680649">情侣最终排名</p>
<ol>
<li _msthash="4315779" _msttexthash="102993293">阿纳斯塔西娅·米希娜 – 亚历山大·加利亚莫夫 – 237.30</li>
<li _msthash="4315909" _msttexthash="131363856">叶卡捷琳娜·奇克马列娃 – 马特维·扬琴科夫 – 205，73</li>
<li _msthash="4316039" _msttexthash="164225425">阿纳斯塔西娅·穆霍托娃 – 德米特里·叶夫根尼耶夫 – 202，43</li>
<li _msthash="4316169" _msttexthash="109603091">伊丽莎白·奥索金娜 – 阿尔乔姆·格里萨延科 – 184.23</li>
<li _msthash="4316299" _msttexthash="82705155">瓦尔瓦拉·切雷姆尼赫 – 丹尼尔·布坚科 – 181.42</li>
<li _msthash="4316429" _msttexthash="116264928">玛丽亚·迪布科娃 – 阿列克谢·赫瓦尔科 – 172，55</li>
<li _msthash="4316559" _msttexthash="88603177">玛雅·谢盖 – 伊戈尔·沙姆舒罗夫 – 172，49</li>
<li _msthash="4316689" _msttexthash="101540855">泰西亚·索比尼娜 – 伊利亚·米罗诺夫 – 169，20</li>
</ol>
<p class="text"><strong _msthash="3744351" _msttexthash="37266424">16：15 – 男子自由滑</strong></p>
<ol>
<li _msthash="4316195" _msttexthash="49898628">叶夫根尼·谢梅年科 – 189，63</li>
<li _msthash="4316325" _msttexthash="49278840">伊利亚·雅布洛科夫 – 170，89</li>
<li _msthash="4316455" _msttexthash="31294250">阿尔乔姆·科瓦列夫 – 164.41</li>
<li _msthash="4316585" _msttexthash="48919871">马卡尔·伊格纳托夫 – 158，80</li>
<li _msthash="4316715" _msttexthash="52062842">阿列克谢·埃罗霍夫 – 149，51</li>
<li _msthash="4316845" _msttexthash="51044890">马特维·维特鲁金 – 145，42</li>
<li _msthash="4316975" _msttexthash="37557286">丹尼尔·波斯塔纳科夫 – 128.75</li>
<li _msthash="4317105" _msttexthash="46164495">叶戈尔·科瓦连科 – 128，21</li>
<li _msthash="4317235" _msttexthash="46457931">弗拉基米尔·奥什切普科夫 – 126.28</li>
<li _msthash="4410536" _msttexthash="55699774">阿尔乔姆·阿列尼科夫 – 125，89</li>
<li _msthash="4410679" _msttexthash="39649116">弗拉基米尔·库兹涅佐夫 – 117.40</li>
<li _msthash="4410822" _msttexthash="46418918">马克西姆·瓦拉金 – 115，33</li>
</ol>
<p _msthash="3744611" _msttexthash="19467799">男子最终排名</p>
<ol>
<li _msthash="4316611" _msttexthash="49899889">叶夫根尼·谢梅年科 – 292，99</li>
<li _msthash="4316741" _msttexthash="32311643">伊利亚·雅布洛科夫 – 264.20</li>
<li _msthash="4316871" _msttexthash="31293444">阿尔乔姆·科瓦列夫 – 245.02</li>
<li _msthash="4317001" _msttexthash="52060775">阿列克谢·埃罗霍夫 – 243，12</li>
<li _msthash="4317131" _msttexthash="46279870">马卡尔伊格纳托夫 – 241，71</li>
<li _msthash="4317261" _msttexthash="51045488">马特维·维特鲁金 – 232，83</li>
<li _msthash="4317391" _msttexthash="65967291">弗拉基米尔·奥什切普科夫 – 191，29</li>
<li _msthash="4317521" _msttexthash="46164677">叶戈尔·科瓦连科 – 190，50</li>
<li _msthash="4317651" _msttexthash="55696615">阿尔乔姆·阿列尼科夫 – 184，02</li>
<li _msthash="4410978" _msttexthash="37557247">丹尼尔·波斯塔纳科夫 – 181.76</li>
<li _msthash="4411121" _msttexthash="30303195">马克西姆·瓦拉金 – 174.02</li>
<li _msthash="4411264" _msttexthash="58311253">弗拉基米尔·库兹涅佐夫 – 170，83</li>
</ol>
<p class="text">&nbsp;</p>
<p class="text" _msthash="3743818" _msttexthash="53349413">比赛的开始时间是莫斯科。</p></div>
"""

y = """
<p _msthash="3744338" _msttexthash="58726148">10. 伊丽莎白·安东诺娃 – 83，67</p>
<p><strong _msthash="3744468" _msttexthash="9830613">短节目</strong></p>
<p _msthash="3744598" _msttexthash="49455627">1. 柳博芙·鲁布佐娃 – 67，72</p>
<p _msthash="3744728" _msttexthash="43624659">2. 埃琳娜·采涅娃 – 54，99</p>
<p _msthash="3744858" _msttexthash="43801537">3. 玛丽亚·马祖尔 – 54，98</p>
<p _msthash="3744988" _msttexthash="41078180">4. 阿丽娜·库拉克 – 52，40</p>
<p _msthash="3743935" _msttexthash="85573020">5. 阿纳斯塔西娅·列斯尼茨卡娅 – 51，52</p>
<p _msthash="3744065" _msttexthash="46881653">6. 玛丽亚·米斯尼克 – 50，47</p>
<p _msthash="3744195" _msttexthash="51788620">7. 娜塔莉亚·什梅列娃 – 48，83</p>
<p _msthash="3744325" _msttexthash="57306678">8. 阿里娜·里亚比切娃 – 48，54</p>
<p _msthash="3744455" _msttexthash="55074513">9. 伊丽莎白·安东诺娃 – 47，38</p>
<p _msthash="3744585" _msttexthash="53933295">10. 奥尔加·诺维科娃 – 44，92</p></div>
"""


@bp.route('')
def index():
    schedule_list = []
    schedules = SchedulesModel.query.all()
    for schedule in schedules:
        schedule_list.append(schedule.to_dict())
    return render_template('index.html', result={'schedule': x, 'rules': y, 'schedule_list': schedule_list})

@bp.route('/aliyun')
def zhibo():
    return render_template('aliyunplay.html')

@bp.route("/search")
def search():
    # /search?q=xxx
    q = request.args.get("put")
    # filter_by：直接使用字段的名称
    # filter：使用模型.字段名称
    # questions =QuestionModel.query.filter(or_(QuestionModel.title.contains(q),QuestionModel.content.contains(q))).order_by(db.text("-create_time"))
    # return render_template("index.html", data=q)
    return {f"你搜索的内容是：{q}"}



