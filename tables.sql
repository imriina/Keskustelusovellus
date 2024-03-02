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

CREATE TABLE post (
    post_id SERIAL PRIMARY KEY,
    room_id INT NOT NULL,
    maker_id INT NOT NULL,
    header TEXT NOT NULL
    content TEXT NOT NULL,
    time TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
    FOREIGN KEY (maker_id) REFERENCES users(id) ON DELETE CASCADE     
);

CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    post_id INT NOT NULL,
    maker_id INT NOT NULL,
    content TEXT NOT NULL,
    time TIMESTAMP,
    FOREIGN KEY (maker_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES post(post_id) ON DELETE CASCADE
);

CREATE TABLE savedposts  (
    saved_post_id SERIAL PRIMARY KEY,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post(post_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE  
);