using System.Net.Http.Headers;
using System.Text.Json;

public class PowerBiService
{
    private readonly HttpClient _httpClient = new HttpClient();

    // TODO: Replace placeholders with actual tenant ID, client ID, client secret, and authority
    private const string Authority = "https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token";
    private const string ClientId = "YOUR_CLIENT_ID";
    private const string ClientSecret = "YOUR_CLIENT_SECRET";
    private const string Scope = "https://analysis.windows.net/powerbi/api/.default";

    private string? _accessToken;

    public async Task<string> GetAccessTokenAsync()
    {
        if (!string.IsNullOrEmpty(_accessToken))
        {
            return _accessToken;
        }

        var content = new FormUrlEncodedContent(new Dictionary<string, string>
        {
            {"client_id", ClientId},
            {"client_secret", ClientSecret},
            {"grant_type", "client_credentials"},
            {"scope", Scope}
        });

        var response = await _httpClient.PostAsync(Authority, content);
        response.EnsureSuccessStatusCode();
        var result = await response.Content.ReadAsStringAsync();
        using var doc = JsonDocument.Parse(result);
        _accessToken = doc.RootElement.GetProperty("access_token").GetString();
        return _accessToken!;
    }

    public async Task<object> GetCatalogAsync()
    {
        var token = await GetAccessTokenAsync();
        _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

        var catalog = new Dictionary<string, object>();

        catalog["groups"] = await GetAsync("https://api.powerbi.com/v1.0/myorg/groups");
        catalog["datasets"] = await GetAsync("https://api.powerbi.com/v1.0/myorg/datasets");
        catalog["reports"] = await GetAsync("https://api.powerbi.com/v1.0/myorg/reports");
        catalog["dashboards"] = await GetAsync("https://api.powerbi.com/v1.0/myorg/dashboards");
        catalog["dataflows"] = await GetAsync("https://api.powerbi.com/v1.0/myorg/dataflows");

        return catalog;
    }

    private async Task<object> GetAsync(string url)
    {
        var response = await _httpClient.GetAsync(url);
        response.EnsureSuccessStatusCode();
        var json = await response.Content.ReadAsStringAsync();
        return JsonSerializer.Deserialize<JsonElement>(json);
    }
}

