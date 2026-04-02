import time
import random
from asset_model import Asset

class StrategyBot:
    """
    自动化策略模拟器：模拟市场价格波动，触发存储过程和视图更新。
    """
    def __init__(self, tickers=['NVDA', 'AAPL', 'TSLA']):
        self.tickers = tickers

    def simulate_market_tick(self):
        ticker = random.choice(self.tickers)
        asset = Asset(ticker)
        
        current_data = asset.db.execute_query("SELECT current_price FROM Assets WHERE ticker=%s", (ticker,))
        if current_data:
            old_price = float(current_data[0]['current_price'])
            new_price = old_price * (1 + random.uniform(-0.02, 0.02))
            
            asset.update_market_price(round(new_price, 4))
            return f"Tick: {ticker} updated from {old_price} to {round(new_price, 4)}"
        return "Tick failed."