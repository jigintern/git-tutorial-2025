CREATE TABLE Hello (
    id INTEGER AUTO_INCREMENT,
    message VARCHAR(16) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(id) REFERENCES User(id)
);

CREATE TABLE User (
    id INTEGER AUTO_INCREMENT,
    name VARCHAR(16) UNIQUE,
    PRIMARY KEY(id),  
);

INSERT INTO Hello(message) VALUES("Hello World!");

SELECT message FROM Hello;
