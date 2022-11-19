import random
import uuid
from faker import Faker
import json
from datetime import datetime, timedelta

seed = "1"
fake = Faker()
fake.seed_instance(int(seed))
random.seed(int(seed))


fake.date_time_between
coupons_prefix = ["coupon", "ulb", "special", "sale", "black_friday"]
coupon_rules = []
coupon_rule_coupon_count = 1
coupon_creators = ["SYSTEM", "Prashant", "Abdal", "Maren", "Lalit"]
coupons = []
customers = []
files_location = "data"
fake_datetime = lambda: fake.date_time_between(start_date="-180d", end_date="+180d")
GLOBAL_OVERWRITE_TO_FILE = True


def coupon_id_generator(count, prefix):
    """Create unique ids for coupons

    Args:
        count ([integer]): Number of characters for suffix
        prefix ([string]): coupon prefix
    Returns:
        [string]: Coupon Id
    """
    code_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code_chars = [*code_chars]
    suffix = "".join(random.sample(code_chars, count))
    return f"{prefix}_{seed}{suffix}"
    pass


def write_to_file(data, file_name, to_file=True):
    """Write json data to file

    Args:
        data ([dict]): output to be written in file
        file_name ([string]): Name of the file
        to_file (bool): Check for wrtting in file. Defaults to True.
    """
    if not to_file:
        return
    with open(f"data/{file_name}_{seed}.json", "w") as outfile:
        json.dump(data, outfile, indent=4, default=str)


def create_customers(count):
    """Create customers for coupons

    Args:
        count ([integer]): Customer count
    """
    for i in range(count):
        customers.append(fake.user_name())
    write_to_file(customers, "customers")


def create_coupons(count):
    """Create coupons for dump

    Args:
        count ([integer]): Coupon count
    """
    rule_length = len(coupon_rules)
    for i in range(count):
        select_rule = random.randint(0, rule_length - 1)
        coupon = {
            "code": coupon_id_generator(
                random.randint(5, 8), random.choice(coupons_prefix)
            ),
            "rule_id": coupon_rules[select_rule]["rule_id"],
            "created_on": fake.date_time_between_dates(
                coupon_rules[select_rule]["created_on"],
                coupon_rules[select_rule]["created_on"] + timedelta(days=20),
            ),
            "created_by": random.choice(coupon_creators),
            "used_count": random.randint(
                0, coupon_rules[select_rule]["can_be_used"] + 1
            ),
        }
        coupon["expiration_date"] = fake.date_time_between_dates(
            coupon["created_on"] + timedelta(days=1),
            coupon["created_on"] + timedelta(days=20),
        )
        coupons.append(coupon)
    write_to_file(coupons, "coupons", GLOBAL_OVERWRITE_TO_FILE)


def create_coupon_rules(count):
    """Create coupon rules for dump

    Args:
        count ([integer]): Coupon Rule count
    """
    coupon_user_group = ["gold", "silver", "bronze"]
    coupon_rule_types = [1, 2, 3]
    for i in range(count):
        select_coupon_type = random.randint(1, 4)
        coupon_rule = {
            "rule_id": f"rule_{seed}_{str(uuid.uuid4())}",
            "expiration_date": fake_datetime(),
            "valid_coupon": bool(random.getrandbits(1)),
            f"{'absolute' if bool(random.getrandbits(1)) else 'percentage'}": random.randint(
                1, 80
            ),
            "can_be_used": random.randint(100, 1000),
        }
        if select_coupon_type == 1:
            coupon_rule["customer_id"] = random.choice(customers)
            coupon_rule["can_be_used"] = 1
        elif select_coupon_type == 2:
            coupon_rule["user_group"] = random.choices(coupon_user_group, k=2)
        coupon_rule["created_on"] = coupon_rule["expiration_dae"] - timedelta(days=120)
        coupon_rules.append(coupon_rule)
    write_to_file(coupon_rules, "coupon_rules", GLOBAL_OVERWRITE_TO_FILE)


if __name__ == "__main__":
    number_of_rules = 10000
    number_of_coupons = 10000000
    customer_count = 10000
    print("customers")
    create_customers(customer_count)
    print("rules")
    create_coupon_rules(number_of_rules)
    print("coupons")
    create_coupons(number_of_coupons)
    print("end")
