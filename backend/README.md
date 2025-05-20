# PowerBI Catalog API

This ASP.NET Core application exposes an endpoint `/api/catalog` that fetches a catalog of all Power BI objects available in the tenant. The service calls the Power BI REST APIs using service principal authentication.

## Configuration

Update `PowerBiService.cs` with your tenant ID, client ID, and client secret.

## Build and Run

```bash
# Requires .NET 6 SDK
cd PowerBI.Catalog.API
dotnet run
```

This will start the API on the default Kestrel port.
