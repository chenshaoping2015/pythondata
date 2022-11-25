import time

import requests
from requests import Request, Session


class TestDemo:
    def test_post_re(self):
        base_url = "http://manage.dit.weshop.topscore.top/api/auth/login"
        data = {"tenant": "333251", "username": "admin", "password": "Tch*2021"}
        header = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8"
        }
        r = requests.post(base_url, json=data, headers=header)
        print(r.text)
        print(r.content)
        assert r.status_code == 200

    def test_post_file(self):
        # 保持会话
        s = requests.session()
        # 文件上传地址
        base_url = "http://manage.dit.weshop.topscore.top/api/weshop/rack/importWeShopProductStatus"
        # 打开要上传的文件
        with open("module.xlsx", "rb") as f:
            content = f.read()
        # 请求头
        h = {
            "Hades-Auth": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOjU0LCJjcmVhdGVkIjoxNjUxODIzMTc0NTk0LCJyb2xlcy\
            I6IlsyXSIsInRlbmFudF90eXBlIjowLCJ0eXBlIjoiQkFDS0VORCIsInRlbmFudCI6IjMzMzI1MSIsImV4cCI6MTY1M\
            jE4MzE3NH0.P16Sge1wm45In09_NmD36iKZ7c28oJgIf-DXAvgf1V8",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "multipart/form-data",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        # 上传文件时的传参
        r_data = {
            "status": "true",
            "shopId": 1
        }

        f = {"excelFile": ("modle.xlsx", open("modle.xlsx", "rb"))}

        r = s.post(base_url, headers=h, data=r_data, files=f)
        print(r.content)

    def test_join(self):
        c = 'abcghidefjkl'
        # 把new_c列表里面的元素按字母排序
        new_c = list(c)
        new_c.sort()
        print(new_c)
        # 通过空分隔符把new_c列表里面元素进行分隔,赋值给到cc
        cc = ''.join(new_c)
        print(cc)
        print(type(cc))

    def test_split(self):
        str = "Hello#Nice to meet you#qwe#asd#zxc\nYou\nHe"

        str1 = str.split("#", 1)
        # 以"#"键为分隔符，分隔1次，分割成2个子字符串
        print(str1)

        str2 = str.split("#", 2)
        # 以"#"键为分隔符，分隔2次，分割成3个子字符串
        print(str2)

        str3 = str.split(" ", 1)
        # 以" "键为分隔符，分隔1次，分割成2个子字符串
        print(str3)

        str4 = str.split(" ", 2)
        # 同理
        print(str4)

        str5 = str.split()
        # 未指定分隔符和分隔次数，默认分隔符为空格、换行（\n）、制表符（\t）
        print(str5)

        str6 = str.split("\n", 1)
        # 同1,2,3,4理
        print(str6)

    def test_re(self):
        url = 'http://httpbin.org/post'
        data = {'name': 'ruiyang'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/53.0.2785.116 Safari/537.36 '
        }
        s = Session()
        req = Request('POST', url, data=data, headers=headers)
        prepped = s.prepare_request(req)
        r = s.send(prepped)
        print(req)

    def test_time(self):
        print(time.ctime())
        print(time.localtime())
        print(time.asctime(time.localtime()))
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))