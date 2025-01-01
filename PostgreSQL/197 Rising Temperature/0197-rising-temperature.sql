-- Write your PostgreSQL query statement below
SELECT today.id
FROM Weather yesterday INNER JOIN Weather today
  ON today.recordDate - 1 = yesterday.recordDate AND
     yesterday.temperature < today.temperature