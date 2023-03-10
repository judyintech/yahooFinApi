# https://theautomatic.net/yahoo_fin-documentation/
from yahoo_fin.stock_info import get_data, tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table



def printStockInfo(ticker, start_date, end_date, interval="1d"):
    try:
        data = get_data(ticker , start_date , end_date)
        print(ticker, ": ", data)
    except Exception as error:
        print(f"ticker {ticker} not supported. {type(error)} Error: {error}")

printStockInfo('msft', '01/01/1999', '01/10/1999')
printStockInfo('srra', '01/01/2017', '01/10/2018')
printStockInfo('aapl', '01/01/2022', '03/01/2022', "1wk")
