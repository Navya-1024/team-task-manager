 Task Manager Web Application

 Project Overview

This is a Task Manager web application developed using Flask and SQLAlchemy.
It allows users to register, login, create projects, assign tasks, and track their completion status.

 Features

* User Signup and Login
* Dashboard with task summary
* Create and manage projects
* Assign tasks to users
* Track task status (Pending / Completed)

 Technologies Used

* Python
* Flask (Web Framework)
* SQLAlchemy (ORM)
* SQLite (Database)
* HTML, CSS (Frontend)

 Installation & Setup

 1. Clone the repository

```bash
git clone <your-repo-link>
cd task-manager
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

 3. Run the application

```bash
python app.py
```

 4. Open in browser

```
http://127.0.0.1:5000/
```

 Deployment

The application is deployed using a cloud platform and accessible via a public URL.

---
 Project Structure

```
task-manager/
│── app.py
│── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── create_project.html
│   ├── create_task.html
│── static/
│── database.db
│── README.md
```
 Future Enhancements

* Password encryption for security
* Role-based access control
* Notifications for task updates
* Integration with PostgreSQL
* Improved UI design

 Author

Developed as a assignment submission.

---
