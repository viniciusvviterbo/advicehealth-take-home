CREATE DATABASE IF NOT EXISTS Norktowndb;

CREATE TABLE IF NOT EXISTS Persons(
    id INTEGER NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Cars(
    id INTEGER NOT NULL AUTO_INCREMENT,
    model ENUM('Hatch', 'Sedan', 'Convertible') NOT NULL,
    color ENUM('Yellow', 'Blue', 'Gray') NOT NULL,
    person_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (person_id) REFERENCES Persons(id)
);

CREATE TABLE IF NOT EXISTS Users(
    id INTEGER NOT NULL AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO Persons(firstName, lastName)
VALUES  ('John', 'Doe'),
        ('Jane', 'Doe');

INSERT INTO Cars(model, color, person_id)
VALUES  ('Hatch', 'Yellow', 1),
        ('Sedan', 'Blue', 1);

-- Username 'user' and password 'password_user'
INSERT INTO Users(username, password)
VALUES  ('user', '916b90cfc82f9cf1115c8ab85593b762cfd67307484f8d6f0104e9aecbd4f1bb')