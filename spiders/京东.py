# 每页60条，后面30页需ajax加载出来

from scrapy import Selector

import pretty_request


def main(page):
    for i in range(1, page + 1):
        url = 'https://search.jd.com/s_new.php?keyword=%E7%BE%8E%E9%A3%9F&enc=utf-8&page={}&scrolling=y&s=31'.format(i) \
            if i % 2 == 0 else 'https://search.jd.com/Search?keyword=%E7%BE%8E%E9%A3%9F&enc=utf-8&page={}'.format(i)

        headers = {'referer': 'https://search.jd.com/Search?keyword=%E7%BE%8E%E9%A3%9F&enc=utf-8&page={}'.format(i)} \
            if i % 2 == 0 else {}
        r = pretty_request.get(url, headers=headers)
        html = Selector(text=r.text)
        # divs = html.xpath('//li[@class="gl-item"]/@data-sku').extract()


if __name__ == '__main__':
    main(5)
