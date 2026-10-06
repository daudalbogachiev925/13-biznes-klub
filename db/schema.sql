CREATE TABLE members (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    tier TEXT CHECK (tier IN ('basic','silver','gold','platinum')),
    joined DATE DEFAULT CURRENT_DATE,
    monthly_fee NUMERIC(10,2),
    status TEXT DEFAULT 'active'
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    date TIMESTAMP NOT NULL,
    place TEXT,
    price NUMERIC(10,2) DEFAULT 0,
    capacity INT
);

CREATE TABLE attendance (
    member_id BIGINT REFERENCES members(id),
    event_id INT REFERENCES events(id),
    visited BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (member_id, event_id)
);

CREATE TABLE payments (
    id BIGSERIAL PRIMARY KEY,
    member_id BIGINT REFERENCES members(id),
    amount NUMERIC(10,2),
    kind TEXT CHECK (kind IN ('monthly','event','entry')),
    paid_at DATE DEFAULT CURRENT_DATE
);

CREATE INDEX idx_payments_member ON payments(member_id);
CREATE INDEX idx_attendance_member ON attendance(member_id);
