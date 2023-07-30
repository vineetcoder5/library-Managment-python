# library-Managment-python
Python-based Library Management System: Automates book borrowing, returns, and catalog management. Simple and efficient interface for librarians and users.



The Library Management System is a basic software application designed to facilitate library operations and automate book borrowing and returning processes. The system allows librarians and users to interact with the database to manage books and handle book checkouts and returns. Here is a breakdown of the key features:

Database Connection:
The script establishes a connection to the MySQL database using the mysql.connector module and the provided database credentials (host, user, password, and database name).

Setting Up Borrowing Limits:
The script allows administrators to set up minimum and maximum class levels to borrow books and the maximum number of books a student can borrow at one time.

Book Catalog Management:
The system maintains a catalog of books available in the library. New books can be added to the catalog with details like name, quantity, real quantity (number of available copies), date added, and price charged if the book is damaged.

Book Borrowing and Returning:
Users can search for books in the catalog and check their availability. If a book is available, they can borrow it by providing their name, class, and section. The system updates the book quantity and records the borrowing date and return date.

Not Returned Books Tracking:
The system has a function named notreturn() that checks for books that were not returned on the expected return date. It generates a list of students who have overdue books and stores their information in a table named "notreturned."

Book Return with Code Verification:
Users can return books by entering the code assigned to them when borrowing the book. The script verifies the code, updates the book quantity, and records the return date.

Database Interaction and Data Manipulation:
The script uses SQL queries to interact with the MySQL database. It fetches and inserts data into various database tables based on user actions.
