import requests

class TestDemo:
    def test_post_re(self):
        base_url = "http://manage.dit.weshop.topscore.top/api/auth/login"
        data = {"tenant":"333251","username":"admin","password":"Tch*2021"}
        header = {
            "Accept":"application/json, text/plain, */*",
            "Content-Type":"application/json;charset=UTF-8"
        }
        r = requests.post(base_url,json=data,headers=header)
        print(r.text)
        print(r.content)
        assert r.status_code == 200
