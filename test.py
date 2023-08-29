import json
import uuid
import copy
import ast

import requests

# cookies = json.loads(open("cookie.json", encoding="utf-8").read())
# cookies[10]['value'] = uuid.uuid4()
# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
# 定义请求参数
params = {
    "prompts": [],
    "sem": 20,
    "style": "creative",
    "cookie_U": "dfgdfd"
}
params1 = {
    "text": '''[
    {
        "domain": ".bing.com",
        "expirationDate": 1724677258.189497,
        "hostOnly": false,
        "httpOnly": false,
        "name": "SnrOvr",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "X=rebateson"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1727614857.416071,
        "hostOnly": false,
        "httpOnly": false,
        "name": "SRCHUSR",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "DOB=20230816&T=1693054852000&POEX=W"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": true,
        "name": "_Rwho",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "u=d"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1693293124.296144,
        "hostOnly": false,
        "httpOnly": false,
        "name": "GC",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "LxYLnnvxgGtNi_4ebqNZeoqNkTzxMnG7U1DFYKY3fZ9re2f8hKDUZws2832oVaCVU7HVZj6eW1laEJpgVEnvKg"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1693232217.496736,
        "hostOnly": false,
        "httpOnly": true,
        "name": "SUID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "A"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1726574119.269327,
        "hostOnly": false,
        "httpOnly": true,
        "name": "_EDGE_CD",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "m=en-us"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1693293136.212902,
        "hostOnly": false,
        "httpOnly": false,
        "name": "cct",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "LxYLnnvxgGtNi_4ebqNZeoqNkTzxMnG7U1DFYKY3fZ9AVAMRaLUNoTA4XPOFseCVMpyJs5vOWqXdt0mqBLDYUA"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1727767317.897036,
        "hostOnly": false,
        "httpOnly": false,
        "name": "SRCHHPGUSR",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "SRCHLANG=zh-Hans&IG=3D3E3C1BF7B94BE9BDA8D6D9DC3D086C&PV=15.0.0&BRW=XW&BRH=M&CW=1496&CH=796&SCW=1204&SCH=316&DPR=1.2&UTC=480&DM=1&EXLTT=31&HV=1693054859&WTS=63827769861&cdxtone=Creative&cdxtoneopts=h3imaginative,clgalileo,gencontentv3&PRVCW=1496&PRVCH=796&BZA=0"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1727767023.881691,
        "hostOnly": false,
        "httpOnly": false,
        "name": "ANON",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "A=ECBB496A7C9DEBCD4A0E14D5FFFFFFFF&E=1c6e&W=1"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1723719679,
        "hostOnly": false,
        "httpOnly": false,
        "name": "BCP",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "AD=1&AL=1&SM=1"
    },
    {
        "domain": "www.bing.com",
        "expirationDate": 1723712452.54711,
        "hostOnly": true,
        "httpOnly": false,
        "name": "MicrosoftApplicationsTelemetryDeviceId",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "d0a33281-f1ae-42c3-9d28-ca498cbc1383"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "_SS",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "SID=20744E40FFB262BA0B095D37FEC76322&R=2793&RB=2793&GB=0&RG=0&RP=2793"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "ipv6",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "hit=1693058462770&t=4"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1694416623.881632,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_U",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "1kXSaJ6bmJ2U251wQPpWe6gkr9aaotfc_BPPFJvxPnTULLj4tVZnp03sbKGzLrllqdAQO_KFNe-GgdxvNLS1hj4J3gPj2OZWYShn0LHyZjiBzpVXOIYiCLbiyvWPUW4pwA0uCQmJ45GAcSpscTjo6AlOvPp3TXayVsZBy11yKSQKRo1ip97OyGyARd28nwxAFjZulX6iqp2IUmOT0DbqBH-Z4lr_zjqfwkYAV-1WmlQw"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1726733061.329974,
        "hostOnly": false,
        "httpOnly": false,
        "name": "SRCHD",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "AF=MY0291"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1726733066.249795,
        "hostOnly": false,
        "httpOnly": false,
        "name": "PPLState",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "1"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1695349365,
        "hostOnly": false,
        "httpOnly": false,
        "name": "ANIMIA",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "FRE=1"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1709481865.249777,
        "hostOnly": false,
        "httpOnly": false,
        "name": "NAP",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "V=1.9&E=1c14&C=WsEfN3we-BWyhK8bRUGCPFav2jayUfOI7_C26mrOjn66RYst1ICdXw&W=1"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1727615762.459651,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_RwBf",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "r=1&ilt=1&ihpd=0&ispd=1&rc=2793&rb=2793&gb=0&rg=0&pc=2793&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=1&l=2023-08-26T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=bingcopilotwaitlist&c=MY00IA&t=6282&s=2023-03-18T15:29:27.9304101+00:00&ts=2023-08-26T13:00:57.7689962+00:00&rwred=0&wls=2&wlb=0&lka=0&lkt=0&TH=&mta=0&dci=0&e=dytgoR3d6vvYcdhxekgdWdhc0XBU5GYKWo8deYN7oxKU6q9OQqwQtKlSXB5959Rze1RmBIywqCCC5LpakcB5vA&A=ECBB496A7C9DEBCD4A0E14D5FFFFFFFF"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1726736451.956277,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_UR",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "QS=0&TQS=0"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": true,
        "name": "_EDGE_S",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": true,
        "storeId": null,
        "value": "SID=20744E40FFB262BA0B095D37FEC76322"
    },
    {
        "domain": "www.bing.com",
        "expirationDate": 1726903023.881511,
        "hostOnly": true,
        "httpOnly": true,
        "name": "MUIDB",
        "path": "/",
        "sameSite": null,
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "16A3E765FEB365241554F476FF2164D7"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1727445074.203939,
        "hostOnly": false,
        "httpOnly": true,
        "name": "USRLOC",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "HS=1&ELOC=LAT=31.22425651550293|LON=121.4769287109375|N=%E9%BB%84%E6%B5%A6%E5%8C%BA%EF%BC%8C%E4%B8%8A%E6%B5%B7%E5%B8%82|ELT=4|&CLOC=LAT=34.0447|LON=-118.2527|A=33429|TS=230828071917|SRC=I"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1727259280.951822,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_HPVN",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "CS=eyJQbiI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wOC0yMlQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6OH0="
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1727253173.368532,
        "hostOnly": false,
        "httpOnly": false,
        "name": "ABDEF",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "V=13&ABDV=13&MRNB=1692693173366&MRB=0"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1726733066.249811,
        "hostOnly": false,
        "httpOnly": true,
        "name": "KievRPSSecAuth",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "FABiBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACBZG5QYVS+A4IAQ/neJoNYE6y4JjDMp7ilXytHfGdSpy0iuQ5Ly7m5btaSVi7Y+n1bXmgMkeLyxXZemudaIkn85sIJ/rNuTtDi7sAzuHJHLWobWGmScmKcINTm2RW/jjgMaYrmpIhY97O3Klfwhfcf5PZkOykTX2q2dS9EmbtUvQ36mlrC7KjmIuNLs0YvXUvi47HqQpyDBtR9RFrPl5GsORfgf20FWhvxhpVjmFL/WV8Jwt03D9VWV0scUQ1LHQEDoIOIuIw4C3q7d8zjKUXA+FkewzrTQiDSbrZ9Bqph+7fVVY03wtJREiq4sUBmV3hVJ3x1Ts1ecbPf/VIViWcjqghM3Wv97XFW4fUqr4MG782FLCkwxtcu7RnmWUma6lMlVBBksJ4mTcDYNemnNELQGqjYeMU6so9N+YvHyM/swRiVcexurmXQBzdezB6+sfWl8/E9M5RTf+CKwbMr8QQ6ZuA+4/P9jlbc2FDq0Zl+OV4R1RZNUKghmfqRyjiwXVUrvdx1yjiogelHfkAAlKdicXGNcA2ROItXcJt0YhBd31lOp76mvSI4KvppnzuYGFGqUeQKuR1PFscTQ8HbpR8xDnN9pL0tkaNCS2v0mXW25fUckIljNZ4WvQHOEDpI9wAVNN6pZzTt8DjohuEGXVwcZmglZfGM5G0mB1KeKgs2EO8UpfyS71Pyox3Shz5S+MyxzSMhGWtp6SzRbW2nt2F/9pDxCnpsf01D69rOKVchhb55SlHFNx7EwOh4p1ybnqiLoFxNMknsePuH2Vjex0ZOMHQJqSvz3LHBKhCRoIWx+NEdIpMh0Pd/GJN56snbtKHbNSPE4wZB9T5BddYHzhpS8Nu9geXeQ2k77O0LE4SYkqfSgWsbH8juj6dz8M76cleJWYm/WXSb5mPz3lH86GE4OVyfcPFpAjZB73efDm2FjnyNvAj/9UW1Nq9LYwqwgvYSva2JzcraKYjbEpPwPCSgGxX5rpnKvD6J1FZnspkXxoSuG3xmOsJXUG55iRauDghcBFL8rya/veT17aBfhJE8lvWI+Hctuv40mGcCEpbxBbDkemizVaJfOYhZ5hbGij+D8C4noPRSQuaxPga1Laf758UnfUSg45Jo6gbnxxFKZh/UTR2tPxoAvF3szbPWA+knqDmIPmRjD5tThXAkI9TarKWznVoEQY35ML1VRKJJpW/kduX1In3CGNKooXT9M1eBkB85hHtImUfQWLQz5RCL07yv4R/5Pvz9MbB4zW3s0vtTJEPf9Af0zmlXJ3oTm4H6f2wlqwt4qYpZGWlpoKIKwlE7gx30r+5mxoIlneyaT6p53W0w7fyLKPl72tIMLyMhEoxaZXhxb196u6+cJuWzdpFYBzGV/goJ5Fq69HFcazmnjDqdkHtMojP6hXuAW9jP0cKj6vVsBnZTYUACXSr+lyk1yhzO0nsCiMN6dmC/ND"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1726645450.405299,
        "hostOnly": false,
        "httpOnly": false,
        "name": "MUID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "16A3E765FEB365241554F476FF2164D7"
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "SNRHOP",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "I=&TS="
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1726733061.329984,
        "hostOnly": false,
        "httpOnly": false,
        "name": "SRCHUID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "V=2&GUID=71C027451D494CD3A09BF3E3DA3DA625&dmnchg=1"
    },
    {
        "domain": ".bing.com",
        "expirationDate": 1693382668.274136,
        "hostOnly": false,
        "httpOnly": true,
        "name": "WLID",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "ZY2rVLfLYbTWoPYxdQXN3WuTVNxSC9CtdNhRtxt7vO/Br5hEkt/V5aA+ZfU+8hXaV09MpSXBUAkZimAjq0EQW2At7lp3+ngU9rXGtDWKFcM="
    },
    {
        "domain": ".bing.com",
        "hostOnly": false,
        "httpOnly": false,
        "name": "WLS",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": true,
        "storeId": null,
        "value": "C=ca1fce2d887304b9&N=%e7%8f%82%e5%bc%ba"
    }
]'''
}
# 发送请求
for n in range(10):
    params['prompts'].append('hello')
# response = requests.post("https://chattest-1umk.onrender.com/bing", headers=headers, json=params)
# response = requests.post("http://127.0.0.1:8000/bing", headers=headers, json=params)
response = requests.post("http://127.0.0.1:8000/update-cookie", headers=headers, json=params1)
try:
    a = ast.literal_eval(response.text)
    print(a)
except:
    print(response.text)
# 打印返回结果
