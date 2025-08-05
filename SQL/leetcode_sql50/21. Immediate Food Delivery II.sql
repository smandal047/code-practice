# Write your MySQL query statement below

with cte as (
    select
    customer_id,
    order_date,
    customer_pref_delivery_date,
    dense_rank() over (partition by customer_id order by order_date asc) rnk
    from Delivery
)


select
    round( sum(case when order_date=customer_pref_delivery_date then 1 else 0 end) * 100 / count(1), 2) as immediate_percentage 
from cte
where rnk = 1