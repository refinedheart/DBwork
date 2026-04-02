CREATE OR REPLACE VIEW View_Portfolio_Risk_Analysis AS
SELECT 
    u.username,
    a.ticker,
    a.asset_name,
    p.quantity,
    p.avg_cost,
    a.current_price,
    (p.quantity * a.current_price) AS market_value,
    ((a.current_price - p.avg_cost) * p.quantity) AS pnl,
    (((a.current_price - p.avg_cost) / p.avg_cost) * 100) AS pnl_percentage,
    u.risk_level
FROM Users u
JOIN Positions p ON u.user_id = p.user_id
JOIN Assets a ON p.asset_id = a.asset_id;