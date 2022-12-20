from sqlalchemy import create_engine
from urllib.parse import quote_plus
import json
engine = create_engine('postgresql://{}:%s@127.0.0.1:5433/coupon_system' % quote_plus("{}"))

import psycopg2

with open('data/coupon_rules_3.json', 'r') as f:
    coupon_data = json.load(f)

for i in coupon_data:
    engine.execute(f"""insert into coupon_rules values ('{json.dumps(i)}');""")

with open('data/customers_3.json', 'r') as f:
    customer_data = json.load(f)

for i in customer_data:
    engine.execute(f"""insert into customers values ('{json.dumps(i)}');""")