# Django Blog Application

## Overview

This project is a blog application built with **Django**, a powerful and flexible Python web framework. The application allows users to publish posts and interact with the blog using Django's built-in authentication system. It is entirely developed using **Class-Based Views (CBVs)**, providing a clean and reusable structure.

---

## Key Features

- **User Registration and Authentication:**
  - Users can register, log in, and log out using Django's built-in authentication system.
  - Secure password handling with hashing.

- **Post Management:**
  - **Create:** Authenticated users can create new blog posts.
  - **Read:** All users can view published blog posts.
  - **Update:** Authors can edit their own posts.
  - **Delete:** Authors can delete their own posts.

- **Class-Based Views (CBVs):**
  - The entire application is implemented using Django's Class-Based Views for better code organization and reusability.

---

## Technologies Used

- **Framework:** Django
- **Database:** SQLite (default), but can be configured for other databases like PostgreSQL or MySQL.
- **Frontend:** HTML, CSS, and Bootstrap for styling.
- **Authentication:** Built-in Django authentication system.

---

## How to Run the Project

### Prerequisites

1. **Python:** Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).
2. **pip:** Python's package manager.
3. **Git:** To clone the project from GitHub.

### Steps

#### 1. Clone the Project

```bash
git clone https://github.com/your-username/django-blog.git
cd django-blog
```

#### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Apply Database Migrations

```bash
python manage.py migrate
```

#### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

#### 6. Run the Local Server

```bash
python manage.py runserver
```

After running the server, you can access the application by navigating to:

```
http://127.0.0.1:8000/
```

---

## How to Use the Application

1. **Sign Up/Login:**
   - Register as a new user or log in with existing credentials.
   - Use the admin panel (`/admin`) to manage users and posts if you are a superuser.

2. **Create a Post:**
   - Navigate to the "Create Post" page and fill in the title and content of your post.

3. **View Posts:**
   - Browse the list of published posts on the homepage.

4. **Edit/Delete Posts:**
   - If you are the author of a post, you can edit or delete it from the post detail page.


