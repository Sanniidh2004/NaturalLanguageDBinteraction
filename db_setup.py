import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="labuser",      
    password="lab123"    
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS nl_db")
cursor.execute("USE nl_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50)
)
""")

cursor.execute("TRUNCATE TABLE students")

cursor.execute("""
INSERT INTO students (name, age, department) VALUES
('Amit', 20, 'CSE'),
('Riya', 21, 'IT'),
('Rahul', 22, 'ECE'),
('Sneha', 20, 'CSE')
""")

conn.commit()
conn.close()

print("Database and sample data created successfully")