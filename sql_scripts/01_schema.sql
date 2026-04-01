CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    risk_level ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    available_cash DECIMAL(18, 4) DEFAULT 100000.00
);

CREATE TABLE Assets (
    asset_id INT PRIMARY KEY AUTO_INCREMENT,
    ticker VARCHAR(10) NOT NULL UNIQUE,
    asset_name VARCHAR(100),
    sector VARCHAR(50),
    current_price DECIMAL(18, 4)
);

CREATE TABLE Fee_Schedules (
    fee_id INT PRIMARY KEY AUTO_INCREMENT,
    min_amount DECIMAL(18, 2),
    max_amount DECIMAL(18, 2),
    fee_rate DECIMAL(6, 4)
);

CREATE TABLE Positions (
    position_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    asset_id INT,
    avg_cost DECIMAL(18, 4),
    quantity INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (asset_id) REFERENCES Assets(asset_id)
);

CREATE TABLE Transactions (
    trans_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    asset_id INT,
    trans_type ENUM('BUY', 'SELL'),
    quantity INT,
    price DECIMAL(18, 4),
    fee DECIMAL(18, 4),
    trans_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (asset_id) REFERENCES Assets(asset_id)
);


CREATE TABLE Audit_Logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    action_type VARCHAR(50),
    message TEXT,
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Price_History (
    history_id INT PRIMARY KEY AUTO_INCREMENT,
    asset_id INT,
    price_date DATE,
    close_price DECIMAL(18, 4),
    FOREIGN KEY (asset_id) REFERENCES Assets(asset_id)
);


CREATE TABLE Sys_Config (
    cfg_key VARCHAR(50) PRIMARY KEY,
    cfg_value VARCHAR(100)
);