-- Create the friends table
CREATE TABLE IF NOT EXISTS friends (
    phone_number VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    surname VARCHAR(100),
    address TEXT,
    date_created TIMESTAMP DEFAULT current_timestamp,
    birthday DATE,
    remark TEXT
);

-- Create the events table
CREATE TABLE IF NOT EXISTS events (
    event_id SERIAL PRIMARY KEY,
    friend_phone_number VARCHAR(20),
    event_date DATE,
    summary TEXT,
    keyword1 VARCHAR(50),
    keyword2 VARCHAR(50),
    keyword3 VARCHAR(50),
    keyword4 VARCHAR(50),
    keyword5 VARCHAR(50),
    file_location TEXT,
    FOREIGN KEY (friend_phone_number) REFERENCES friends(phone_number)
);

-- Create the children table
CREATE TABLE IF NOT EXISTS children (
    child_id SERIAL PRIMARY KEY,
    friend_phone_number VARCHAR(20),
    date DATE,
    description TEXT,
    amount DECIMAL(10, 2),
    remark TEXT,
    FOREIGN KEY (friend_phone_number) REFERENCES friends(phone_number)
);

-