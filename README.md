# HRMS Lite (Django + React)

A lightweight Human Resource Management System for a single admin user.

## Project Overview
This application provides two core modules:
- Employee Management: add, list, and delete employees.
- Attendance Management: mark daily attendance and view records per employee.

It is built as a full-stack monorepo:
- `backend/` - Django + Django REST Framework APIs with SQLite persistence.
- `frontend/` - React (Vite) admin UI.

## Tech Stack
- Frontend: React 18, Vite
- Backend: Django, Django REST Framework, django-cors-headers
- Database: SQLite

## Features Implemented
- Add employee with server-side validation:
  - Required fields
  - Unique employee ID
  - Valid and unique email
- View employee directory
- Delete employee (cascades linked attendance)
- Mark attendance:
  - Employee, date, status (Present/Absent)
  - Prevent duplicate attendance for same employee/date
- View attendance records per selected employee
- Attendance date filtering (bonus)
- Present-day count for selected employee (bonus)
- Dashboard summary cards (bonus)
- UI states:
  - Loading
  - Empty states
  - Error states
- RESTful API responses with meaningful HTTP errors

## Folder Structure
```text
.
├── backend
│   ├── attendance
│   ├── hr
│   ├── hrms_lite
│   ├── manage.py
│   └── requirements.txt
├── frontend
│   ├── src
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## Run Locally

### 1) Backend Setup
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Backend runs at `http://127.0.0.1:8000`.

Run backend tests (optional):
```bash
python manage.py test
```

### 2) Frontend Setup
In a new terminal:
```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```
Frontend runs at `http://127.0.0.1:5173` and connects to `http://127.0.0.1:8000/api`.
For deployment, set `VITE_API_BASE_URL` to your live backend API base URL.

## Backend Deployment (Vercel)
Backend is pre-configured for Vercel in:
- `backend/vercel.json`
- `backend/api/index.py`

Deploy steps:
1. Import this repo into Vercel.
2. Set the **Root Directory** to `backend`.
3. Deploy.

Notes for SQLite on Vercel:
- Vercel filesystem is serverless/ephemeral. This setup uses `/tmp/db.sqlite3` on Vercel.
- Data is not durable across cold starts/redeploys.
- For production persistence, switch to a managed PostgreSQL database.
- For assignment convenience, backend currently allows all hosts/CORS.

## API Endpoints
- `GET /api/employees/` - list employees
- `POST /api/employees/` - add employee
- `DELETE /api/employees/{id}/` - delete employee
- `GET /api/employees/{id}/attendance/` - attendance by employee
- `GET /api/attendance/?employee_id={id}&date=YYYY-MM-DD` - filtered attendance
- `POST /api/attendance/` - mark attendance
- `GET /api/dashboard/` - summary stats

## Assumptions and Limitations
- Single admin user; authentication/authorization is out of scope.
- SQLite is used for local persistence.
- On Vercel with SQLite, data is ephemeral (`/tmp/db.sqlite3`).
- Backend is intentionally open for assignment use (`ALLOWED_HOSTS=['*']`, CORS allow all).
- Pagination is not enabled due limited assignment scope.
- Backend deployment is configured for Vercel; durable production DB is not included.
