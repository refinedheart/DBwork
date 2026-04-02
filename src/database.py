import pymysql
from pymysql.cursors import DictCursor

class DatabaseManager:
    """
    针对报告【系统配置】章节的连接串分析：
    - Host: 'localhost'
    - Port: 3306
    - User: 'root'
    - DB: 'quant_system'
    """
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'your_password',
            'database': 'quant_system',
            'charset': 'utf8mb4',
            'cursorclass': DictCursor,
            'autocommit': False
        }

    def get_connection(self):
        return pymysql.connect(**self.config)

    def execute_query(self, sql, params=None):
        """通用查询方法，用于 View 和基础查询"""
        conn = self.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                return cursor.fetchall()
        finally:
            conn.close()