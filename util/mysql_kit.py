import pymysql

from util import common_kit
from util.log_kit import logger

DB_CONF = {
    "host": common_kit.env('MYSQL_HOST'),
    "port": int(common_kit.env('MYSQL_PORT')),
    "user": common_kit.env('MYSQL_USER'),
    "password": common_kit.env('MYSQL_PASSWD'),
    "db": common_kit.env('MYSQL_DB'),
}


class Mysqler:

    def __init__(self, db_conf=DB_CONF):
        # 通过字典拆包传递配置信息，建立数据库连接
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        # 通过 cursor() 创建游标对象
        self.cur = self.conn.cursor()  # 返回数据不带列名字典
        # self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor) #返回数据带列名字典

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def query(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute(self, sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            logger.info("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()


mysqler = Mysqler(DB_CONF)

if __name__ == '__main__':
    # 数据库读操作
    pay_record_id = '33344'
    key = mysqler.query(
        f"SELECT pr.outTradeNo FROM payrecord pr INNER JOIN goodsorder go ON pr.goodsOrderId = go.id WHERE pr.id = '{pay_record_id}'; ")[
        0][0]
    # 数据库写操作
    mysqler.execute(f"UPDATE bbc_enter_name SET openid = 'o-12n0z07Zc6aLI9sAYouWkAojmA' WHERE id = 58 ")

#
# def exec_sql(sql):
#     """执行指定sql，限于增/删/改类型"""
#     logger.info('execute sql: %s' % sql)
#     db_util.execute(sql)
#
#
# def query_sql(sql):
#     """执行指定sql(查询类)，获取返回结果"""
#     # logger.info('query sql: %s' % sql)
#     return db_util.query(sql)
#
#
# def query_count_sql(sql):
#     """执行指定sql(查询类)，获取返回count"""
#     logger.info('query sql: %s' % sql)
#     resp = db_util.query(sql)
#
#
# def exec_file(file_path):
#     """从文件读取sql执行"""
#     logger.info('execute file: %s' % file_path)
#     path = "%s/%s" % (cfg.WS_HOME, file_path)
#     cmd = "mysql -h %s -P %s -u %s -p%s < %s" % (
#         cfg.MYSQL_IP, cfg.MYSQL_PORT,
#         cfg.MYSQL_USER, cfg.MYSQL_PASSWD, path)
#     status, output = subprocess.getstatusoutput(cmd)
#     assert status == 0, '导入 文件:%s 错误：%s' % (path, output)
