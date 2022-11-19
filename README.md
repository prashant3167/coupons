# coupons
Create coupon management system



# Decided coupon schema
Coupons
```
{
    coupon_code: str
    rule_id(foreign_key)
    created_on: date
    created_by: integer
    <!-- last_used_on: <date default null>  -->
    expiration_date: date
    used_count: number
}
```

<!-- TODO: Implement min_price -->
coupon_rules

```
{
    rule_id:<str>
    user_group: list of user groups: <optional>
    vaild_coupon: boolean,
    min_price: integer <optional>
    used_by: date,
    created_on: date,
    expiration_date: date
    can_be_used:integer <optional>
    customer_ids: [
            "zyz","abc]  < list of customer_id> <optional,
    absolute: integer <optional>
    percentage: integer <optional>
}
```




# Setup


1. Install python packages.
   > `pip install -r requirements.txt`

2. Make Directory `data` in the git path.

3. To create coupon data run below command.
   >  `python3 src/data_generator.py`