import pytest

from util.mysql_kit import mysqler


# 查询数据库：最新创建的报名活动id
@pytest.fixture(scope="function")
def sql_matchid():
    match_id = mysqler.query(f"SELECT id FROM bbc_match ORDER BY create_time DESC LIMIT 1")[0][0]
    return match_id


# 更新数据库：将对应报名ID用户的openid改成自己的
@pytest.fixture(scope="function")
def sql_fix_openid(signin_id):
    res = mysqler.query(f"UPDATE bbc_enter_name SET openid = 'o-12n0z07Zc6aLI9sAYouWkAojmA' WHERE id = \'{signin_id}\'")


if __name__ == '__main__':
    pass
