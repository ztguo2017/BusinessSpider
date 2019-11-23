# get完事
import pretty_request


def main():
    url = 'https://category.vip.com/suggest.php?keyword=%E7%BE%8E%E9%A3%9F&ff=235|12|1|1'
    for i in range(20):
        r = (pretty_request.get('https://detail.vip.com/detail-3305526-701977195.html').text)
        print(r)


if __name__ == '__main__':
    main()