import json

def read_json(filetxt):
    with open(filetxt, 'r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile)

def write_json(filetxt, data):
    with open(filetxt, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

def add_product():
    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    weight = int(input("Введите вес продукта: "))
    available = input("Продукт в наличии? (да/нет): ").strip().lower() == 'да'
    
    return {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }

def display_products(data):
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

file_path = '10lab2products.json'

data = read_json(file_path)

new_product = add_product()
data['products'].append(new_product)

write_json(file_path, data)

print("Обновленное содержимое файла:")
display_products(data)
