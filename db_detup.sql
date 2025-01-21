-- Create Tokens Table
CREATE TABLE tokens (
    id SERIAL PRIMARY KEY,
    token_id VARCHAR(255) UNIQUE NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    directory VARCHAR(255) NOT NULL,
    trigger_url TEXT NOT NULL,
    alert_email VARCHAR(255),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Logs Table
CREATE TABLE token_logs (
    id SERIAL PRIMARY KEY,
    token_id VARCHAR(255) NOT NULL,
    ip_address VARCHAR(255),
    headers JSONB,
    event_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (token_id) REFERENCES tokens (token_id)
);
