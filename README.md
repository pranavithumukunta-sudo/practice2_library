# My Book Library – Django Database Website
**Django Lab Exercise 8 | Introduction to Python**

A complete, clean, database-driven Book Library web application built using Python, Django, SQLite, and HTML templates, following the **Django Practice Manual 2 – Database Website** specifications.

---

## 📖 Description
This project demonstrates how Django connects web pages to a relational database using the **MVT (Model-View-Template)** architecture. Unlike static websites where content is hardcoded into HTML files, this website dynamically retrieves book records from an SQLite database and presents them in an organized table. Users can view the book collection, add new books through an HTML form that validates input and persists records, and manage all records through the built-in Django Admin interface.

---

## 🛠️ Technologies Used
- **Python 3.12+** (Programming Language)
- **Django** (High-level Python Web Framework)
- **SQLite3** (`db.sqlite3` – Default Relational Database)
- **HTML5 & CSS3** (Frontend presentation and clean responsive design)
- **Django Templates Engine (DTL)** (Dynamic template rendering)
- **Django ModelForm** (Automated form creation and validation)
- **VS Code** (Integrated Development Environment)
- **Git & GitHub** (Version control)

---

## ✨ Features
1. **Database-Driven Storage**: Books are persisted directly in SQLite database via Django ORM.
2. **Dynamic Listing (`/`)**: Displays the total count of books, row indices, book titles, authors, publishing years, and availability status.
3. **Add Book Form (`/add/`)**: Easy-to-use form with validation and CSRF security token that saves records directly to the database and redirects to the listing page.
4. **Django Admin Site (`/admin/`)**: Full CRUD (Create, Read, Update, Delete) capability with custom column displays (`list_display`).
5. **Clean & Professional UI**: Styled with responsive, centered layout, clear typography, intuitive buttons, and status badges.
6. **Automated Unit Tests**: Built-in test suite verifying models, views, and form behaviors.

---

## 📂 Project Structure

```text
practice2_library/
│
├── manage.py                   # Django command-line utility
├── db.sqlite3                  # SQLite database storing book records
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules for Python/Django
│
├── config/                     # Django Project Configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # Settings (installed apps, database config)
│   ├── urls.py                 # Main URL routing (routes to books.urls & admin)
│   └── wsgi.py
│
└── books/                      # Django Application
    ├── __init__.py
    ├── admin.py                # Admin configuration for Book model
    ├── apps.py                 # App configuration
    ├── forms.py                # BookForm definition (ModelForm)
    ├── models.py               # Book database model
    ├── tests.py                # Automated test cases
    ├── urls.py                 # Application URL patterns
    ├── views.py                # book_list and add_book view functions
    ├── migrations/             # Database migration history
    │   ├── 0001_initial.py     # Initial migration creating Book table
    │   └── __init__.py
    └── templates/              # HTML Templates
        └── books/
            ├── book_list.html  # Book listing page template
            └── add_book.html   # Add new book form template
```

---

## 🚀 Installation & Setup Steps (Windows)

### 1. Open Project Folder in Terminal / VS Code
Open VS Code, navigate to or open `practice2_library`:
```powershell
cd practice2_library
```

### 2. Create and Activate Virtual Environment
```powershell
python -m venv venv
venv\Scripts\activate
```
*(If PowerShell restricts script execution, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then activate again).*

### 3. Install Django
```powershell
pip install django
```

### 4. Apply Database Migrations
```powershell
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin Superuser (if not already created)
```powershell
python manage.py createsuperuser
```
*(Default demo superuser credentials: username: `admin`, password: `admin123`)*

---

## 💻 Running the Application

Start the local development server:
```powershell
python manage.py runserver
```

Once running, access the following URLs in your web browser:

| Page | URL | Description |
|---|---|---|
| **Book Library** | [http://127.0.0.1:8000/](http://127.0.0.1:8000/) | Main listing page showing all books and total count |
| **Add Book Form** | [http://127.0.0.1:8000/add/](http://127.0.0.1:8000/add/) | Form to add a new book to the database |
| **Django Admin** | [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) | Admin panel to manage books and users |

---

## 🧪 Running Automated Tests

To run the automated test suite:
```powershell
python manage.py test
```

Expected output:
```text
Ran 5 tests in 0.235s
OK
```

---

## 📚 Sample Data Included

| No. | Title | Author | Year | Available |
|:---:|:---|:---|:---:|:---:|
| 1 | Wings of Fire | A. P. J. Abdul Kalam | 1999 | Yes |
| 2 | The Alchemist | Paulo Coelho | 1988 | Yes |
| 3 | Python Crash Course | Eric Matthes | 2015 | Yes |
| 4 | Malgudi Days | R. K. Narayan | 1943 | No |
| 5 | Ikigai | Hector Garcia and Francesc Miralles | 2016 | Yes |
