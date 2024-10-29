from jinja2 import Environment

env = Environment()

# Data
customers = [
    {"title": "Mr", "name": "Sabry", "order_number": "123456"},
    {"title": "Eng", "name": "Gad", "order_number": "654321"},
    {"title": "Prof", "name": "Sobhy", "order_number": "987654"},
    {"title": "Ms", "name": "Samar", "order_number": "456789"},
    {"title": "Mr", "name": "Shabrawy", "order_number": "159753"},
    {"title": "Dr", "name": "Nasser", "order_number": "951357"},
    {"title": "Mr", "name": "Mazen"},
]

for customer in customers:
    title = customer.get("title")
    name = customer.get("name")
    order_number = customer.get("order_number")
