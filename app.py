import streamlit as st
import alpaca_trade_api as tradeapi

# إعداد المفاتيح (⚠️ لا تشارك هذه المفاتيح خارج البيئة الخاصة)
API_KEY = "PKSMPMAAIY38BM22YWAA"
API_SECRET = "XjJNJJuheOxB8CLJGzxm8qCmD7LZPxjyggErsZpJ"
BASE_URL = "https://paper-api.alpaca.markets"

# إنشاء الاتصال
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')
account = api.get_account()

# واجهة ستريمليت
st.title("📈 Alpaca Paper Trading App")
st.subheader("💵 Buying Power:")
st.code(f"{account.buying_power}", language="python")

# تنفيذ صفقة بسيطة
if st.button("🛒 Execute Test Order (Buy 1 SPY)"):
    order = api.submit_order(
        symbol="SPY",
        qty=1,
        side="buy",
        type="market",
        time_in_force="gtc"
    )
    st.success(f"✅ Order submitted: {order.id}")