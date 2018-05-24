import requests
from lxml import etree

url = "https://otcbtc.com/"
r = requests.get(url).text

s = etree.HTML(r)
file = s.xpath('//div[@class="row"]/div/table/tr[2]/td/text()')
with open('test.txt','a') as f:
    for i in file:
        f.write(i)
