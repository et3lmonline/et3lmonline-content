from jinja2 import Environment, FileSystemLoader, StrictUndefined

env = Environment(
    loader=FileSystemLoader("templates"),
    undefined=StrictUndefined,
)

email_template_string = env.get_template("emails/02_detailed.md")

orders = [
    {
        "customer_name": "gad",
        "date": "2024-01-01",
        "order_number": "147852",
        "items": [
            {"name": "Mastering Python", "price": 123.32},
            {"name": "FastAPI From Zero to Hero in 30 Minutes 😎😎😎", "price": 123.32},
            {"name": "Dimensional Modeling - Star Schema", "price": 123.32},
            {"name": "dbt Fundamentals", "is_gift": True},
        ],
    },
    {
        "customer_name": "emad",
        "date": "2024-09-11",
        "order_number": "197012",
        "items": [
            {"name": "Microsoft Excel - Tips & Tricks", "price": 123.32},
            {"name": "Power BI - DAX", "price": 123.32},
        ],
    },
]


for order in orders:
    order_number = order.get("order_number")
    order_date = order.get("date")
    items = order.get("items")
    name = order.get("customer_name")
