# 10_exception_proof_cart.py
prices = []
while True:
    user_input = input("Enter item price (Q to quit): ").strip()
    try:
        if user_input.lower() == "q":
            break
        price = float(user_input)
        if price < 0:
            print("Price cannot be negative!")
        else:
            prices.append(price)
            print("Item added!")
    except ValueError:
        print("Invalid price!")
    finally:
        print("Entry processed.")
        print()

print(f"Items purchased: {len(prices)}")
print(f"Total: ${sum(prices):.2f}")