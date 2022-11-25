import json
from deepdiff import DeepDiff

def test_dep():
    f1 = json.loads(open('order02.json', 'r', encoding='utf-8').read())
    f2 = json.loads(open('order02.json', 'r',encoding='utf-8').read())

    re1 = json.dumps(f1)
    re2 = json.dumps(f2)
    print(re1)
    print(type(re1))
    print(DeepDiff(re1, re2))

