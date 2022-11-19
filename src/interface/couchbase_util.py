from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions, QueryOptions
import couchbase.exceptions
import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            print("%r  %2.2f ms" % (method.__name__, (te - ts) * 1000))
        return result
    return timed


class Database:
    def __init__(self, username="admin", password="dbpasss", host="127.0.0.1", db="test") -> None:
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
            return self.connect.scope("_default").collection("rules").get(rule_id)
        except couchbase.exceptions.DocumentNotFoundException:
            print("Rule not found")
            return None

    @timeit
    def get_coupon(self, coupon):
        try:
            return self.connect.scope("_default").collection("coupons").get(coupon)
        except couchbase.exceptions.DocumentNotFoundException:
            print("Coupon not found")
            return None    

    
