# show_expected_result = False
# show_hints = False

# class Stock:
#     def __init__(self, tricker, price, company) -> None:
#         self.tricker    = tricker
#         self.price      = price
#         self.company    = company

#     def get_description(self):
#         return f"{self.tricker}: {self.company} -- ${self.price}"

import time
import yfinance as yf


class Stock:
    # This class represents one stock in your watchlist or portfolio.

    def __init__(self, ticker, company, buy_below=None, sell_above=None):
        # Instance attributes belong to each object separately.
        self.ticker = ticker
        self.company = company
        self.buy_below = buy_below
        self.sell_above = sell_above

        self.current_price = None
        self.previous_price = None

    def fetch_price(self):
        # This method gets the latest available price from Yahoo Finance.
        stock_data = yf.Ticker(self.ticker)
        history = stock_data.history(period="1d", interval="1m")

        if history.empty:
            return None

        latest_price = history["Close"].dropna().iloc[-1]
        return float(latest_price)

    def update_price(self):
        # Save the old price before updating.
        self.previous_price = self.current_price

        # Fetch and store the new price.
        self.current_price = self.fetch_price()

    def get_price_change_status(self):
        # This method compares the current price with the previous price.
        if self.previous_price is None or self.current_price is None:
            return "NO PREVIOUS DATA"

        if self.current_price > self.previous_price:
            return "PRICE UP"

        if self.current_price < self.previous_price:
            return "PRICE DOWN"

        return "NO CHANGE"

    def get_alert(self):
        # This method gives simple alerts based on your own price limits.
        if self.current_price is None:
            return "NO PRICE DATA"

        if self.buy_below is not None and self.current_price <= self.buy_below:
            return "BUY ALERT"

        if self.sell_above is not None and self.current_price >= self.sell_above:
            return "SELL ALERT"

        return "NO ALERT"

    def get_description(self):
        # This method returns a readable text about this stock.
        price_text = "N/A" if self.current_price is None else f"${self.current_price:.2f}"
        status = self.get_price_change_status()
        alert = self.get_alert()

        return f"{self.ticker}: {self.company} | Price: {price_text} | {status} | {alert}"

    def __str__(self):
        # print(stock_object) will use this method.
        return self.get_description()


class Watchlist:
    # This class manages multiple Stock objects.

    def __init__(self):
        # This list stores Stock objects.
        self.stocks = []

    def add_stock(self, stock):
        # Add a Stock object to the watchlist.
        self.stocks.append(stock)

    def remove_stock(self, ticker):
        # Keep all stocks except the one with the given ticker.
        self.stocks = [stock for stock in self.stocks if stock.ticker != ticker]

    def show_all(self):
        # Print all stocks in the watchlist.
        for stock in self.stocks:
            print(stock)

    def update_all_prices(self):
        # Update every stock price one by one.
        for stock in self.stocks:
            try:
                stock.update_price()
            except Exception as error:
                print(f"Could not update {stock.ticker}: {error}")

    def run(self, seconds=30):
        # This loop updates prices every given number of seconds.
        while True:
            print("\nUpdating stock prices...\n")

            self.update_all_prices()
            self.show_all()

            print(f"\nWaiting {seconds} seconds...")
            time.sleep(seconds)


# This code only runs when this file is executed directly.
if __name__ == "__main__":
    my_watchlist = Watchlist()

    google = Stock(
        ticker="GOOGL",
        company="Alphabet Inc.",
        buy_below=160,
        sell_above=190
    )

    apple = Stock(
        ticker="AAPL",
        company="Apple Inc.",
        buy_below=180,
        sell_above=230
    )

    tesla = Stock(
        ticker="TSLA",
        company="Tesla Inc.",
        buy_below=200,
        sell_above=300
    )

    my_watchlist.add_stock(google)
    my_watchlist.add_stock(apple)
    my_watchlist.add_stock(tesla)

    try:
        my_watchlist.run(seconds=30)
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")