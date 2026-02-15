CREATE USER 'labuser'@'localhost' IDENTIFIED BY 'lab123';
GRANT ALL PRIVILEGES ON nl_db.* TO 'labuser'@'localhost';
FLUSH PRIVILEGES;