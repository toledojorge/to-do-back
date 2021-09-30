 CREATE TABLE person(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
 );

 CREATE TABLE card(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    state boolean not null,
    person_id INT NOT NULL,
        FOREIGN KEY (person_id) REFERENCES person(id)
);