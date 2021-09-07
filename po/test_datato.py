import json

def test_dict2json(data=None):
    # 将字典转换为json格式
    datajson = json.dumps(data)
    return  datajson
    # 查看json格式数据
    print('json数据的格式为:',type(datajson))

def test_json2dict(data=None):
    data_orgin ={"name": "Bill", "info": {"sex": "male", "age": 29, "birth": "19900506"}}
    data_json = test_dict2json(data_orgin)
    print(type(data_json))

    # 将json字符串转换为字典
    datadict = json.loads(data_json)
    print(datadict)
    print(type(datadict))