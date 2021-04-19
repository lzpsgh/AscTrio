"""文件工具类，处理文件相关"""
import os


def getRootPath(projectName="qm-autotest"):
    """获取项目的根目录"""
    """从文件中读取需要检验的json数据返回"""
    curPath = os.path.abspath(os.path.realpath(__file__))  # 获取项目根目录
    # 获取根目录
    rootPath = curPath[:curPath.find(projectName + "/") + len(projectName)]  # 关键点！！
    return rootPath


def judgeFileNotExistToCreate(path=None):
    """判断文件如果不存在就创建"""
    if not os.path.exists(path):
        # 创建空文件
        # os.mknod(path)  # mac 使用 mknod需要升级特权，所有这里使用open a 创建
        open(path, 'a')


if __name__ == "__main__":
    rootPath = getRootPath()
    judgeFileNotExistToCreate(rootPath + "/resources/sensors/check")
