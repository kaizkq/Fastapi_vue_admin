# Video Project

A full-stack web application built with Vue.js 3 and FastAPI, featuring user authentication and book management.

## Project Structure

```
video_project/
├── frontend/         # Vue.js frontend
└── backend/         # FastAPI backend
```

## Prerequisites

- Node.js (v16 or higher)
- Python 3.11
- PostgreSQL (v12 or higher)
- npm or yarn

## Backend Setup

1. Create and activate a Python virtual environment:
```bash
cd backend
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Database Setup:
   - Install PostgreSQL if not already installed
   - Create a new database:
   ```sql
   CREATE DATABASE fastapi_vue_admin;
   ```
   - Create a user (if not exists):
   ```sql
   CREATE USER root WITH PASSWORD 'root123';
   ```
   - Grant privileges:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE fastapi_vue_admin TO root;
   ```
   - Import the initial data:
   ```bash
   psql -U root -d fastapi_vue_admin -f demo_postgres.sql
   ```

4. Start the backend server:
```bash
cd backend  # Make sure you're in the backend directory
uvicorn main:app --reload --port 5000
```
The backend server will run on `http://localhost:5000`

## Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
# or
yarn install
```

2. Start the development server:
```bash
npm run dev
# or
yarn dev
```
The frontend will be available at `http://localhost:5173`

## Default Users

The system comes with pre-configured users:

Admin User:
   - Username: admin
   - Password: 123456


## API Documentation

Once the backend is running, you can access the API documentation at:
- Swagger UI: `http://localhost:5000/docs`
- ReDoc: `http://localhost:5000/redoc`

## Features

- User Authentication (Login/Register)
- User Profile Management
- Book Management (CRUD operations)
- Responsive UI
- API Documentation
- PostgreSQL Database

## Development Notes

- The backend uses Tortoise ORM for database operations
- Frontend is built with Vue 3 + Vite
- API authentication uses JWT tokens
- CORS is enabled for development

## Common Issues

1. Database Connection:
   - Ensure PostgreSQL is running
   - Check credentials in `backend/main.py`
   - Verify database exists and user has proper permissions

2. Frontend API Connection:
   - Check if backend URL is correctly set in frontend configuration
   - Verify CORS settings if experiencing connection issues 