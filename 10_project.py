inventory = {}

def show_menu():
    print("\n===== Inventory Management =====")
    print("1. Add Product")
    print("2. View Stock")
    print("3. Sell Product")
    print("4. Exit")

def add_product(inventory: dict,product: str,quantity: int):
    

    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

    print("Stock updated.")

def view_product(inventory: dict, product: str):
    stock = inventory.get(product)

    if stock is None:
        print("Product is not available. Press 1 if you want to add it to the inventory.")
    else:
        print(f"{product} has {stock} units in the inventory.")

def sell_product(inventory: dict, product: str):
    stock = inventory.get(product)

    if stock is None:
        print("product does not exist")

    elif stock == 0:
        print("out of stock")

    else:
        inventory[product] -= 1
        print("Stock updated")







while True:
    
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter your product: ")
        quantity = int(input("Enter quantity: "))

        add_product(inventory,product,quantity)
        
        

    elif choice == "2":
        product = input("Enter your product: ")
        

        view_product(inventory,product)
        

    elif choice == "3":
        product = input("Enter your product: ")

        sell_product(inventory,product)
        

       

        

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")