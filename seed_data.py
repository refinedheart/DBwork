import pymysql
from src.database import DatabaseManager

def seed_database():
    db = DatabaseManager()
    conn = db.get_connection()
    
    try:
        with conn.cursor() as cursor:
            assets = [
                ('NVDA', 'Nvidia Corp', 'Technology', 900.50),
                ('AAPL', 'Apple Inc', 'Technology', 175.20),
                ('TSLA', 'Tesla Inc', 'Automotive', 180.10),
                ('BTC', 'Bitcoin', 'Crypto', 65000.00)
            ]
            cursor.executemany(
                "INSERT IGNORE INTO Assets (ticker, asset_name, sector, current_price) VALUES (%s, %s, %s, %s)",
                assets
            )
            cursor.execute(
                "INSERT IGNORE INTO Users (user_id, username, risk_level, available_cash) VALUES (1, 'Hewenshuo', 'High', 1000000.00)"
            )
            cursor.execute(
                "INSERT IGNORE INTO Positions (user_id, asset_id, avg_cost, quantity) VALUES (1, 1, 850.00, 100)"
            )

            conn.commit()
            print("  Success 成功！‘灵魂数据’已注入 quant_system 数据库。")
    except Exception as e:
        conn.rollback()
        print(f"  Failure 注入失败: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()