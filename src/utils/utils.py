from datetime import datetime
import time

def cstd(date):
    """Convert string to datetime

    Args:
        date ([string]): String date

    Returns:
        [datetime]: Datetime format date
    """    
    return datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
 

def check_expiry(*args):
    """Check coupon expiry

    Returns:
        [Boolean]: Coupon is expired or not
    """    
    return datetime.now()>min(args)



def check_use_count(used_count, can_be_used):
    """Check coupon is overused

    Args:
        used_count ([integer]): Number of times it is used
        can_be_used ([integer]): Number of times it can be used

    Returns:
        [Boolean]: Is coupon overused
    """    
    return used_count>=can_be_used

def check_customer_details(customer_details, rules):
    """Check coupon is valid for the customer based on tier and id

    Args:
        customer_details ([dict]): Details of customert
        rules ([dict]): Description of rules

    Returns:
        [bool]: is it applicable for the customer
    """    
    # print("Cd",customer_details['tier'] in rules.get("user_group", []))
    if not (rules.get("customer_id", None)==None or rules.get("customer_id", None)==customer_details['username']):
        return False
    if not (rules.get("user_group", None)==None or customer_details['tier'] in rules.get("user_group", [])):
        return False
    return True

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            print("%s :  %2.2f ms" % (method.__name__.replace('_', ' ').upper(), (te - ts) * 1000))
        return result
    return timed