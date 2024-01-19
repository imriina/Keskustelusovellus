CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT,
    admin INT
);

CREATE TABLE rooms (



);

CREATE TABLE posts (


);

CREATE TABLE comments (


);
