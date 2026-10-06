SELECT m.id, m.name, m.tier, m.monthly_fee,
       MAX(p.paid_at) AS last_payment,
       CURRENT_DATE - MAX(p.paid_at) AS days_inactive
FROM members m
LEFT JOIN payments p ON p.member_id = m.id
WHERE m.status = 'active'
GROUP BY m.id
HAVING MAX(p.paid_at) < CURRENT_DATE - INTERVAL '60 days'
    OR MAX(p.paid_at) IS NULL
ORDER BY days_inactive DESC;
