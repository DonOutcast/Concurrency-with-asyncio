CREATE TABLE IF NOT EXISTS user_favorite(
    user_id INT NOT NULL,
    product_id INT NOT NULL
);

INSERT INTO user_favorite
VALUES
(1, 1),
(1, 2),
(1, 3),
(3, 1),
(3, 2),
(3, 3);
