import json

import redis

'''
用普通连接的方式：redis_conn = redis.Redis(host='127.0.0.1', port= 6379, password= 'your pw', db= 0)
缺点：
1.打印出的key数组，每个字符串前面加了一个b。在python3.x中，这表示这个字符串是bytes
2.在redis中，键和值都是以bytes方式存储的，r.keys()返回键也是bytes形式的，当我们判断str类型的字符串是否在 bytes类型的列表中时，结果是False
3.使用get()获取value值时，中文也会显示乱码
解决：在python中，我们可以通过声明redis连接池的decode_responses字段来对键值对进行默认编码
'''


def test_redis():
    pool = redis.ConnectionPool(host='192.168.2.45', port=6378, password='Ixs9opkwSw6WDIGoLJO5g', db=0,
                                decode_responses=True)
    redis_conn = redis.Redis(connection_pool=pool)
    # result为string类型
    result = redis_conn.get('DOUYIN_TOKEN_KEY69045273152130759804463798')
    # 将其转换为dict类型
    r = json.loads(result)
    # 读取具体某个字段值
    print(r['access_token'])
