# BugTracker

A simple Django-based application for tracking bugs, issues, and tasks.

## Overview

BugTracker allows users to:
- Create new bug reports
- Edit existing bugs
- Track the status and severity of bugs
- Manage bugs through Django's built-in admin panel

This project was built to practice Django development, ORM modeling, and CRUD application design.

---

## Tech Stack

- Python 3.x
- Django 4.x
- SQLite (default development database)
- HTML/CSS (via Django Admin)

---

## Features

- Add, update, delete bug records
- Track bug title, description, status, severity, and creation date
- Admin interface for easy management
- Lightweight, fast local server for testing

---

## Getting Started

### Prerequisites

- Python 3.x installed
- `pip` package manager
- (Recommended) Virtual environment (`venv`)

### Installation

1. Clone the repository or download the project folder.
2. Navigate into the project directory:
    cd bugtracker
3. Install Django:
    pip install django
4. Run migrations to set up the database:
    python manage.py makemigrations
    python manage.py migrate
5. Create a superuser account to access the admin panel:
    python manage.py createsuperuser
6. Start the development server:
    python manage.py runserver
7. Open your browser and visit:
    http://127.0.0.1:8000/admin


## Future Improvements (Ideas)
- Add user authentication (reporter, assignee)
- Add file attachments for bugs (e.g., screenshots)
- Build public-facing pages (not just admin)
- Add API endpoints (REST framework)
- Status notifications (email updates)
