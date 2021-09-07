import pymysql


def test_mysqlConnect(db=None):
    config = {
        'host': '192.168.2.46',
        'port': 3309,
        'user': 'root',
        'passwd': '123456',
        'charset': 'utf8',
        'database': db
    }
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    return conn



def test_queryRand(db = None,key=None, table=None, **kwargs):
    # 查询结果随机一条数据操作
    conn = mysqlConnect(db)
    ct = json2str(kwargs)
    sql = f"""SELECT {key} FROM {db}.{table} WHERE  {ct} order by rand() limit 1"""
    query = conn.select(sql)
    return query[0][0]
