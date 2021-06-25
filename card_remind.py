#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import requests
import time
import time,datetime
import json

holiday_info = {}
CUR_YEAR = '2021'
WORK_WX_URL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=*************************'

def post_to_wx(content):
    data = {
      "msgtype": "text",
      "text": {
        "content": content,
        "mentioned_list": ["@all"],
       }
    }
    headers = {'Content-Type':'application/object'}
    jdata = json.dumps(data)
    # jdata = bytes(jdata, encoding="uft8")
    rep = requests.post(url=WORK_WX_URL, data=jdata, headers=headers)

# get holiday information
def init_holiday_info():
    global holiday_info
    rep = requests.get('http://tool.bitefu.net/jiari/?d=' + CUR_YEAR)
    info_txt = rep.content.decode()
    holiday_info = json.loads(info_txt)
    # print("holidya_info:" + str(holiday_info))

def check_is_work_day():
    day_info = time.strftime("%m%d", time.localtime(time.time()))
    print(day_info)
    if day_info in holiday_info[CUR_YEAR]:
        return False

    week = datetime.datetime.now().weekday()
    if 0 <= week and 4 >= week:
        post_to_wx('Hi,now is 9:15PM, don`t forget to clock out!')
        print("send successful!")
       
if __name__ == "__main__":
    init_holiday_info()
    check_is_work_day()
    post_to_wx("Hi,now is 9:15PM, don`t forget to clock out!")








