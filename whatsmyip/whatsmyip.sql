CREATE DATABASE IF NOT EXISTS whatsmyip;

use whatsmyip;

CREATE TABLE ips (
    id INT AUTO_INCREMENT PRIMARY KEY,
    public_ip VARCHAR(255) NOT NULL,
    local_ip VARCHAR(255) NOT NULL,
    hostname VARCHAR(255) NOT NULL,
    at DATETIME
) ;
