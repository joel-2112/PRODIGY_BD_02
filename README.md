# User API with Django REST Framework and PostgreSQL

This project provides a RESTful API for managing user data using Django REST Framework (DRF) and PostgreSQL.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Project](#running-the-project)
5. [API Endpoints](#api-endpoints)
6. [Environment Variables](#environment-variables)
7. [Database Migrations](#database-migrations)
8. [Testing](#testing)
9. [Contributing](#contributing)
10. [License](#license)

---

## Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.8+**
- **PostgreSQL**
- **pip** (Python package manager)
- **virtualenv** (for creating isolated Python environments)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. **Copy the example environment file and configure it:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file** to set your PostgreSQL credentials:
   ```plaintext
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

3. **Load environment variables:**
   ```bash
   source .env
   ```

---

## Running the Project

1. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

3. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

4. The API will be available at **http://127.0.0.1:8000/**.

---

## API Endpoints

### Users
- **GET `/api/users/`**: Retrieve a list of users.
- **POST `/api/users/`**: Create a new user.
- **GET `/api/users/{id}/`**: Retrieve a specific user by ID.
- **PUT `/api/users/{id}/`**: Update a specific user by ID.
- **DELETE `/api/users/{id}/`**: Delete a specific user by ID.

---

## Environment Variables

The project uses environment variables for configuration. Ensure you have the following variables set in your `.env` file:

```plaintext
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Database Migrations

To create and apply database migrations, run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

