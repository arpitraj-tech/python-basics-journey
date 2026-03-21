# 🌦️ Weather Forecast 

A terminal-based **Weather Forecast application** built with Python that fetches real-time weather data using the [Weatherstack API](https://weatherstack.com/) and presents it through a clean, interactive menu.

---

## 📸 Preview

```
                              Welcome to weather forecast                              

what do you want to know :
1. your location
2. current temperature
3. weather condition
4. Timing of sun and moon rise and set
5. Air quality and cloud cover
6. Exit

from above options please select appropriate response only:
```

---

## 🚀 Features

- 📍 **Location Info** — City, State, Country, Latitude & Longitude
- 🌡️ **Current Temperature** — Live temperature in °C
- ⛈️ **Weather Condition** — Description like "Thunderstorm", "Sunny", etc.
- 🌅 **Astro Timings** — Sunrise, Sunset, Moonrise & Moonset times
- 🌬️ **Air Quality & Cloud Cover** — CO, NO₂, O₃, SO₂, PM2.5, PM10 + cloud coverage %
- 💾 **JSON Caching** — API response saved locally to avoid repeated calls
- 🖥️ **Auto screen clear** — Clean terminal UI after every action

---

## 📁 Project Structure

```
weather-forecast/
│
├── function.py              # Fetches data from Weatherstack API & saves to JSON
├── main.py                  # Menu-driven interface to display weather info
├── wheather_response.json   # Cached API response (auto-generated)
└── README.md                # You're reading it!
```

---

## ⚙️ Requirements

**Python 3.x** and one external library:

```bash
pip install requests
```

> All other modules (`json`, `os`, `time`) are Python built-ins — no extra install needed.

---

## 🔑 API Setup (Required Before Running)

This app uses the **Weatherstack API** (free plan available).

**Step 1** — Sign up at [https://weatherstack.com/](https://weatherstack.com/)

**Step 2** — Go to your **Dashboard** and copy your `access_key`

**Step 3** — Open `function.py` and replace the placeholder:

```python
params = {
    "access_key": "YOUR_API_KEY_HERE",   # ← paste your key here
    "type": "city",
    "query": "YourCity, YourCountry"     # ← set your city
}
```

---

## 🛠️ How to Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/weather-forecast.git
cd weather-forecast
```

**2. Install dependencies**
```bash
pip install requests
```

**3. Fetch fresh weather data** *(run this first — generates the JSON file)*
```bash
python function.py
```


> ⚠️ Always run `function.py` first (or whenever you want updated data), then run `main.py` to explore it.

---

## 📖 Menu Options Explained

| Option | Feature | What it shows |
|--------|---------|---------------|
| `1` | 📍 Your Location | City, State, Country, Latitude, Longitude |
| `2` | 🌡️ Temperature | Current temperature in °C |
| `3` | ⛈️ Weather Condition | Description (e.g. Thunderstorm, Clear, Cloudy) |
| `4` | 🌅 Sun & Moon Timings | Sunrise, Sunset, Moonrise, Moonset |
| `5` | 🌬️ Air Quality & Clouds | CO, NO₂, O₃, SO₂, PM2.5, PM10, Cloud cover % |
| `6` | 🚪 Exit | Gracefully closes the app |

---


## 🧠 Modules Used

| Module | Type | Purpose |
|--------|------|---------|
| `requests` | External | Make HTTP GET request to Weatherstack API |
| `json` | Built-in | Parse API response & read/write JSON file |
| `os` | Built-in | Detect OS to clear terminal (`cls` / `clear`) |
| `time` | Built-in | Pause screen after displaying each result |

---


