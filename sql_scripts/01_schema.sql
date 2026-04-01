CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    balance DECIMAL(18, 2) DEFAULT 100000.00
);
CREATE TABLE Assets (
    asset_id INT PRIMARY KEY AUTO_INCREMENT,
    ticker VARCHAR(10) NOT NULL UNIQUE,
    asset_name VARCHAR(100),
    current_price DECIMAL(18, 2)
);
CREATE TABLE Transactions (
    trans_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    asset_id INT,
    quantity INT NOT NULL,
    price_at_exec DECIMAL(18, 2),
    trans_type ENUM('BUY', 'SELL'),
    trans_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (asset_id) REFERENCES Assets(asset_id)
);