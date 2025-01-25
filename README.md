# CRM Backend System - My Project

This project represents my work on building the backend for a basic Customer Relationship Management (CRM) application.  I focused on creating a scalable, secure, and well-documented API to handle core CRM functionalities.

## Features I Implemented

* **Customer Management:** I've created APIs that allow for full CRUD (Create, Read, Update, Delete) operations on customer data. Each customer record includes fields for name, email, phone number, and optional company affiliation. I also included automatic timestamps for `created_at` and `updated_at` to track changes.
* **User Authentication:**  I implemented a robust user authentication system using password hashing for security and JWT (JSON Web Token) based authentication to protect API endpoints.  This ensures that only authorized users can access and modify customer data.  Users can register and log in through dedicated API endpoints.
* **Database Integration:** I chose PostgreSQL as the database for this project (you can adapt the instructions for your preferred database). I designed the database schema with efficiency and data integrity in mind, establishing appropriate relationships between tables (e.g., customers and users).  You'll find the schema details below.
* **Search and Filtering:** To make the CRM practical, I added an API endpoint to search for customers based on their name, email, or phone number.  Additionally, I implemented filtering capabilities so users can easily retrieve customers associated with a specific company.
* **Error Handling and Validation:** I paid close attention to data validation, ensuring that required fields are present and that data formats are correct (e.g., valid email addresses). I also implemented comprehensive error handling to provide informative error messages and appropriate HTTP status codes.
* **API Documentation:**  I've documented the API thoroughly using Swagger/OpenAPI (or your preferred tool – replace if needed).  This documentation makes it easy to understand how to use the API and explore its various endpoints.  You can find a link to the interactive documentation below.
* **(Optional) Pagination:**  I added pagination to the customer list API to improve performance when dealing with large datasets.  This allows clients to retrieve customer data in manageable chunks.
* **(Optional) Role-Based Access Control:**  For added security and control, I've implemented role-based access control. This distinguishes between regular users and administrators, granting different permissions based on their roles.
* **(Optional) Interaction Logging:**  I included APIs to log and retrieve customer interactions, such as notes, follow-up reminders, or other relevant activities.  This adds a valuable layer of functionality to the CRM.
﻿# CRM
 
 *Live link - https://basic-crm-app.onrender.com*

UserName:ravi21
Password:inventory@123
