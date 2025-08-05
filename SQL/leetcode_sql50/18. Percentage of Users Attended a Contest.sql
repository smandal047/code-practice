# Write your MySQL query statement below

select contest_id, round((count(user_id)/cnt)*100,2) percentage
from register re
join (select count(1) as cnt from users) ct
group by 1
order by 2 desc, 1 asc