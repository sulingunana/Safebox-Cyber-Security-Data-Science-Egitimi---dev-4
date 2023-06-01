# Safebox-Cyber-Security-Data-Science-Egitimi---dev-4
Safebox Cyber Security Data Science Eğitimi - Ödev 4

Stored Procedure and Trigger are important features used in database systems. Here are their functions and effects:

Stored Procedure:

A stored procedure is a program stored in a database that performs a specific function when called.
It can contain multiple SQL statements, logical structures, and operations.
It is stored as a single unit in the database and can be called multiple times.
As it runs on the database server, it is efficient in terms of network traffic and performance.
It facilitates complex operations by combining business logic and database operations.
From a security perspective, when proper authorization is in place, it can be used to control access to the database.
Positive Effects:

Performance: Stored procedures can run faster as they are precompiled and stored on the database server.
Security: Database administrators can restrict direct execution of queries and grant access only to stored procedures, enhancing database security.
Data Integrity: Stored procedures can be used to ensure data integrity during complex database operations, such as updating multiple tables and performing joins.
Negative Effects:

Development and Maintenance Challenges: Stored procedures tend to be complex and may require more effort during the development process. Maintenance and updates can also become more challenging.
Dependency: Stored procedures can create dependency on the database. This can cause issues when attempting to change or migrate the database platform.
Update Issues: Changes made to stored procedures can impact application compatibility. Therefore, the update process needs to be carefully managed.
Trigger:

A trigger is a function that is automatically executed when a specific event occurs in a database.
The scope of a trigger is the table it is associated with, and it is triggered when a specific event occurs on that table.
It can be used to maintain data integrity, perform automated tasks, and create alerts in a database.
