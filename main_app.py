import streamlit as st
import pandas as pd
from database import DatabaseManager
from user_model import User

st.set_page_config(page_title="PQ-RMS 量化风控系统", layout="wide")

db = DatabaseManager()

st.sidebar.title("导航栏")
menu = st.sidebar.selectbox("选择功能模块", ["资产总览", "模拟交易", "风控审计"])

if menu == "资产总览":
    st.header("📈 个人资产穿透实时视图")
    query = "SELECT * FROM View_Portfolio_Summary"
    data = pd.DataFrame(db.execute_query(query))
    
    if not data.empty:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric("可用现金", f"${data['available_cash'].iloc[0]:,.2f}")
        with col2:
            st.dataframe(data)
    else:
        st.info("暂无持仓数据。")

elif menu == "模拟交易":
    st.header("🚀 智能交易中心")
    ticker = st.selectbox("选择标的", ["NVDA", "AAPL", "TSLA"])
    qty = st.number_input("买入数量", min_value=1, value=10)
    
    if st.button("提交订单"):
        user = User(user_id=1)
        result = user.buy_asset(ticker, qty)
        
        if result is True:
            st.success("交易成功！已通过风险校验。")
        else:
            st.error(f"交易被拒绝：{result}")