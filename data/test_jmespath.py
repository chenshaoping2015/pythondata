import jmespath
import json

def test_jmes_path():
    json_obj = json.load(open('lemon.json', 'r', encoding='utf-8'))
    print(type(json_obj))
    results = jmespath.search("lemon.teachers.id",json_obj)
    print(results)
