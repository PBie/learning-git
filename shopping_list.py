zakupy = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

liczba_produktow = 0

print("Lista zakupów")

for sklep, produkty in zakupy.items():
    sklep = sklep.upper()
    produkty = [produkt.capitalize() for produkt in produkty]
    
    print(f"Idę do {sklep} i kupuję tam: {produkty}.")

  