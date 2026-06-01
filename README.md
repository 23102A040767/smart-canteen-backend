# Smart Canteen Backend

A FastAPI + PostgreSQL backend for a Smart Canteen Management System.

## Features

- User Registration
- User Login
- PostgreSQL Database Integration
- Meal Management APIs
- Order Management APIs

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- Git & GitHub

## Project Structure

```
smart-canteen-backend/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── test_db.py
│
└── routes/
    ├── users.py
    ├── meals.py
    └── bookings.py
```

## Setup

### Clone Repository

```bash
git clone https://github.com/23102A040767/smart-canteen-backend.git
cd smart-canteen-backend
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Server

```bash
uvicorn main:app --reload
```

### API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

## Database

Database: PostgreSQL

Current Tables:

- users

Future Tables:

- meals
- orders

## Author

Manaswi Boligarla
