import yfinance as yf
from typing import List
import time

def getRealtimeInfo(stock: str) -> float:
  # Create a ticker object for the stock you want to retrieve data for
  ticker = yf.Ticker(stock)

  # Get the real-time stock information
  data = ticker.info

  # Access currentPrice from the data
  try:
    current_price = data['currentPrice']
  except KeyError:
    current_price = 0

  debug = False
  if debug:
    # Print the retrieved information
    print("Current Price:", current_price)

  return current_price


def getHistorialMonthlyData(stock: str, months: int):
  # Create a ticker object for the stock you want to retrieve data for
  ticker = yf.Ticker("AAPL")  # Replace "AAPL" with the desired stock symbol

  # Get the historical stock price data for the last month
  data = ticker.history(period="{}mo".format(months))

  # Print the retrieved historical stock price data
  print(data)


def startRealTimeLoop(stocks: List[str], duration: int) -> List[float]:
  while True:
    for stock in stocks:
      price = getRealtimeInfo(stock)
      print("{}:{}".format(stock, price))
    time.sleep(duration)
