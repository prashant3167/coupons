
from utils.utils import timeit
from psycopg2  import connect



class Database:
    def __init__(self, username="admin", password="admin@123", host="127.0.0.1", db="coupon_system") -> None:
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.connect()

    def connect(self):
      self.connect = connect(host=self.host, user=self.username, password=self.password,database = self.db,port= "5433")


    @timeit
    def get_rule(self, rule_id):
      cur  = self.connect.cursor()
      cur = cur.execute(f"""select * from coupon_rules where coupon_rules->>'rule_id'='{rule_id}';""")
      return cur.fetchone()[0]

    @timeit
    def get_coupon(self, coupon):
      cur  = self.connect.cursor()
      cur.execute(f"""select * from coupons where coupon->>'code'='{coupon}';""")
      return cur.fetchone()[0] 
    
    @timeit
    def get_customer(self, username):
      cur  = self.connect.cursor()
      cur.execute(f"""select * from customers where customers->>'username'='{username}';""")
      return cur.fetchone()[0]