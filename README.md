# 🎓 Student Management System

A full-stack Student Management System built using **Python, Flask, SQLite, HTML, CSS, and JavaScript**. This application allows users to securely log in and perform complete CRUD (Create, Read, Update, Delete) operations on student records stored in a SQLite database.

---

## 🚀 Features

- 🔐 Login Authentication
- 👨‍🎓 View All Students
- ➕ Add New Student
- ✏️ Edit Student Details
- 🗑️ Delete Student
- 💾 SQLite Database Integration
- 🌐 REST API Backend
- 📡 Fetch API Communication
- 📱 Simple and Responsive User Interface

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Fetch API

### Backend
- Python
- Flask

### Database
- SQLite3

### Tools
- Postman
- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```text
Student_Management_System/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── students.html
│   ├── add_student.html
│   └── edit_student.html
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── student_management.db (ignored by Git)
```

---

## 📌 REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/login` | User Login |
| GET | `/students` | Retrieve All Students |
| POST | `/students` | Add a Student |
| PUT | `/students/<id>` | Update Student Details |
| DELETE | `/students/<id>` | Delete a Student |

---

## 🗄️ Database Schema

### Students Table

| Column | Type |
|----------|------|
| id | INTEGER (Primary Key, Auto Increment) |
| name | TEXT |
| age | INTEGER |
| department | TEXT |

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone <your-github-repository-link>
```

### 2. Navigate to the Project

```bash
cd Student_Management_System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧪 Testing

The REST APIs were tested using **Postman**.

Supported operations:

- Login
- Add Student
- Get Students
- Update Student
- Delete Student

---



---

## 📖 What I Learned

Through this project, I gained hands-on experience with:

- Flask Web Development
- REST API Design
- CRUD Operations
- SQLite Database Integration
- SQL Queries
- HTML, CSS and JavaScript
- Fetch API
- JSON Request & Response
- HTTP Methods (GET, POST, PUT, DELETE)
- Git & GitHub Version Control
- API Testing using Postman

---

## 🌱 Future Improvements

- Password Hashing
- User Registration
- Search Students
- Pagination
- Email Validation
- Role-Based Authentication
- Docker Deployment
- Cloud Database (MySQL/MongoDB)

---

## 👩‍💻 Author

**Princy**

B.Sc. Computer Science with Data Science

Passionate about AI, Data Science, Backend Development, and Software Engineering.

GitHub: https://github.com/princy-007
