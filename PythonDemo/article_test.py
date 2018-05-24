#!/usr/bin/python
#coding:utf-8

import requests
import time
from lxml import etree
import sys
import os
#60428161 神级高手在都市

path = os.getcwd()
print(path)
def get_articel_info(from_page, page):
	for i in range(page - from_page + 1):
		article_index = i+from_page
		url = 'http://baidu8.ikanshu.cn/book/60428161/{}.html'.format(article_index)
		print(url)
		response = requests.get(url = url).text
		s = etree.HTML(response)

		# article_name = s.xpath('/html/body/div[14]/p/a[4]/span/text()')
		# page_num = s.xpath('//*[@id="lbChapterProcess"]/text()')
		title = s.xpath('//*[@id="lbChapterName"]/text()')
		file = s.xpath('//*[@id="uiContent"]/text()')

		print('获取%s页' % str(i+1))

		file_path = '%s/articel/Chapter-%s.txt' % (path ,str(article_index))
		file_path = 'Chapter-%s.txt' % str(article_index)

		with open(file_path, 'w') as f:
			# for x in article_name:
			# 	print(x)
			# 	f.write(x)
			# for x in page_num:
			# 	print(x)
			# 	f.write(x)
			for x in title:
				print(x)
				f.write(x)
			for x in file:
				f.write(x)
		time.sleep(0.5)


if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8')#解决编码问题UnicodeEncodeError: ‘ascii’ codec can’t encode characters in position
	get_articel_info(1, 1300)



