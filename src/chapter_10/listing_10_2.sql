CREATE TABLE IF NOT EXISTS user_cart(
    user_id INT NOT NULL,
    product_id INT NOT NULL
);

INSERT INTO user_cart
VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 2),
(2, 5);


