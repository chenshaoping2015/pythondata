import pymysql


def test_mysqlConnect():
    config = {
        'host': '192.168.2.46',
        'port': 3309,
        'user': 'root',
        'passwd': '123456',
        'charset': 'utf8',
        'database': 'platform'
    }
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    return conn



def test_queryRand(db = None,key=None, table=None, **kwargs):
    # 查询结果随机一条数据操作
    conn = test_mysqlConnect()
    sql = f"""SELECT {key} FROM {db}.{table} order by rand() limit 1"""
    query = conn.excute(sql)
    return query[0][0]

def test_category_brand():
    category_brand = test_queryRand('platform','code', 't_brand')
    return category_brand[0][0]