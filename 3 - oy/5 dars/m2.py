from v1 import Product

Product('pepsi', 10, 10)
Product('fanta', 100, 10)
Product('flesh', 1000, 10)


print(Product.products)
print(Product.discount_products())
print(Product.max_price_products())
print(Product.products)