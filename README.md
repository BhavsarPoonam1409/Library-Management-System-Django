# 📚 Library Management System

A simple **Library Management System** developed using Python and Django as part of a practical assignment. This project helps manage books, student records, and book issuing and returning.

## 🚀 Features

### 📖 Book Management

* Add new books with book name, author, category, ISBN, and quantity.
* View all available books.
* Edit and delete book records.

### 👨‍🎓 Student Management

* Add student details such as name, enrollment number, and course.
* View all registered students.
* Edit and delete student records.

### 📋 Book Issue and Return

* Issue books to registered students.
* Record issue dates and return dates.
* View all issued books and their current status.
* Return books and update their availability.

### 🎨 User Interface

* Common header and footer using Django templates.
* CSS styling for a clean and user-friendly interface.
* Navigation between different pages.

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML**
* **CSS**
* **SQLite**
* **Django ORM**
* **Django ModelForms**

## 📂 Project Structure

```text
Qus3_Library_Management_System/
│
├── LibraryManagement/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── library/
│   ├── migrations/
│   ├── templates/
│   │   └── library/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── book_list.html
│   │       ├── book_form.html
│   │       ├── student_list.html
│   │       ├── student_form.html
│   │       ├── issue_list.html
│   │       └── issue_form.html
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── static/
│   └── css/
│       └── style.css
│
├── manage.py
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Library-Management-System-Django.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Open the Project Folder

```bash
cd Library-Management-System-Django
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

## 🗄️ Database Models

The project uses three main models:

* **Book:** Stores book details and available quantity.
* **Student:** Stores student information.
* **IssueBook:** Stores book issue records, issue dates, return dates, and current status.

## 🎯 Learning Objectives

This project demonstrates the practical use of:

* Django Models and ORM
* Django ModelForms
* CRUD operations
* URL routing and views
* Django templates and template inheritance
* Static CSS files
* Relationships between database models
* Book issue and return management

## 👩‍💻 Author

**Poonam Bhavsar**

---

*This project was developed for academic practical work to understand Django web development and database management.*
