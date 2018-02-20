CREATE DATABASE IF NOT EXISTS cours_iot_python_pour_le_web;
use cours_iot_python_pour_le_web;

CREATE TABLE  IF NOT EXISTS user (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(500),
    password VARCHAR(200),
    is_admin BOOLEAN,
    PRIMARY KEY (id)
);

CREATE TABLE  IF NOT EXISTS entries (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(200),
    value VARCHAR(2000),
    PRIMARY KEY (id)
);

INSERT INTO user (email, password, is_admin) VALUES ('someone@yopmail.com', '$argon2i$v=19$m=512,t=2,p=2$07qXMsb4P4fQ+p9T6l3rvQ$hWU817VMNDP/E9l21rYOKQ', true);
INSERT INTO entries (name, value) VALUES ('slogan', 'Mangez des pommes !');

