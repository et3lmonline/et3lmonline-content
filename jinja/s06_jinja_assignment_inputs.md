# Jinja2 Assignment

Giving the below input data:
```py
tables = [
    {
        "name": "cities",
        "is_enables": True,
        "columns_mode": "all",
    },
    {
        "name": "countries",
        "is_enables": True,
        "columns_mode": "select",
        "columns": [
            {"name": "id", "alias": "country_id"},
            {"name": "name", "alias": "country_name"},
            {"name": "continent"},
            {"name": "population"},
            {"name": "updated_at"},
        ],
    },
    {
        "name": "customers",
        "is_enables": True,
        "columns_mode": "all",
        "limit": 25,
    },
    {
        "name": "orders",
        "is_enables": False,
        "columns_mode": "all",
    },
]
```

design a Jinja template that produces a similar output:
```sql
SELECT
    *
FROM cities
```

```sql
SELECT
    id AS country_id,
    name AS country_name,
    continent,
    population,
    updated_at
FROM countries
```

```sql
SELECT
    *
FROM customers
LIMIT 25
```
