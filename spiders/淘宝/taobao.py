if __name__ == '__main__':
    import requests
    headers ={
        'user-agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Cookie': 'uc1=pas=0&tag=8&cookie15=UIHiLt3xD8xYTw%3D%3D&cookie21=VFC%2FuZ9ajC0X15Rzt0LhxQ%3D%3D&existShop=false&cookie14=UoTbmVUxFxZULw%3D%3D&lng=zh_CN&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D;unb=1841624642;_uab_collina=157458817702466643306776;cna=ajxhFofBdXsCAWVULmCi964P;cookie2=10ae0f2522446c8d1e45f001ebee4268;_tb_token_=61b53e6b766f;t=c87a2047a67d7806acb04bec146b2b99;v=0;uc3=vt3=F8dByuQCIlwPcflv8jk%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&nk2=r7k3AWnfrfHphk538FKW&id2=UonfNiL40%2BeeSw%3D%3D;log=lty=Ug%3D%3D;csg=59263ead;lgc=%5Cu5929%5Cu6DAF%5Cu6D6A%5Cu5B502013101;uc4=nk4=0%40rVtNc5sBAk96adc%2Ftyefcj3g%2F%2Boogd8NUfE%3D&id4=0%40UOE1hWOBbAWYouxY%2FOnUA5z2QOee;cookie17=UonfNiL40%2BeeSw%3D%3D;dnk=%5Cu5929%5Cu6DAF%5Cu6D6A%5Cu5B502013101;skt=99ecb5e9d50a9e3b;existShop=MTU3NDU4ODAyMg%3D%3D;tracknick=%5Cu5929%5Cu6DAF%5Cu6D6A%5Cu5B502013101;l=dBNFe7DIqVGA0wTkBOCanurza77OSIRYYuPzaNbMi_5gy6T1ng-1kdW5HF96VjWftRTB42FvhwJ9-etkZrLunQSpXUJ_fDc.;lc=Vyu9LoTYStqR3%2Bd037GzLZZ6lfQ%3D;_cc_=URm48syIZQ%3D%3D;lid=%E5%A4%A9%E6%B6%AF%E6%B5%AA%E5%AD%902013101;tg=0;_l_g_=Ug%3D%3D;sg=125;_nk_=%5Cu5929%5Cu6DAF%5Cu6D6A%5Cu5B502013101;cookie1=W8zL9ezuijcuSvPE4ixvCd96pnadgeoMgsVzfhdD2Q8%3D;isg=BFVVgJkhpE4Mq4AyCLlyabK3ZFHP-iIvknpTJdf6EUwbLnUgn6IZNGPs_HI9NSEc;'}
    url = 'https://s.taobao.com/search?q=%E7%BE%8E%E9%A3%9F&s=44' # mod = 44
    # url = 'https://s.taobao.com/search?data-key=s&data-value=264&ajax=true&_ksTS=1574591734575_744&callback=jsonp745&q=%E7%BE%8E%E9%A3%9F&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191124&ie=utf8&bcoffset=-9&ntoffset=-3&p4ppushleft=1%2C48&s=176'
    r = requests.get(url, headers=headers)
    print(r.text)

    '''
  data-key: s
data-value: 88
ajax: true
_ksTS: 1574591102790_938
callback: jsonp939
q: 美食
imgfile: 
js: 1
stats_click: search_radio_all:1
initiative_id: staobaoz_20191124
ie: utf8
bcoffset: 0
ntoffset: 6
p4ppushleft: 1,48
s: 44  
    
    
data-key: s
data-value: 132
ajax: true
_ksTS: 1574591138820_1089
callback: jsonp1090
q: 美食
imgfile: 
js: 1
stats_click: search_radio_all:1
initiative_id: staobaoz_20191124
ie: utf8
bcoffset: -3
ntoffset: 3
p4ppushleft: 1,48
s: 88

data-key: s
data-value: 176
ajax: true
_ksTS: 1574591216001_1272
callback: jsonp1273
q: 美食
imgfile: 
js: 1
stats_click: search_radio_all:1
initiative_id: staobaoz_20191124
ie: utf8
bcoffset: -6
ntoffset: 0
p4ppushleft: 1,48
s: 132
    '''