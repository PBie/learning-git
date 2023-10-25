# Jasne, zapomniałem o angielskich zmiennych.
shopping = {
    "piekarnia": ["chleb", "pączek", "bułka"],
    "warzywniak": ["marchew", "seler", "cukinia"]
}

products_number = 0

print("Lista zakupów")

for shop, products in shopping.items():
    shop = shop.upper()
    products = [product.upper() for product in products]
    
    print(f"Idę do {shop} i kupuję tam: {products}.")

    products_number += len(products)

print(f"W sumie kupuję {products_number} produktów.")
