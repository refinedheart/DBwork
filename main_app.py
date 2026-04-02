import streamlit as st
import pandas as pd
from src.user_model import User
from src.trade_engine import TradeEngine
from src.risk_monitor import RiskMonitor
from src.strategy_bot import StrategyBot

st.set_page_config(page_title="Nankai Quant-RMS", layout="wide")

user_id = 1
user = User(user_id)
engine = TradeEngine()
monitor = RiskMonitor()
bot = StrategyBot()

st.sidebar.title("  量化管理系统")
choice = st.sidebar.radio("模块导航", ["资产大盘", "交易终端", "风险审计", "系统维护"])

if choice == "资产大盘":
    st.header("  实时资产穿透视图")
    st.caption("基于 MySQL 视图：View_Portfolio_Summary")
    
    portfolio_data = pd.DataFrame(user.get_portfolio())
    if not portfolio_data.empty:
        col1, col2, col3 = st.columns(3)
        col1.metric("可用现金", f"${float(user.balance):,.2f}")
        col2.metric("持仓标的数量", len(portfolio_data))
        
        st.subheader("持仓明细")
        st.dataframe(portfolio_data, use_container_width=True)
    else:
        st.warning("当前账户无持仓，请前往交易终端。")

elif choice == "交易终端":
    st.header("⚡ 智能下单中心")
    st.write("本模块演示【触发器 Trigger】拦截逻辑。")
    
    with st.form("trade_form"):
        ticker = st.selectbox("选择证券标的", ["NVDA", "AAPL", "TSLA"])
        qty = st.number_input("买入数量", min_value=1, value=100)
        submit = st.form_submit_button("执行买入")
        
        if submit:
            result = user.buy_asset(ticker, qty)
            if result is True:
                st.success("交易成功！已通过后端触发器风控校验。")
            else:
                # 截图重点：这里会展示触发器抛出的 'Insufficient balance'
                st.error(f"交易拦截：{result}")

elif choice == "风险审计":
    st.header("  实时风险监控")
    st.write("演示【多表 Join 查询】与审计日志。")
    
    alerts = monitor.get_risk_alerts()
    st.subheader("最新审计日志")
    st.table(alerts)
    
    if st.button("运行市场行情模拟 (调用存储过程)"):
        msg = bot.simulate_market_tick()
        st.toast(msg)

elif choice == "系统维护":
    st.header("  危险操作区")
    st.write("演示 事务 Transaction 级联删除")
    
    if st.button("全账户清算"):
        success, msg = engine.liquidate_user(user_id)
        if success:
            st.success(msg)
        else:
            st.error(msg)