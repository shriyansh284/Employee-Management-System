## Employee Management System (EMS)

**Overview:**
The Employee Management System (EMS) is a comprehensive software solution designed to streamline the management of employee data, enhancing productivity and operational efficiency. Developed in Python, the EMS utilizes Tkinter for its graphical user interface (GUI), providing a user-friendly experience. The integration of CustomTkinter enhances the visual appeal with modern UI elements.

**Key Features:**
- **Employee Information Management:** Easily manage details such as employee code, designation, name, date of birth, and experience.
- **Data Entry and Editing:** Intuitive fields for inputting and updating employee information.
- **Attendance Tracking:** Monitor attendance to ensure accurate payroll processing.
- **Report Generation:** Generate detailed reports on employee data.
- **User-Friendly Interface:** Streamlined navigation for enhanced user experience.
- **Customizable Options:** Tailor the system to meet organizational needs.

**Technology Stack:**
- **Programming Language:** Python
- **GUI Framework:** Tkinter and CustomTkinter
- **Database Management:** MySQL, accessed via the MySQL Connector library.

**Purpose:**
The EMS aims to simplify employee information management, reducing manual errors and ensuring critical data is readily accessible. It serves as a practical application for students and developers to explore database management, GUI design, and application logic in Python.

## Installation and Working Process for Employee Management System (EMS)

### Prerequisites
- **Python (3.x)**: Download from the [official Python website](https://www.python.org/).
- **MySQL Database**: Install from the [official MySQL site](https://www.mysql.com/).
- **MySQL Connector for Python**: Install via pip:
  ```bash
  pip install mysql-connector-python
  ```

### Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Robinrai2612/Employee_Management_System.git
   cd Employee_Management_System
   ```

2. **Update MySQL Connection:**
   Modify the connection details in your Python script:
   ```python
   con = mysql.connector.connect(
       host="localhost",
       user="root",
       password="your_root_password",
       database="employee"
   )
   ```

### Database Setup

1. **Log in to MySQL:**
   ```bash
   mysql -u root -p
   ```

2. **Create Database and Table:**
   ```sql
   CREATE DATABASE employee;
   USE employee;
   CREATE TABLE empdata (
       Id INT PRIMARY KEY,
       Name VARCHAR(255),
       Email_Id VARCHAR(255),
       Phone_no VARCHAR(15),
       Address VARCHAR(255),
       Post VARCHAR(255),
       Salary FLOAT
   );
   ```

### Running the Application

Run the EMS with:
```bash
python employee_management_system.py
```

### Usage

The application allows you to:
- **Add Employees**: Input details like name, email, and salary.
- **Display Records**: View all employee information.
- **Update Information**: Modify existing records.
- **Promote Employees**: Adjust salaries.
- **Remove Records**: Delete employees as needed.
- **Search Functionality**: Find records by ID.

This setup provides an efficient tool for managing employee information in any organization.
