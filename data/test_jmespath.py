import jmespath
import json

def test_jmes_path():
    json_obj = json.load(open('lemon.json', 'r', encoding='utf-8'))
    results = jmespath.search("lemon.teachers",json_obj)
    print(results)
