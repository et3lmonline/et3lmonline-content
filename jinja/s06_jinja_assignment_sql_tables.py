from jinja2 import Environment, FileSystemLoader, StrictUndefined

env = Environment(
    loader=FileSystemLoader("templates"),
    undefined=StrictUndefined,
)

email_template_string = env.get_template("sql/select.sql")

tables = []


for order in tables:
    pass
