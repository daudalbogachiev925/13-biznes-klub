SELECT e.id, e.title, e.date, e.place, e.capacity,
       COUNT(a.member_id) AS visitors,
       ROUND(100.0 * COUNT(a.member_id) / e.capacity, 1) AS fill_pct
FROM events e
LEFT JOIN attendance a ON a.event_id = e.id AND a.visited
GROUP BY e.id
ORDER BY e.date DESC;
