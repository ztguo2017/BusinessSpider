# h5页面 , js 29191123
# 批量搜索大概需要登录
import re

import execjs
import requests

url = 'https://mobile.yangkeduo.com'
url1 = 'https://mobile.yangkeduo.com/search_result.html?search_key=%E7%BE%8E%E9%A3%9F'

headers = {'headers': {'user-agent':
                           'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}}


def get_anticont(url):
    with open('anti_content.js', 'r') as f:
        js = ''.join(f.readlines())
    result = execjs.compile(js).call('get_anticontent', url)
    return result


def main():
    s = requests.session()
    s.get(url, **headers)
    s.get('https://mobile.yangkeduo.com/rpt_report.html?tp=1', **headers)
    r = s.get(url1, **headers)
    url2 = 'https://mobile.yangkeduo.com/proxy/api/search?source=search&search_met=history&' \
           'list_id={list_id}' \
           '&sort=default&filter=&q=%E7%BE%8E%E9%A3%9F&page={page}&size=50&' \
           'flip={flip}&' \
           'anti_content={anti_content}'
    list_id, flip = re.search('listID":"(.+?)".+?flip":"(.+?)"', r.text, flags=re.S).groups()
    url2 = url2.format(list_id=list_id, page=1, flip=flip, anti_content=get_anticont(url1))
    print(url2)


if __name__ == '__main__':
    main()
