#!mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'root123';FLUSH PRIVILEGES;"
#!mysql -u root -p'root123' -e "CREATE DATABASE mydatabase;"
#!mysql -u root -p'root123' -e "USE mydatabase; CREATE TABLE attendance (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, time TIME NOT NULL, PRIMARY KEY (id));"

!mysql -u root -p'root123' -e "USE mydatabase; INSERT INTO attendance (name, time) VALUES (' Doe', '08:30:00');"
!mysql -u root -p'root123' -e "USE mydatabase; select * from attendance;"