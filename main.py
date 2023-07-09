import yfinance as yf
from helper import *

def main():
    stocks = ["AAPL", "MSFT"]
    startRealTimeLoop(stocks, 1)

if __name__ == "__main__":
    main()
    
