# Todo List Application

A simple and responsive Todo List web application built with Flask and Bootstrap, allowing users to create, view, update, and delete tasks.

---

## 📝 Features

- Add new todo items with a title and description.
- View a list of all todo tasks in a table format.
- Edit existing tasks to update their details.
- Delete tasks that are no longer needed.
- Responsive design for seamless use on all devices.
- Real-time timestamps for when tasks were created.

---

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (or any preferred database)
- **Templating Engine**: Jinja2

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AbdulMa1505/todo-list.git
   cd todo-list
2. Set Up a Virtual Environment
  ```python -m venv venv
    source venv/bin/activate    # On Linux/MacOS
    venv\Scripts\activate       # On Windows
3. Install Dependencies
    ``pip install flask
4. Run the Application
    ``flask run

## 📂 Project Structure
todolist/
├── app.py              # Main Flask application
├── templates/          # HTML templates (index, update, etc.)
│   ├── index.html
│   ├── update.html
├── static/             # Static files (CSS, JavaScript)
│   ├── css/
│   ├── js/
├── database/           # Database file (SQLite)
│   ├── todo.db
└── README.md           # Project documentation


