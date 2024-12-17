# FastAPI Project Example

This project demonstrates the fundamental features of the FastAPI framework, including how to work with databases. It covers essential FastAPI functionality such as handling requests, responses, routing, and data validation, and it integrates database interactions using SQLAlchemy.

## Features

- **FastAPI Core Features**:
  - Fast, modern Python web framework based on standard Python type hints.
  - Automatically generated OpenAPI and documentation (Swagger UI).
  - Asynchronous support for request handling.

- **Database Integration**:
  - SQLAlchemy ORM integration for database modeling and querying.
  - Async support for database interactions.
  - Examples of database CRUD (Create, Read, Update, Delete) operations.

- **Pydantic**:
  - Data validation and serialization using Pydantic models.
  - Request and response models.
  
- **Dependency Injection**:
  - Use of FastAPI’s dependency injection system to manage database connections and other services.

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- asyncpg (if using PostgreSQL)
- Uvicorn (ASGI server)

Install the dependencies via `pip`:

```bash
pip install fastapi sqlalchemy asyncpg uvicorn
```
# Project Structure
```
.
├── app
│   ├── __init__.py
│   ├── main.py          # Main application entry point
│   ├── models.py        # SQLAlchemy models (e.g., User, Item)
│   ├── crud.py          # CRUD operations for interacting with the database
│   ├── schemas.py       # Pydantic schemas for request/response validation
│   ├── database.py      # Database setup and session management
│   └── routers
│       ├── users.py     # Router for handling user-related endpoints
│       └── items.py     # Router for handling item-related endpoints
└── README.md
```
# Key Files:
- main.py: The main application file that initializes FastAPI and includes the router definitions, with background task handling.
- models.py: Defines the database models (e.g., User, Item) using SQLAlchemy ORM.
- database.py: Manages database connection setup and lifecycle using SQLAlchemy’s AsyncSession.
- bot.py: Presumably handles bot functionalities, part of the MVP.
- test_main.http: Contains test requests for the API, can be run using tools like HTTPie or Postman.

# Running the Application

To run the FastAPI application using Uvicorn, execute the following command:
```

uvicorn main:app --reload
```
The --reload flag enables auto-reloading on code changes.
The application will be available at http://127.0.0.1:8000.
