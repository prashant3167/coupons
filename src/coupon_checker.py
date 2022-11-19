from interface.couchbase_util import Database
from datetime import datetime
from utils.utils import cstd , check_expiry, check_use_count, check_customer_details

couch_connect = Database()
# mongo_connect = Database()




def verify_coupon(coupon, customer_id, price):
    """Verify coupon and provide the discount applicable

    Args:
        coupon ([str]): Coupon applied
        customer_id ([str]): User 
        price ([float]): Total paid value before any discount

    Returns:
        [float]: Discount applicable
    """    
    coupon_details = couch_connect.get_coupon(coupon).value
    print(coupon_details)
    if coupon_details is None:
        return "Coupon not present"
    # TODO: Add the code for get_customer and create dummy data for customer data
    # customer_details = couch_connect.get_customer(customer_id)
    # Remove: After adding get_customer remove below

    customer_details = {"id": "sullivanjoe", "name": "Prashant", "phone": "828488423", "tier" : "silver" }
    associated_rule = coupon_details["rule_id"]
    print(associated_rule)
    rule_details = couch_connect.get_rule(associated_rule)
    print(rule_details)
    valid_coupon = True
    if check_expiry(cstd(coupon_details["expiration_date"]),cstd(rule_details.value["expiration_dae"])):
        return "Coupon Expired"
    if check_use_count(coupon_details["used_count"], rule_details.value["can_be_used"]):
        return "Coupon use already maxed out"
    if not check_customer_details(customer_details, rule_details.value):
        return "Coupon is not applicable for you"
    discounted_price = price * (0.01 * rule_details.value['percentage']) if 'percentage' in rule_details.value.keys() else rule_details.value['absolute']
    return price - discounted_price,discounted_price
        




def update_coupon(coupon):
    pass



# print(verify_coupon("black_friday_101BYP", 'sullivanjoe', 200))

