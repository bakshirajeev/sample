# Sample PowerBI Catalog Application

This repository contains a simple end-to-end sample demonstrating how to build a Power BI catalog using a .NET backend and a React frontend.

- `backend/` contains an ASP.NET Core minimal API that calls the Power BI REST APIs.
- `frontend/` contains a React application that fetches and displays the catalog.

## Prerequisites

- .NET 6 SDK
- Node.js and npm

## Running the Sample

1. Update credentials in `backend/PowerBI.Catalog.API/PowerBiService.cs`.
2. Start the backend API:
   ```bash
   cd backend/PowerBI.Catalog.API
   dotnet run
   ```
3. In another terminal, start the React app:
   ```bash
   cd frontend
   npm install
   npm start
   ```
4. Navigate to `http://localhost:3000` to view the catalog.

---

## HRMS Webapp

This repository also includes a minimal HRMS (Human Resource Management System) implementation using a Django REST backend and a React frontend built with Material UI. The landing page displays a simple dashboard and React Router is used to navigate between Employees and Departments pages.

### Backend

The Django project is located in `hrms_backend/`. It exposes two REST endpoints under `/api/` for managing employees and departments. To run the backend:

```bash
cd hrms_backend
python3 manage.py migrate  # create the SQLite database
python3 manage.py runserver
```

### Frontend

The React app is located in `hrms_frontend/`. It uses Material UI components and React Router for navigation. To start the development server:

```bash
cd hrms_frontend
npm install
npm start
```

### Tests

Unit tests are provided for both the Django backend and the React frontend:

```bash
# Backend tests
cd hrms_backend
python3 manage.py test

# Frontend tests
cd hrms_frontend
npm test
```

These tests require the appropriate dependencies to be installed.
