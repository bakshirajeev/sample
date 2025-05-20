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
