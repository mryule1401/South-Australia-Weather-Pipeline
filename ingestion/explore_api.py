import requests
from datetime import datetime
from zoneinfo import ZoneInfo

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -34.93,
    "longitude": 138.60,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "Australia/Adelaide",
    "past_days": 1,
    "forecast_days": 1,
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()
print("Status code:", response.status_code)
print("URL thực tế:", response.url)

data = response.json()
print(data["daily"])

daily = data["daily"]
rows = []
for d, tmax, tmin, rain in zip(daily["time"],
                                daily["temperature_2m_max"],
                                daily["temperature_2m_min"],
                                daily["precipitation_sum"]):
    rows.append({"location": "Adelaide", "date": d,
                 "temp_max": tmax, "temp_min": tmin, "rainfall": rain})

for r in rows:
    print(r)
    
today_adelaide = datetime.now(ZoneInfo("Australia/Adelaide")).date().isoformat()
rows = [r for r in rows if r["date"] < today_adelaide]