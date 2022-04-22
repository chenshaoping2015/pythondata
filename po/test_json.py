import json

'''
json：是一种数据格式，是纯字符串。可以被解析成python的dict或其他形式。
dict：是一个完整的数据结构，是对hash table这一数据结构的实现，是一套从存储到提取都封装好的方案。它使用内置的hash函数来规划key对应的value的存储位置，从而获得O(1)的数据读取速度。
原文链接：https://blog.csdn.net/u010569893/article/details/97538914
'''
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
def test_dict2json(data=None):
    # 将python转换为json格式
    datajson = json.dumps(data)
    # print(type(data))
    # print(type(datajson))
    return  datajson
    # 查看json格式数据


def test_json2dict(data=None):
    data_orgin ={"name": "Bill", "info": {"sex": "male", "age": 29, "birth": "19900506"}}
    data_json2 = test_dict2json(data_orgin)
    print(type(data_json2))
    print(data_json2)

    # 将json字符串转换为python字典
    datadict = json.loads(data_json2)
    print(datadict)
    print(type(datadict))


def test_json():

    json_data = """{
       "favourite":{
          "bkmrk":{
             "id1490843709594066":{
                "guid":"904eff52277f403b89f6410fe2758646.11",
                "lcate":"1"
             },
             "id1490843712805183":{
                "guid":"58457f60eca64025bc43a978f9c98345.16",
                "lcate":"2"
             },
             "id149084371467327":{
                "guid":"a0f907f9dc8b40f689b083f3eba7228b.16",
                "lcate":"3"
             },
             "id1490843716295393":{
                "guid":"eb75d929455e468bb712e7bc2025d11a.16",
                "lcate":"4"
             }
          }
       }
    }"""

    data = json.loads(json_data)
    for v in data['favourite']['bkmrk'].values():
        print("%s;%s" % (v['lcate'], v['guid']))
