def main():
    # 1. Hardcoded dictionary defining stock prices
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 140.00,
        "MSFT": 330.00,
        "AMZN": 135.00,
        "NIFTY50": 200.00,
        "SENSEX": 170.00,
        "TATA": 280.00,
        "SAMSUNG": 270.00
    }

    portfolio = {}
    total_investment = 0.0

    print("--- Simple Stock Portfolio Tracker ---")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    # 2. Input/Output loop for user data entry
    while True:
        symbol = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

        if symbol == 'DONE':
            break

        if symbol not in stock_prices:
            print(f"Error: '{symbol}' is not in our database. Try again.")
            continue

        try:
            quantity = float(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number for the quantity.")
            continue

        # Update the portfolio dictionary with the new quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} shares of {symbol}.")

    # 3. Basic Arithmetic to calculate totals
    print("\n" + "="*30)
    print("--- Portfolio Summary ---")
    
    summary_lines = []
    
    for sym, qty in portfolio.items():
        price = stock_prices[sym]
        value = qty * price
        total_investment += value
        
        # Format the line and save it to our list for easy printing/saving
        line = f"{sym}: {qty} shares @ ${price:.2f} = ${value:.2f}"
        summary_lines.append(line)
        print(line)

    total_line = f"\nTotal Investment Value: ${total_investment:.2f}"
    print(total_line)
    print("="*30)

    # 4. Optional File Handling to save the result
    if total_investment > 0:
        save_file = input("\nWould you like to save this summary to a file? (yes/no): ").lower()
        if save_file in ['yes', 'y']:
            try:
                # Using 'with' ensures the file is automatically closed after writing
                with open("portfolio_summary.txt", "w") as file:
                    file.write("--- Portfolio Summary ---\n")
                    for line in summary_lines:
                        file.write(line + "\n")
                    file.write(total_line + "\n")
                print("Successfully saved to 'portfolio_summary.txt'.")
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    main()