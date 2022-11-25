import requests
import pytest

class TestDemo:
    def test_shop_nature(self):
        base_url = "http://sit.topscore.top:81/api/web/platform/dict/save"
        data = {"categoryCode":"shop_nature","categoryName":"店铺性质","name":"自测_011","id":"null"}
        header = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json",
            "Cookie": "bmeval=1645671540314"
        }
        r = requests.post(base_url,json=data,headers=header)
        result = r.json()
        assert result["success"]==True
        print(r.json())

    def test_shop_type(self):
        base_url = "http://sit.topscore.top:81/api/web/platform/dict/save"
        data = {"categoryCode":"shop_type","categoryName":"店铺类型","name":"测试店_001","id":"null"}
        header = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json",
            "Cookie": "bmeval=1645671540314"
        }
        r = requests.post(base_url,json=data,headers=header)
        result = r.json()
        assert result["success"]==True
        print(r.json())

    def test_saveOrder(self):
        base_url = "http://sit.topscore.top:82/manufacturer/web/manufacturer/requisitionPlan/saveOrUpdateOrder"
        data = {"factoryId":107,"brandCode":"KC","generalCategoryCode":"B.大底_裁片底","planType":"forecast",\
                "requisitionPlanDetailVOList":[{"middleCategoryName":"H___C8EV05138","littleCategoryName":"T___C8EV00633",\
                                                "materialCode":"BHA-BHT1800014-C","materialName":"TA98320-1黑色橡胶大底+黑边油（通底/穿皮条插脚扣底标）",\
                                                "sizeCodeRangeName":"女鞋220-245码","spec":"null","unit":"双","plannedArrivalDate":1653926400000,\
                                                "sizeName":"245","sizeCode":"C10549","requisitionNum":111},\
                                               {"middleCategoryName":"H___C8EV05138","littleCategoryName":"T___C8EV00633","materialCode":"BHA-BHT1800014-C",\
                                                "materialName":"TA98320-1黑色橡胶大底+黑边油（通底/穿皮条插脚扣底标）","sizeCodeRangeName":"女鞋220-245码",\
                                                "spec":"null","unit":"双","plannedArrivalDate":1653926400000,"sizeName":"220","sizeCode":"C10544",\
                                                "requisitionNum":113}]}

        header = {
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        r = requests.post(base_url,json=data,headers=header)
        result = r.json()
        assert result["success"]==True
        print(r.json())