# coupons
Create coupon management system



# Decided coupon schema
Coupons
{
    coupon_code: str
    rule_id(foreign_key)
    created_on: date
    created_by: integer
    <!-- last_used_on: <date default null>  -->
    expiration_date: date
    used_count: number
}


coupon_rules
{
    rule_id:<str>
    user_group: list of user groups: <optional
    vaild_coupon: boolean
    used_by: date,
    created_on: date,
    expiration_date: date
    can_be_used:integer <optional>
    customer_ids: [
            "zyz","abc]  < list of customer_id> <optional,
    absolute: integer <optional>
    percentage: integer <optional>
}