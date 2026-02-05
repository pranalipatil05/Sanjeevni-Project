CREATE DATABASE IF NOT EXISTS sanjeevani;
USE sanjeevani;
-- Hospitals Table
CREATE TABLE hospitals (
    hospital_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200),
    address VARCHAR(300),
    city VARCHAR(100),
    rating FLOAT,
    is_24x7 BOOLEAN,
    phone VARCHAR(20)
);
INSERT INTO hospitals (name, address, city, rating, is_24x7, phone) VALUES
('Apollo Hospital', 'Bandra West', 'Mumbai', 4.8, TRUE, '+91-900000001'),
('Fortis Hospital', 'Mulund West', 'Mumbai', 4.6, TRUE, '+91-900000002'),
('Lilavati Hospital', 'Bandra West', 'Mumbai', 4.7, TRUE, '+91-900000003'),
('Hinduja Hospital', 'Mahim', 'Mumbai', 4.5, TRUE, '+91-900000004');
select* from hospitals;

-- Bed Availability Table
CREATE TABLE bed_availability (
    bed_id INT PRIMARY KEY AUTO_INCREMENT,
    hospital_id INT,
    icu_beds INT,
    general_beds INT,
    ventilator_beds INT,
    status VARCHAR(20),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (hospital_id) REFERENCES hospitals(hospital_id)
);
INSERT INTO bed_availability (hospital_id, icu_beds, general_beds, ventilator_beds, status) VALUES
(1, 8, 15, 2, 'Available'),
(2, 2, 12, 0, 'Limited'),
(3, 12, 20, 5, 'Available'),
(4, 0, 3, 0, 'Full');
select * from bed_availability;

-- Blood Inventory Table 
CREATE TABLE blood_inventory ( 
blood_id INT PRIMARY KEY AUTO_INCREMENT, 
hospital_id INT, 
blood_A_pos INT, 
blood_A_neg INT, 
blood_B_pos INT, 
blood_B_neg INT, 
blood_O_pos INT, 
blood_O_neg INT, 
blood_AB_pos INT, 
blood_AB_neg INT, 
last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
FOREIGN KEY (hospital_id) REFERENCES hospitals(hospital_id) 
);
INSERT INTO blood_inventory (hospital_id, blood_A_pos, blood_A_neg, 
blood_B_pos, blood_B_neg, blood_O_pos, blood_O_neg, 
blood_AB_pos, blood_AB_neg) VALUES 
(1, 25, 10, 15, 5, 18, 7, 4, 2), 
(2, 30, 8, 12, 3, 8, 4, 1, 0), 
(3, 35, 12, 20, 8, 22, 10, 15, 5), 
(4, 20, 7, 18, 3, 15, 5, 5, 2);
select* from blood_inventory;

-- Users Table 
CREATE TABLE users ( 
user_id INT PRIMARY KEY AUTO_INCREMENT, 
full_name VARCHAR(200), 
email VARCHAR(200) UNIQUE, 
phone VARCHAR(20), 
password_hash VARCHAR(255) 
);
INSERT INTO users (full_name, email, phone, password_hash)
VALUES
('Rahul Sharma', 'rahul.sharma@example.com', '9876543210', 'hash12345'),
('Priya Verma', 'priya.verma@example.com', '9123456780', 'hash67890'),
('Amit Patel', 'amit.patel@example.com', '9988776655', 'hashabc12'),
('Sneha Kapoor', 'sneha.kapoor@example.com', '9090909090', 'hashxyz34'),
('Rohan Mehta', 'rohan.mehta@example.com', '8800112233', 'hashpass56');
select* from users;

-- Contact Messages Table 
CREATE TABLE contact_messages ( 
message_id INT PRIMARY KEY AUTO_INCREMENT, 
first_name VARCHAR(100), 
last_name VARCHAR(100), 
email VARCHAR(200), 
phone VARCHAR(20), 
department VARCHAR(100), 
message TEXT, 
submitted_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);
INSERT INTO contact_messages 
(first_name, last_name, email, phone, department, message)
VALUES
('Rahul', 'Sharma', 'rahul.sharma@example.com', '9876543210', 'Support', 'I need help accessing my account.'),
('Priya', 'Verma', 'priya.verma@example.com', '9123456780', 'Sales', 'I want to know more about your service plans.'),
('Amit', 'Patel', 'amit.patel@example.com', '9988776655', 'Technical', 'I am facing an issue with the app loading screen.'),
('Sneha', 'Kapoor', 'sneha.kapoor@example.com', '9090909090', 'Billing', 'Please send me the invoice for last month.'),
('Rohan', 'Mehta', 'rohan.mehta@example.com', '8800112233', 'General Inquiry', 'How can I update my profile details?');
select* from contact_messages;
SHOW TABLES;