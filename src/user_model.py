from database import DatabaseManager

class User:
    def __init__(self, user_id):
        self.db = DatabaseManager()
        self.user_id = user_id
        self._load_user_data()

    def _load_user_data(self):
        """从数据库加载用户信息"""
        sql = "SELECT * FROM Users WHERE user_id = %s"
        result = self.db.execute_query(sql, (self.user_id,))
        if result:
            self.data = result[0]
            self.username = self.data['username']
            self.balance = self.data['available_cash']

    def get_portfolio(self):
        """
        调用刚才创建的视图
        对应报告中含有视图的查询操作
        """
        sql = "SELECT * FROM View_Portfolio_Summary WHERE username = %s"
        return self.db.execute_query(sql, (self.username,))

    def buy_asset(self, ticker, qty):
        """
        执行买入操作，会触发表中的 Trigger 
        """
        asset_sql = "SELECT asset_id, current_price FROM Assets WHERE ticker = %s"
        asset = self.db.execute_query(asset_sql, (ticker,))[0]
        
        conn = self.db.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO Transactions (user_id, asset_id, trans_type, quantity, price, fee)
                VALUES (%s, %s, 'BUY', %s, %s, %s)
                """
                cursor.execute(sql, (self.user_id, asset['asset_id'], qty, asset['current_price'], 5.0))
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            return str(e)
        finally:
            conn.close()