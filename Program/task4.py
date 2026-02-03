

def add_item(cart):
    # Function to add an item to the cart
    item = input("Enter the item name: ")
    price = float(input("Enter the item price: $"))
    cart[item] = price
    print(f"Added '{item}' to the cart for ${price:.2f}\n")


def display_cart(cart):
    # Function to display all items in the cart
    if not cart:
        print("Your cart is empty.\n")
        return
    print("\n--- Shopping Cart ---")
    for item, price in cart.items():
        print(f"{item}: ${price:.2f}")
    print("----------------------\n")


def calculate_total(cart):
    # Function to calculate total cost
    total = sum(cart.values())
    return total

def main():
    # Main program loop
    cart = {}
    while True:
        print("1. Add Item")
        print("2. View Cart")
        print("3. Checkout")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            display_cart(cart)
        elif choice == "3":
            display_cart(cart)
            total = calculate_total(cart)
            print(f"Total cost: ${total:.2f}")
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

# Run the program
main()
