-- Write your MySQL query statement below

select
t1.employee_id,
t1.name,
count(1) reports_count,
round(avg(t2.age), 0) average_age
from Employees t1
inner join Employees t2
on t1.employee_id = t2.reports_to 
group by employee_id, name
order by employee_id