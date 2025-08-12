# Write your MySQL query statement below

with cte_dual as (
    select 
    *
    from employee
    where primary_flag= 'Y'
)
, cte_uno as (
    select
    *,
    count(employee_id) cnt
    from employee
    group by employee_id
    having cnt = 1
)

select employee_id, department_id from cte_uno
union all
select employee_id, department_id from cte_dual