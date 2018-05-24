
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
import requests
from lxml import etree


headers = {
   'authorization':' ', #括号中填上你的authorization
   'User-Agent':' ', #括号中填上你的User-Agent
}


url = "https://otcbtc.com/"
# r = requests.get(url,headers = headers).text #加上header
r = requests.get(url).text

print(r)
s = etree.HTML(r)

file = (s.xpath('//div[@class="row"]/div/table/tr[2]/td/text()'))

indexs = [3,4]
for i in indexs :
    file =file + s.xpath('//div[@class="row"]/div/table/tr[%d]/td/text()' % i)

df = pd.DataFrame(file)
print (df)

df.to_excel('pandas_data.xlsx')




















