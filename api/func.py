import json
import requests
import pymysql
import time
from logs.base_log import log
from exts import db


def get_fans_info(vmid, cookie, pn):
    url = "https://api.bilibili.com/x/relation/followers?vmid={}&pn={}&ps=50&order=desc&order_type=attention&jsonp=jsonp&callback=__jp14"
    # log.info(f'vmid信息：{vmid}, 页码信息：{pn}, cookie数据：{cookie}')
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
    return json_result


def viplevel(vip):
    if vip == 0:
        vip_name = '非会员'
    elif vip == 1:
        vip_name = '大会员'
    else:
        vip_name = '年度大会员'
    return vip_name

def like_details(card_id, cookie, ps=20):
    """ps:20-300"""
    url = "https://api.bilibili.com/x/msgfeed/like_detail?card_id={}&ps={}&pn={}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*',
        "Accept-Encoding": 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        # 'Referer': 'https://message.bilibili.com/',
        'cookie': cookie
    }

    user_list = []
    try:
        i = 1
        while True:
            # print(f'执行{i}页')
            response = requests.get(url.format(card_id, ps, i), headers=headers)
            like_list = json.loads(response.text)['data']['items']

            if json.loads(response.text)['data']['page']['is_end']:
                print(f"此时状态是：{json.loads(response.text)['data']['page']['is_end']}")
                break
            for user in like_list:
                user_list.append(user['user']['nickname'])
            i += 1
    except Exception as e:
        print(e)


    return user_list


if __name__ == '__main__':
    # get_fans_daily()
    cookie = "buvid3=DBD668BD-25FE-44E0-924B-BD27F8F66A95167638infoc; rpdid=|(k||Rll~uRR0J'uYkY~))uJl; LIVE_BUVID=AUTO6216271189171918; video_page_version=v_old_home_18; i-wanna-go-back=-1; blackside_state=0; buvid_fp_plain=undefined; b_ut=5; buvid4=DE900CFE-CD72-6125-C014-32E1E420CA4149283-022012422-p7UKSeFfDyU6EfOCtKxgtg==; nostalgia_conf=-1; CURRENT_BLACKGAP=0; is-2022-channel=1; hit-dyn-v2=1; DedeUserID=484311775; DedeUserID__ckMd5=652915bb543cfc25; buvid_fp=75a15e6c5e984180986f6c22ee2a26c8; _uuid=91A99282-17C7-48A6-8AC1-37AFE399FC1D12402infoc; _ga=GA1.1.1336735845.1650892533; _ga_34B604LFFQ=GS1.1.1661960660.7.1.1661960666.54.0.0; b_nut=100; CURRENT_QUALITY=120; fingerprint3=8576185e4a8d4d2e51572202ab16862d; fingerprint=83863cf8c50ab422f725294f4b752fa6; CURRENT_FNVAL=4048; PVID=1; b_lsid=10D6C7CF7_183F03223A3; SESSDATA=7cb90d39,1681734163,66338*a2; bili_jct=2fbccbba263f4787da3118fe15a87ec8; sid=8ays3gri; bp_video_offset_484311775=718713092988469253"
    # print(get_fans_info(484311775, cookie, 6))
    print(like_details(168578933492, cookie))

