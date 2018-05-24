# -*- coding:utf-8 -*-

import requests
import pandas as pd
import time




headers = {

    'authorization':'Bearer 2|1:0|10:1514892674|4:z_c0|92:Mi4xakV3Q0FBQUFBQUFBZ01EZFljMExDaWNBQUFDRUFsVk5ndnB5V2dBdFhlMy1nQi1WbnhMcnIwV0V1R2ZkdGd3YWRR|1f2467b75ec2bf46657e3fe7833b5830119c2dc1d608b732deb295c07e20a426',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

followers = []
def get_followers_data(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/ke-xue-shi-jie-za-zhi/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
        response = requests.get(url, headers=headers).json()['data']
        followers.extend(response)
        print('正在爬取第%s页' % str(i + 1))
        time.sleep(1)

if __name__ == '__main__':
    get_followers_data(10)
    df = pd.DataFrame.from_dict(followers)
    print(df)
    df.to_excel('users.xlsx')