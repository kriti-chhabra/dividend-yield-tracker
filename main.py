# Dividend Yield Tracker for Multiple Stocks
import yfinance as yf
import pandas as pd

# List of stock tickers (you can add more)
tickers = ["AAPL", "MSFT", "TSLA", "JPM", "KO"]

data = []

print("📈 Dividend Yield Watchlist")
print("-" * 40)

for ticker in tickers:
    stock = yf.Ticker(ticker)

    # Get current price
    stock_price = stock.history(period="1d")["Close"][0]

    # Get annual dividend (trailing 12 months)
    dividend = stock.info.get("dividendRate", 0.0)

    if stock_price > 0 and dividend > 0:
        dividend_yield = (dividend / stock_price) * 100
        print(f"{ticker}: {dividend_yield:.2f}%")
        data.append([ticker, stock_price, dividend, dividend_yield])
    else:
        print(f"{ticker}: No dividend available")
        data.append([ticker, stock_price, dividend, None])

# Save to CSV
df = pd.DataFrame(data, columns=["Ticker", "Stock Price", "Annual Dividend", "Dividend Yield (%)"])
df.to_csv("dividend_yields.csv", index=False)
print("\n✅ Results saved to dividend_yields.csv")
