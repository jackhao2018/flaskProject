import json
import requests
import pymysql
import time
from logs.base_log import log
from exts import db


def get_fans_info(vmid, cookie, pn):
    url = "https://api.bilibili.com/x/relation/followers?vmid={}&pn={}&ps=50&order=desc&order_type=attention&jsonp=jsonp&callback=__jp14"
    log.info(f'vmid信息：{vmid}, 页码信息：{pn}, cookie数据：{cookie}')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Referer': 'https://space.bilibili.com/484311775/fans/fans',
        'cookie': cookie
    }
    proxy = ['202.55.5.209', '103.37.141.69', '113.88.208.112', '112.6.117.135', '183.64.239.19', '47.105.91.226', '188.131.233.175', '117.34.25.11', '47.113.90.161', '47.100.255.35', '106.54.128.253', '122.9.101.6', '152.136.62.181', '112.14.47.6', '118.163.120.181', '183.247.199.114', '58.215.201.98', '47.106.105.236', '27.42.168.46', '113.254.249.138', '106.15.197.250', '61.216.185.88', '111.3.118.247', '106.55.15.244', '14.215.212.37', '183.247.215.218', '121.13.252.58']
    i = 0
    while True:
        if i < len(proxy):
            proxies = {
                'https://': proxy[i]
            }
            response = requests.get(url.format(vmid, pn), proxies=proxies, headers=headers)
            if response.status_code == 200:
                break
            i = i + 1
        if i + 1 == len(proxy):
            print("IP 全部失效")
            break

    json_result = json.loads(response.text[7: -1])  # 返回json格式
    log.info(f'当页粉丝结果：{json_result}')
    if len(json_result['data']['list']) >= 1:
        return json_result['data']['list'], json_result['data']['total']
    else:
        return '已经翻页到最后一页了。 总计：{}位粉丝，加油 UP！！！'.format(json_result['data']['total']), json_result['data']['total']

def viplevel(vip):
    if vip == 0:
        vip_name = '非会员'
    elif vip == 1:
        vip_name = '大会员'
    else:
        vip_name = '年度大会员'
    return vip_name

def insert_fans(up_mid, fans_mid, uname, sign, viptype, mtime):
    cursor = db.cursor()
    sql = 'INSERT INTO fans(up_id,fans_id,fans_name, sign, viplevel, mtime) values(%s, %s, %s, %s, %s, %s)'
    val = (up_mid, fans_mid, uname, sign, viptype, mtime)
    try:
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()

def get_fans_daily(vmid, cookie, pn=1):
    fans_list = []
    while True:
        result, total = get_fans_info(vmid, pn, cookie)

        if type(result) is list:
            log.info('*' * 90 + f'第{pn}页' + "*" * 90)

            for user_detail in result:
                # print(user_detail)
                # time.sleep(3)  # 每个用户之间间隔一秒查询
                # user_detail = get_user_details(info['mid'])
                # fans_list.append(user_detail['uname']) 账户等级：{}, 性别：{},,
                # print(
                #     "粉丝昵称：{}, 关注时间：{},  会员类型：{}, 头像是：{}, \n签名：{}\n".format(
                #         user_detail['uname'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user_detail['mtime'])),
                #         # user_detail["data"]['level'], user_detail["data"]['sex'],
                #         viplevel(user_detail['vip']['vipType']), user_detail['face'], user_detail['sign']))

                insert_fans(vmid, user_detail['mid'], user_detail['uname'], 'NULL' if len(user_detail['sign']) == 0 else user_detail['sign'], viplevel(user_detail['vip']['vipType']), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user_detail['mtime'])))
                log.info(vmid, user_detail['mid'], user_detail['uname'], user_detail['sign'], user_detail['vip']['vipType'], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user_detail['mtime'])))
        else:
            print(result, end='\n\n')
            break
        time.sleep(5)  # 一秒翻页等待
        pn += 1
    return fans_list


if __name__ == '__main__':
    get_fans_daily(484311775, 1, _COOKIE)
