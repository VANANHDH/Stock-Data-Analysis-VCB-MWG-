import pandas as pd

def read_data(ticker):
    df = pd.read_csv(ticker)
    df.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = df.set_index("Date")
    df.index = pd.to_datetime(df.index, format='%Y%m%d')
    df.sort_values("Date", ascending=True, inplace=True)


    return df