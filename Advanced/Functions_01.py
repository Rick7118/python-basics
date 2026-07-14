def show_menu():
    print("\n===== Inventory Management =====")
    print("1. Add Product")
    print("2. View Stock")
    print("3. Sell Product")
    print("4. Exit")

show_menu()

def add_product(product):
    print(f'Adding {product}....')

add_product("Laptop")
add_product("Mouse")

def square(n: int) -> int:
    return n * n

result = square(90)
print(result)

