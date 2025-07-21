import streamlit as st
import alpaca_trade_api as tradeapi
from gamma_utils import extract_gamma_strikes
from trade_logic import submit_order, get_price, calculate_pnl
from telegram_utils import send_telegram_message
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
    # 📉 زر إغلاق الصفقة
if st.button("🚫 Close Trade"):
    # احصل على السعر الحالي
    exit_price = get_price("SPY")

    # احسب PnL
    pnl_value, pnl_percent = calculate_pnl(entry_price, exit_price)

    # عرض النتيجة
    st.success(f"✅ Trade closed at {exit_price} | PnL: ${pnl_value} ({pnl_percent}%)")

    # إرسال تنبيه إلى تليجرام
    send_telegram_message(bot_token, chat_id, f"📉 Trade closed.\nExit Price: {exit_price}\nPnL: ${pnl_value} ({pnl_percent}%)")

    # حفظ في سجل الصفقات
    with open("trade_log.csv", "a") as f:
        f.write(f"{datetime.now()},SPY,{entry_price},{exit_price},{pnl_value},{pnl_percent},closed\n")
