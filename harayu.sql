CREATE TABLE Hello (
    id INTEGER AUTO_INCREMENT,
    message VARCHAR(16) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO Hello(message) VALUES("Hello World!");

SELECT message FROM Hello;
