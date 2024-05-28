import json

file_path = '10lab1products.json'

with open(file_path, 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

for product in data['products']:
    name = product['name']
    price = product['price']
    weight = product['weight']
    available = product['available']
    
    availability = "В наличии" if available else "Нет в наличии!"
    
    print(f"Название: {name}")
    print(f"Цена: {price}")
    print(f"Вес: {weight}")
    print(availability)
    print() 
