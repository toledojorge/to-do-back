CREATE TABLE card(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    state boolean not null
)


 CREATE TABLE person(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email UNIQUE VARCHAR(100) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
 )