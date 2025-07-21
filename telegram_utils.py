import yfinance as yf
from datetime import datetime
from alpaca_trade_api.rest import REST

def submit_order(api: REST, symbol: str, qty=1, side='buy'):
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type='market',
        time_in_force='gtc'
    )
    return order

def get_price(symbol):
    data = yf.download(tickers=symbol, period='1d', interval='1m')
    return data['Close'].iloc[-1]

def calculate_pnl(entry_price, exit_price):
    return round(exit_price - entry_price, 2), round((exit_price - entry_price) / entry_price * 100, 2)
