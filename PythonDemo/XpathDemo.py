import requests
from lxml import etree

url = "https://otcbtc.com/"
r = requests.get(url).text

s = etree.HTML(r)

print ("-------------")
print(s.xpath('//div[@class="row"]/div/table/tr[2]/td/text()')[0])
print(s.xpath('//div[@class="row"]/div/table/tr[2]/td/text()')[1])
print(s.xpath('//div[@class="row"]/div/table/tr[2]/td/text()')[2])
print(s.xpath('//div[@class="row"]/div/table/tr[2]/td/text()')[3])
print ("-------------")
print(s.xpath('//div[@class="row"]/div/table/tr[3]/td/text()')[0])
print(s.xpath('//div[@class="row"]/div/table/tr[3]/td/text()')[1])
print(s.xpath('//div[@class="row"]/div/table/tr[3]/td/text()')[2])
print(s.xpath('//div[@class="row"]/div/table/tr[3]/td/text()')[3])
print ("-------------")
print(s.xpath('//div[@class="row"]/div/table/tr[4]/td/text()')[0]+s.xpath('//div[@class="row"]/div/table/tr[4]/td/text()')[1]+s.xpath('//div[@class="row"]/div/table/tr[4]/td/text()')[2]+s.xpath('//div[@class="row"]/div/table/tr[4]/td/text()')[3])



eos_url = "http://eoschart.com/?lang=zh"
eosHtml = requests.get(eos_url).text
eosTree = etree.HTML(eosHtml)
print (eosTree.xpath('//div[contains(@class,"panel-body")]/text()'))
# print (eosTree.xpath('//*[@id="distributionSummary"]/tr[14]/td[4]'))
