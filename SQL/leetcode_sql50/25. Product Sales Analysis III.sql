-- my code
with cte as (
    select product_id, 
    year first_year,
    quantity, 
    price,
    dense_rank() over (partition by product_id order by year) rnk
    from sales
)

select product_id, 
    first_year,
    quantity, 
    price
from cte where rnk = 1

--- more efficient code
WITH FirstYearSales AS (
  SELECT 
    product_id,
    MIN(year) AS first_year
  FROM Sales
  GROUP BY product_id
)

SELECT 
  s.product_id, 
  s.year AS first_year, 
  s.quantity, 
  s.price
FROM 
  Sales s
JOIN 
  FirstYearSales f 
  ON s.product_id = f.product_id AND s.year = f.first_year;