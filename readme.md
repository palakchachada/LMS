# 📚 Library Management System

A **Library Management System** built using **Django** and **MySQL** to manage books, users, and transactions efficiently.

---

## 🚀 Features
- 📖 Manage books (add, update, delete)
- 👤 User authentication (login, logout, register)


---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/palakchachada/LMS.git
cd library_management

2️⃣ Set Up a Virtual Environment

python -m venv env
source env/bin/activate  # For Mac/Linux
env\Scripts\activate  # For Windows


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Configure .env File
Create a .env file and add:
env

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password


5️⃣ Run Migrations
python manage.py migrate


6️⃣ Create a Superuser
python manage.py createsuperuser

7️⃣ Run the Server
python manage.py runserver



👨‍💻 Tech Stack
Frontend: HTML, CSS, Bootstrap

Backend: Django

Database: MySQL