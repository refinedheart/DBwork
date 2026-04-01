class Asset:
    def __init__(self, ticker):
        self.db = DatabaseManager()
        self.ticker = ticker

    def update_market_price(self, new_price):
        """
        功能：调用数据库存储过程，同步更新资产价格并记录审计日志。
        """
        conn = self.db.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.callproc('UpdateAssetPrice', (self.ticker, new_price))
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            return False
        finally:
            conn.close()