from database import DatabaseManager
import pandas as pd

class RiskMonitor:
    def __init__(self):
        self.db = DatabaseManager()

    def get_risk_alerts(self, limit=10):
        """
        获取最新的风险审计日志
        对应报告：多表关联查询与审计逻辑展示
        """
        sql = """
        SELECT l.log_id, u.username, l.action_type, l.message, l.log_time
        FROM Audit_Logs l
        LEFT JOIN Users u ON l.user_id = u.user_id
        ORDER BY l.log_time DESC
        LIMIT %s
        """
        return pd.DataFrame(self.db.execute_query(sql, (limit,)))

    def get_high_risk_users(self):
        """
        查找被触发器拦截次数超过 3 次的用户
        """
        sql = """
        SELECT u.username, COUNT(l.log_id) as violations
        FROM Audit_Logs l
        JOIN Users u ON l.user_id = u.user_id
        WHERE l.action_type = 'RISK_REJECT'
        GROUP BY u.user_id
        HAVING violations >= 3
        """
        return pd.DataFrame(self.db.execute_query(sql))