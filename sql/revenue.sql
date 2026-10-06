SELECT date_trunc('month', paid_at) AS month,
       SUM(amount) AS revenue,
       COUNT(DISTINCT member_id) AS paying_members,
       SUM(amount) FILTER (WHERE kind='monthly') AS monthly,
       SUM(amount) FILTER (WHERE kind='event') AS events
FROM payments
GROUP BY month
ORDER BY month;
