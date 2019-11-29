import requests
headers = {"headers": {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; DUK-AL20 Build/LMY48Z) Resolution/768*1366 Version/6.8.0 Build/6080103 Device/(HUAWEI;DUK-AL20) NetType/WiFi",

}}

def main():
    url = 'https://www.xiaohongshu.com/api/sns/v2/note/5ddbad6a000000000100151c/videofeed?page=1&num=5&' \
          'fetch_mode=3&' \
          'source=follow_feed&' \
          'ads_track_id=&' \
          'platform=android&' \
          'deviceId=2342ddea-87f2-3682-b08c-4d50af73ba4b&' \
          'device_fingerprint=20191113151756f8c2b20f631b64e0ae2b8b23a497ea8401e9110b08d93def&' \
          'device_fingerprint1=20191113151756f8c2b20f631b64e0ae2b8b23a497ea8401e9110b08d93def&' \
          'versionName=6.8.0&' \
          'channel=Store360' \
          '&sid=session.1574678247514389756013&' \
          'lang=zh-Hans' \
          '&t=1574678717&' \
          'fid=15740607810099397f4efcc4561309eb5e42ab0b0e45&' \
          'sign=92506a4dfbf44640bb3173621d1c757d'
    '''https://www.xiaohongshu.com/api/sns/v1/note/5dd378f5000000000100230c/feed?
    page=1
    &num=5
    &fetch_mode=1
    &source=explore
    &ads_track_id=
    &platform=android
    &deviceId=2342ddea-87f2-3682-b08c-4d50af73ba4b
    &device_fingerprint=20191113151756f8c2b20f631b64e0ae2b8b23a497ea8401e9110b08d93def
    &device_fingerprint1=20191113151756f8c2b20f631b64e0ae2b8b23a497ea8401e9110b08d93def
    &versionName=6.8.0&channel=Store360
    &sid=session.1574678247514389756013
    &lang=zh-Hans
    &t=1574684940
    &fid=15740607810099397f4efcc4561309eb5e42ab0b0e45
    &sign=79078571d545b610019cd0a8a80e2d50'''

    '''https://www.xiaohongshu.com/api/sns/v2/note/5dac417d000000000100bcc1/videofeed?
    page=1&num=5&fetch_mode=3&source=explore&ads_track_id=&platform=android
    &deviceId=2342ddea-87f2-3682-b08c-4d50af73ba4b
    &device_fingerprint=20191113151756f8c2b20f631b64e0ae2b8b23a497ea8401e9110b08d93def
    &device_fingerprint1=20191113151756f8c2b20f631b64e0ae2b8b23a497ea8401e9110b08d93def
    &versionName=6.8.0&channel=Store360
    &sid=session.1574678247514389756013
    &lang=zh-Hans
    &t=1574685624
    &fid=15740607810099397f4efcc4561309eb5e42ab0b0e45
    &sign=84bd6df43983b81342733540fb4a8cdf'''

    '''https://www.xiaohongshu.com/api/sns/v6/homefeed?
    oid=homefeed_recommend
    &cursor_score=1574684351.9800
    &geo=eyJsYXRpdHVkZSI6MzEuMjQ3MTkyLCJsb25naXR1ZGUiOjEyMS40OTIzNzh9%0A
    &trace_id=8e6f9467-2b8c-30fb-bbca-5650aadf7833
    &note_index=21
    &refresh_type=3
    &platform=android
    &deviceId=2342ddea-87f2-3682-b08c-4d50af73ba4b
    &device_fingerprint=20191113151756f8c2b20f631b64e0ae2b8b23a497ea8401e9110b08d93def
    &device_fingerprint1=20191113151756f8c2b20f631b64e0ae2b8b23a497ea8401e9110b08d93def
    &versionName=6.8.0
    &channel=Store360
    &sid=session.1574678247514389756013
    &lang=zh-Hans
    &t=1574684666
    &fid=15740607810099397f4efcc4561309eb5e42ab0b0e45
    &sign=c7dec857149a793894fc7b04dd3cd6e5'''

    '''https://www.xiaohongshu.com/api/sns/v6/homefeed?oid=homefeed_recommend&cursor_score=&
    geo=eyJsYXRpdHVkZSI6MzEuMjQ3MTkyLCJsb25naXR1ZGUiOjEyMS40OTIzNzh9%0A
    &trace_id=a70906ec-aa81-30fd-adf8-f34997784095
    &note_index=0&refresh_type=1
    &platform=android&deviceId=2342ddea-87f2-3682-b08c-4d50af73ba4b
    &device_fingerprint=20191113151756f8c2b20f631b64e0ae2b8b23a497ea8401e9110b08d93def
    &device_fingerprint1=20191113151756f8c2b20f631b64e0ae2b8b23a497ea8401e9110b08d93def
    &versionName=6.8.0&channel=Store360&sid=session.1574678247514389756013&lang=zh-Hans&t=1574686772
    &fid=15740607810099397f4efcc4561309eb5e42ab0b0e45
    &sign=4e9d928d78a759673d3ca393feea7922'''



    r = requests.get(url, **headers)
    print(r.text)
if __name__ == '__main__':
    main()