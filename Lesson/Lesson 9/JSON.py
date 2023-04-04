# Парсинг JSON - преобразование из JSON в Python
import json

# some JSON
x = '{"name": "Alex", "age": 20, "city": "Falesti"}'

# parse x
y = json.loads(x)

# the result is a Python dictionary
print(y["age"])

# a Python object (dict):
x = {
    "name": "Mihai",
    "age": 21,
    "city": "chisinau"
}

# convert into JSON
y = json.dumps(x)

# the result is a JSON string
print(y)

# При преобразовании из Python в JSON объекты Python преобразуются в эквивалент JSON (JavaScript):
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Преобразуем объект Python,который содержит все допустимые типы данных:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars":[
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))