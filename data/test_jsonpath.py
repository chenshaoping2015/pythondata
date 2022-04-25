import os,sys
import json,jsonpath

def test_get_path():
    json_obj = json.load(open('lemon.json', 'r',encoding='utf-8'))
    print(type(json_obj))
    #提取所有包含addr属性的老师信息，结果为list类型
    results = jsonpath.jsonpath(json_obj, "$..teachers[?(@.addr)]")
    print(results)

    #提取所有年龄小于20岁的老师的name，结果为list类型
    results2 = jsonpath.jsonpath(json_obj, "$.lemon.teachers[?(@.age < 20)].name")
    print(results2)

def test_old_path():
    data = json.load(open('lemon.json', 'r', encoding='utf-8'))
    for v in data['lemon']['teachers'][0].values():
        print(v)