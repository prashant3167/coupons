from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions, QueryOptions
import couchbase.exceptions
from utils.utils import timeit




class Database:
    def __init__(self, username="admin", password="admin@123", host="127.0.0.1", db="coupon_system") -> None:
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.connect()

    def connect(self):
        self.connect = Cluster.connect(
            f"couchbase://{self.host}?ssl=no_verify&tcp_keepalive=true",
            ClusterOptions(PasswordAuthenticator(self.username, self.password)),
        ).bucket(self.db)

    @timeit
    def get_rule(self, rule_id):
        try:
            return self.connect.scope("_default").collection("coupon_rules").get(rule_id).value
        except couchbase.exceptions.DocumentNotFoundException:
            # print("Rule not found")
            return None

    @timeit
    def get_coupon(self, coupon):
        try:
            return self.connect.scope("_default").collection("coupons").get(coupon).value
        except couchbase.exceptions.DocumentNotFoundException:
            # print("Coupon not found")
            return None    

    @timeit
    def get_customer(self, username):
        try:
            return self.connect.scope("_default").collection("customers").get(username).value
        except couchbase.exceptions.DocumentNotFoundException:
            # print("Coupon not found")
            return None   
