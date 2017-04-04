import urllib
import os
from bs4 import BeautifulSoup
import pandas as pd


base_url = "http://ichart.finance.yahoo.com/table.csv?s="
output_path = os.getcwd()


def make_url(ticker_symbol):
    return base_url + ticker_symbol

#output_path = "C:/path/to/output/directory"
def make_filename(ticker_symbol):
    return output_path + "/" + ticker_symbol + ".csv"

def pull_historical_data(ticker_symbol, directory=''):
    ticker_symbol = ticker_symbol.upper()
    try:
        urllib.request.urlretrieve(make_url(ticker_symbol), make_filename(ticker_symbol))
    except urllib.error.ContentTooShortError as e:
        outfile = open(make_filename(ticker_symbol), "w")
        outfile.write(e.content)
        outfile.close()

def read_historical_data(ticker_symbol):
    fname = make_filename(ticker_symbol)
    df = pd.read_csv(fname)
    df = df.set_index(pd.DatetimeIndex(df['Date']))
    df = df.drop('Date', 1)

    return df['2017-03-21':'2017-02-01']
        
# main fn
def get_price_history(ticker_symbol):
    pull_historical_data(ticker_symbol)
    df = read_historical_data(ticker_symbol)
    os.remove(make_filename(ticker_symbol))
    return df
        
