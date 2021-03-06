import pymysql

from util import common_util
from util.log_util import logger

DB_CONF = {
    "host"    : common_util.env('MYSQL_HOST'),
    "port"    : int(common_util.env('MYSQL_PORT')),
    "user"    : common_util.env('MYSQL_USER'),
    "password": common_util.env('MYSQL_PASSWD')
    # "db": common_util.env('MYSQL_DB'),
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
