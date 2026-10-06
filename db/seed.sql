INSERT INTO members (name, email, tier, monthly_fee) VALUES
('Иван Петров','ivan@x',  'gold',     15000),
('Анна Смирнова','anna@x','silver',   8000),
('Сергей Иванов','sergey@x','platinum',30000),
('Мария Кузнецова','maria@x','basic', 3000);

INSERT INTO events (title, date, place, price, capacity) VALUES
('Нетворкинг-завтрак','2024-02-10 09:00','Москва',0,50),
('Мастер-класс по продажам','2024-02-15 18:00','Москва',5000,30),
('Конференция лидеров','2024-03-01 10:00','СПб',15000,100);

INSERT INTO attendance (member_id, event_id) VALUES
(1,1),(1,2),(2,1),(3,1),(3,3),(4,2);

INSERT INTO payments (member_id, amount, kind, paid_at) VALUES
(1,15000,'monthly','2024-01-01'),(1,15000,'monthly','2024-02-01'),
(2,8000,'monthly','2024-01-05'),
(3,30000,'monthly','2024-01-01'),(3,30000,'monthly','2024-02-01'),
(4,3000,'monthly','2024-01-10');
