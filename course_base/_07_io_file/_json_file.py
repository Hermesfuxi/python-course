import json

x = '{ "name":"Bill", "age":63, "city":"Seatle"}'
y = json.loads(x)
print(y)
print(y['name'])

y = {
    "name": "Bill",
    "age": 63,
    "city": "Seatle"
}
x = json.dumps(y)
print(x)
