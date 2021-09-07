import random


def test_radomdata():
    # 从指定的字符集中随机取，组合成新字符串
    seed = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    str1 = []
    for i in range(4):
        str1.append(random.choice(seed))
    StringS = ''.join(str1)
    return StringS

