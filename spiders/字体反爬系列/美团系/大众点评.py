import requests
from fontTools.ttLib import TTFont
from scrapy import Selector
import re


headers = {'headers': {'user-agent':
                           'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}}

def main():
    # url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/' \
    #     #       'svgtextcss/fdfd7db3396bd1564ca702c46dd063b3.css'
    #     # r = requests.get(url)
    #     # urls = re.findall('url\("(.+?)"\)', r.text)
    #     # for url in urls:
    #     #     print(url)
    # 暂时取一个为例
    r = requests.get('http:' + '//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/4560818f.woff?#iefix')
    with open('font.woff', 'wb') as f:
        f.write(r.content)
    font = TTFont('font.woff')
    font.saveXML('font.xml')
    # uni_list = font['cmap'].tables[0].ttFont.getGlyphOrder()  # 取出字形保存到uniList中
    # print(uni_list)


if __name__ == '__main__':
    main()