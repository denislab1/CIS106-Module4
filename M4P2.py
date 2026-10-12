purchase_price = float(input("Enter purchase price per share: "))
current_price = float(input("Enter current stock price: "))
quantity = int(input("Enter number of shares: "))

change = (current_price - purchase_price) * quantity

print("Stock gain or loss: $", round(change, 2))