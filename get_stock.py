from yahoo_finance import Share
from pprint import pprint

stock = Share('GOOG')
print stock.get_open()
print stock.get_price()
print stock.get_trade_datetime()
pprint(stock.get_historical('2017-06-01', '2017-06-02'))
