CREATE DATABASE IF NOT EXISTS cours_iot_introduction_python;
use cours_iot_introduction_python;

CREATE TABLE  IF NOT EXISTS user (
    id INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(200),
    lastname VARCHAR(200),
    age INT,
    PRIMARY KEY (id)
);

INSERT INTO user (firstname, lastname, age) VALUES ('Bernard', 'Tessier', 55);

