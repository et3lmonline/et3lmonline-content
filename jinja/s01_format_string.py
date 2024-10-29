message_01 = "Table has been loaded successfully"

table_name = "customers"
message_02 = f"Table {table_name} has been loaded successfully"
message_03 = "Table {table_name} has been loaded successfully".format(
    table_name=table_name
)


print("message 01:", message_01)
print("message 02:", message_02)
print("message 03:", message_03)

with open("templates/emails/00_simple_not_jinja.txt", "r", encoding="utf-8") as f:
    template = f.read()

message_04 = """Dear {title} {name},
Kindly be noted that your order {order_number} has been processed.""".format(
    title="dr",
    name="Nasser",
    order_number=951357,
)
print("message 04:", message_04)
