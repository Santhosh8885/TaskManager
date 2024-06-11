# Task Management Application

This is a Django-based task management application that allows users to organize and track tasks effectively. It provides API endpoints for managing tasks, comments, task lists, user authentication, and role-based permissions.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/task-management.git
    cd task-management
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate  # For Windows
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

2. **Access the API endpoints:**

    - Task Management: `/api/tasks/`
    - Comment Management: `/api/comments/`
    - Task List Management: `/api/task-lists/`
    - User Authentication: `/api/accounts/`


3. **Create a superuser to access the Django admin interface:**

    ```bash
    python manage.py createsuperuser
    ```

4. **Log in to the admin interface at** `http://localhost:8000/admin/` **to manage models.**

## Configuration

- **Database:** Defalut sqllite3
- **Authentication:** Token-based authentication using Django REST Framework

## Folder Structure

- `taskmanager/`: Django project settings and configuration
- `tasks/`: App for task, comment, and task list models
- `accounts/`: App for user auth
