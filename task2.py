def stock_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 175
    }

    portfolio = {}
    total_value = 0

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        symbol = input("\nEnter Stock Symbol (or type 'done' to finish): ").upper().strip()
        if symbol == "DONE":
            break
        if symbol not in stock_prices:
            print("Stock not found in database. Try again.")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("Please enter a valid number for quantity.")

    print("\n--- Portfolio Summary ---")
    summary_text = "Stock Portfolio Summary:\n"
    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        val = price * qty
        total_value += val
        line = f"{symbol}: {qty} shares @ ${price} = ${val}\n"
        print(line.strip())
        summary_text += line

    total_line = f"\nTotal Investment Value: ${total_value}"
    print(total_line)
    summary_text += total_line

    # Save to file
    with open("portfolio_summary.txt", "w") as file:
        file.write(summary_text)
    
    print("\nSummary saved to 'portfolio_summary.txt' successfully!")

if __name__ == "__main__":
    stock_tracker()