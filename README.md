# 📝 Task Manager

A simple Task Manager application built using "Python", "FastAPI", "SQLAlchemy", and "SQLite". This project demonstrates how to perform basic task management operations while maintaining a clean and modular project structure.

## 🚀 Features

* Add a new task
* View all tasks
* Update an existing task
* Delete a task
* Store task data using SQLite
* Modular project structure

## 🛠️ Technologies Used

* Python
* FastAPI
* SQLAlchemy
* SQLite

## 📂 Project Structure

```text
TaskManager/
│── main.py          # Application logic and endpoints
│── models.py        # SQLAlchemy Task model
│── database.py      # Database connection and session
│── tasks.db         # SQLite database
│── requirements.txt
│── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aaradhana964/TaskManager.git
```

### 2. Navigate to the project directory

```bash
cd TaskManager
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the virtual environment

**Windows**

```bash
env\Scripts\activate
```

**macOS/Linux**

```bash
source env/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
uvicorn main:app --reload
```

The application will start at:

```
http://127.0.0.1:8000
```

## 📖 API Documentation

Interactive API documentation is available at:

```
http://127.0.0.1:8000/docs
```

## 📌 Available Operations

* **GET** – Retrieve all tasks
* **POST** – Add a new task
* **PUT** – Update an existing task
* **DELETE** – Remove a task

## 📚 Learning Outcomes

Through this project, I learned:

* Building applications using FastAPI
* Working with SQLAlchemy ORM
* Connecting to an SQLite database
* Implementing CRUD operations
* Managing database sessions
* Organizing code into separate modules

## 📄 License

This project is created for learning and educational purposes.
