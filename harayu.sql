CREATE DATABASE Temp;

USE Temp;

CREATE TABLE User (
    id INTEGER AUTO_INCREMENT,
    name VARCHAR(16) UNIQUE,
    PRIMARY KEY(id)
);

CREATE TABLE Hello (
    id INTEGER AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    message VARCHAR(16) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(id) REFERENCES User(id)
);

INSERT INTO User(name) VALUES("test");
INSERT INTO Hello(user_id, message) VALUES(1, "Hello World!");

SELECT message FROM Hello;


DROP DATABASE Temp;
