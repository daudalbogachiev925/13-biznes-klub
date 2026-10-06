SELECT m.id, m.name, m.tier, m.monthly_fee,
       COUNT(p.id) AS payments,
       COALESCE(SUM(p.amount),0) AS total_paid,
       MAX(p.paid_at) AS last_payment
FROM members m
LEFT JOIN payments p ON p.member_id = m.id
GROUP BY m.id
ORDER BY total_paid DESC;
