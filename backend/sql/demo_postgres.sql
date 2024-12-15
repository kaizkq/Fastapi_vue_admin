-- PostgreSQL version of demo.sql
-- Database: fastapi_vue_admin

-- Drop tables if they exist
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS "user";

-- Create books table
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    published_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    category VARCHAR(255) NOT NULL
);

-- Create user table
CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    nickname VARCHAR(255),
    avatar VARCHAR(255)
);

-- Add comments to user table
COMMENT ON COLUMN "user".username IS '账号';
COMMENT ON COLUMN "user".password IS '密码';
COMMENT ON COLUMN "user".nickname IS '昵称';
COMMENT ON COLUMN "user".avatar IS '头像url';

-- Insert sample data
BEGIN;

-- Insert books data
INSERT INTO books (id, title, author, published_date, created_at, updated_at, category) VALUES
    (1, '活着', '余华', '1994-06-07', '2024-06-26 15:03:29', '2024-06-26 22:08:42', '余华作品'),
    (2, '红楼梦', '曹雪芹', '2024-06-26', '2024-06-26 22:07:05', '2024-06-26 22:07:05', '古典文学'),
    (3, '三国演义', '罗贯中', '2024-06-26', '2024-06-26 06:09:40', '2024-06-26 14:10:08', '古典文学'),
    (5, '呐喊', '鲁迅', '2024-06-26', '2024-06-27 06:14:27', '2024-06-26 22:14:50', '鲁迅作品'),
    (6, '狂人日记', '鲁迅', '2024-06-26', '2024-06-26 14:15:32', '2024-06-26 14:15:32', '鲁迅作品');

-- Reset books sequence
SELECT setval('books_id_seq', (SELECT MAX(id) FROM books));

-- Insert user data
INSERT INTO "user" (id, username, password, nickname, avatar) VALUES
    (1, 'ggbond', '$2b$12$2vJ8XUTZdTJ3cP1gzq4pWOj5Pu9uVvGioe/OxphMyWZQngsBg4B8m', NULL, NULL),
    (2, 'admin', '$2b$12$3KwQrnPaL7/e3PEA6b0jHOLub7dHMWuhsSBrCxj9O6KX/rbgvMU0O', '萧嫣', NULL),
    (3, 'kkk', '$2b$12$GcshM6Cl/BV.iC2nNrG0P.ctrqYMOB/FvBqEqGoxSdpVqIsWIUj3K', '猪猪', NULL);

-- Reset user sequence
SELECT setval('user_id_seq', (SELECT MAX(id) FROM "user"));

COMMIT;

-- Create trigger for updating updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_books_updated_at
    BEFORE UPDATE ON books
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column(); 