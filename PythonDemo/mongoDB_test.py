#! /usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from pymongo import MongoClient
import time
from fake_useragent import UserAgent

client = MongoClient()
db = client.lagou
lagou = db.PHP #创建PHP集合

headers = {
            'Cookie':'LGUID=20161018180419-3c4bf1aa-951a-11e6-af97-5254005c3644; gr_user_id=7f1ff076-1fce-4d4f-aa23-4e8426b92ef8; user_trace_token=20171018190507-7676f7f2-2012-4447-b199-df01f10fe074; _ga=GA1.2.67830777.1476785059; JSESSIONID=ABAAABAABEEAAJA241F4A1939D6A9D316E4FC1667ADF4C9; X_HTTP_TOKEN=6ed1b2b1ea4fca27ea3d817042ba606c; _gid=GA1.2.1447682625.1515566778; _gat=1; PRE_UTM=; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515566779,1515566779; LGSID=20180110144619-f6d74e00-f5d1-11e7-821a-525400f775ce; PRE_HOST=www.google.co.jp; PRE_SITE=https%3A%2F%2Fwww.google.co.jp%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E6%B7%B1%E5%9C%B3; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515566784; LGRID=20180110144625-fa10b06d-f5d1-11e7-a026-5254005c3644; TG-TRACK-CODE=index_search; SEARCH_ID=79330c3f55034400a82862be78b0a6e5',
            'Referer':'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
        } #对应的headers信息

def get_job_info(page, kd): #加入一个职位参数kd
    for i in range(page):
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
        payload = {
            'first': 'true',
            'pn': i,
            'kd': kd,
        }

        ua = UserAgent() 
        headers['User-Agent'] = ua.random #使用fake-Agent随机生成User-Agent，添加到headers
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            job_json = response.json()['content']['positionResult']['result']
            lagou.insert(job_json)
        else:
            print('Something Wrong!')

        print('正在爬取' + str(i+1) + '页的数据...')
        time.sleep(3)

if __name__ == '__main__':
    get_job_info(3, 'PHP') #爬取前3页的PHP职位信息