import random
import time


def randomTest():
    id = round(time.time() * 1000)
    print(id)
    return id


def dict_str(dictin):
    '''
    将字典变成，key='value',key='value' 的形式
    '''
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), str(v))
        tmplist.append(' ' + tmp + ' ')
    return ','.join(tmplist)


def dict_str_time(dictin):
    '''
    将字典变成，key='value',key='value' 的形式
    '''
    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    dictin["create_time"] = create_time
    dictin["update_time"] = update_time
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), str(v))
        tmplist.append(' ' + tmp + ' ')
    return ','.join(tmplist)


def dict_str_and(dictin):
    '''
    将字典变成，key='value' and key='value'的形式
    '''
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), str(v))
        tmplist.append(' ' + tmp + ' ')
    return ' and '.join(tmplist)


def get_i_sql(table, dict):
    '''
    生成insert的sql语句
    @table，插入记录的表名
    @dict,插入的数据，字典
    '''
    sql = 'insert into %s set ' % table
    sql += dict_str(dict)
    return sql


def get_i_sql_time(table, dict):
    '''
    生成insert的sql语句
    @table，插入记录的表名
    @dict,插入的数据，字典
    '''

    sql = 'insert into %s set ' % table
    sql += dict_str_time(dict)
    return sql


def get_s_sql(table, keys, conditions, isdistinct=0):
    '''
        生成select的sql语句
    @table，查询记录的表名
    @key，需要查询的字段list
    @conditions,插入的数据，字典
    @isdistinct,查询的数据是否不重复
    '''
    if isdistinct:
        sql = 'select distinct %s ' % ",".join(keys)
    else:
        sql = 'select  %s ' % ",".join(keys)
    sql += ' from %s ' % table
    if conditions:
        sql += ' where %s ' % dict_str_and(conditions)
    return sql


def get_u_sql(table, value, conditions):
    '''
        生成update的sql语句
    @table，查询记录的表名
    @value，dict,需要更新的字段
    @conditions,插入的数据，字典
    '''
    sql = 'update %s set ' % table
    sql += dict_str(value)
    if conditions:
        sql += ' where %s ' % dict_str_and(conditions)
    return sql


def get_d_sql(table, conditions):
    '''
        生成detele的sql语句
    @table，查询记录的表名

    @conditions,插入的数据，字典
    '''
    sql = 'delete from  %s  ' % table
    if conditions:
        sql += ' where %s ' % dict_str_and(conditions)
    return sql


def get_random(length):
    range_start = 10 ** (length - 1)
    range_end = (10 ** length) - 1
    return random.randint(range_start, range_end)


def get_timestamp():
    return int(round(time.time() * 1000))  # 13位 1609923362699