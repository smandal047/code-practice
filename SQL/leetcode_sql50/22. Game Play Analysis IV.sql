# Write your MySQL query statement below
with cte as (
    select player_id,
    event_date,
    lead(event_date, 1) over (partition by player_id order by event_date) nxt_event_date,
    dense_rank() over (partition by player_id order by event_date) rnk
    from activity
)

select 
round(count(player_id) / (select count(distinct player_id) from activity),2) fraction 
from cte
where rnk = 1 and datediff(nxt_event_date, event_date) = 1
