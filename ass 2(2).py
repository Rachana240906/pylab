products = {}
while True:
    product_name = input("Enter product name (or type 'done' to finish): ")
    if product_name.lower() == 'done':
        break
    price = input(f"Enter price for {product_name}: ")
    products[product_name] = price
while True:
    lookup_product = input("Enter a product name to get its price (or type 'exit' to quit): ")
    if lookup_product.lower() == 'exit':
        break
    if lookup_product in products:
        print(f"The price of {lookup_product} is {products[lookup_product]}")
    else:
        print(f"{lookup_product} not found.")
