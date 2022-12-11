from interface.couchbase_util import Database as CouchBase
from interface.mongo_util import Database as MongoDb
from interface.postgres_util import Database as PostgresDb

from datetime import datetime
from utils.utils import (
    cstd,
    check_expiry,
    check_use_count,
    check_customer_details,
    timeit,
)

couch_connect = CouchBase()
mongo_connect = MongoDb()
postgres_client = PostgresDb()
# couch_connect = None
# mongo_connect = None


@timeit
def verify_coupon(coupon, customer_id, price, db="Mongodb"):
    """Verify coupon and provide the discount applicable

    Args:
        coupon ([str]): Coupon applied
        customer_id ([str]): User
        price ([float]): Total paid value before any discount

    Returns:
        [float]: Discount applicable
    """
    price = float(price)
    db_client = (
        mongo_connect
        if db == "Mongodb"
        else couch_connect
        if db == "CouchBase"
        else postgres_client
    )
    customer_details = db_client.get_customer(customer_id)
    if customer_details is None:
        return "Not a valid customer", None
    coupon_details = db_client.get_coupon(coupon)

    if coupon_details is None:
        return "Coupon not present", None
    # TODO: Add the code for get_customer and create dummy data for customer data
    # customer_details = couch_connect.get_customer(customer_id)
    # Remove: After adding get_customer remove below

    # customer_details = {"id": "sullivanjoe", "name": "Prashant", "phone": "828488423", "tier" : "silver" }

    associated_rule = coupon_details["rule_id"]
    # print(associated_rule)
    rule_details = db_client.get_rule(associated_rule)
    # print(rule_details)
    valid_coupon = True
    if check_expiry(
        cstd(coupon_details["expiration_date"]), cstd(rule_details["expiration_date"])
    ):
        return "Coupon Expired", None
    if check_use_count(coupon_details["used_count"], rule_details["can_be_used"]):
        return "Coupon use already maxed out", None
    if not check_customer_details(customer_details, rule_details):
        return "Coupon is not applicable for you", None
    discounted_price = (
        price * (0.01 * rule_details["percentage"])
        if "percentage" in rule_details.keys()
        else rule_details["absolute"]
    )
    return price - discounted_price, discounted_price


def update_coupon(coupon):
    pass


# print(verify_coupon("black_friday_101BYP", 'sullivanjoe', 200))
