product_catalog = {"SKU123": {"name": "Widget A", "price": "$19.99", "qauntity": 50},
           "SKU456": {"name": "Widget B", "price": 34.95, "qauntity": 25},
           "SKU789": {"name": "Widget C", "price": 9.99, "qauntity": 100}}

sku_to_find = product_catalog.get("SKU123")
price = sku_to_find.get("price")
name = sku_to_find.get("name")
print("The price of " + name + " is " + price)