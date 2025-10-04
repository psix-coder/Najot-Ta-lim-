from product import Product

products = [
    Product("Coca cola", 10, 10_000),
    Product("Fanta", 10, 10_000),
    Product("Orbit", 10, 10_000),
]

total_price = 0

for product in products:
    total_price+=product.narxi*product.soni

print(total_price)
