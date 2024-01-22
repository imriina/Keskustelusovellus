CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT,
    admin INT
);

CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    topic TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP


);

CREATE TABLE posts (


);

CREATE TABLE comments (


);
