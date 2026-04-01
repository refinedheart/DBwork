import pymysql
from database import DatabaseManager

class TradeEngine:
    def __init__(self):
        self.db = DatabaseManager()

    def liquidate_user(self, user_id):
        """
        [对应报告：含有事务应用的删除操作 - 13分]
        功能：清空用户账户，包括级联删除持仓、流水和用户主体。
        """
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            conn.begin()
            cursor.execute("DELETE FROM Positions WHERE user_id = %s", (user_id,))
            
            cursor.execute("DELETE FROM Transactions WHERE user_id = %s", (user_id,))
            
            cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
            
            conn.commit()
            return True, "用户清算成功，数据已安全移除。"
            
        except Exception as e:
            conn.rollback()
            return False, f"清算失败，已触发事务回滚: {str(e)}"
        finally:
            conn.close()