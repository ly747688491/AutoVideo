import os
import sqlite3

from dbutils.persistent_db import PersistentDB

from config.InitDatabase import DATABASE_NAME


def check_sql_db_file():
    # 获取当前文件所在的目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 检查目录下是否存在sql.db文件
    files = os.listdir(base_dir)
    if DATABASE_NAME in files:
        # 如果文件存在，返回文件的完整路径
        return os.path.join(base_dir, DATABASE_NAME)
    else:
        # 如果文件不存在，返回False
        return False


class Connect:
    def __enter__(self):
        """自动从连接池中取出一个连接"""
        db_pool = Pool()
        self.conn = db_pool.connection()
        self.cur = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """自动释放当前连接资源 归还给连接池"""
        self.cur.close()
        self.conn.close()


class Pool(object):  # 数据库连接池
    __pool = None  # 记录第一个被创建的对象引用
    config = {
        'database': check_sql_db_file()  # 数据库文件路径
    }

    def __new__(cls, *args, **kwargs):
        """创建连接池对象  单例设计模式(每个线程中只创建一个连接池对象)  PersistentDB为每个线程提供专用的连接池"""
        if cls.__pool is None:  # 如果__pool为空，说明创建的是第一个连接池对象
            cls.__pool = PersistentDB(sqlite3, maxusage=None, closeable=False, **cls.config)
        return cls.__pool
