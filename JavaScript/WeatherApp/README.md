# 🌦️ Weather App

A small client-side web application that retrieves and displays current weather information for a selected region using the WeatherAPI service. The application allows users to search for a location and view basic weather data such as temperature, weather condition, and a corresponding icon.

The interface dynamically adapts its visual theme based on the weather condition and time of day.

---

## 📱 Preview
![preview](gif/preview.gif)

---

## 📄 Brief Description

This project is a lightweight weather lookup tool built with **HTML, CSS, and JavaScript**.  
Users can input a region name, send a request to the weather API, and view the current weather conditions in a simple UI.

The application retrieves weather data through an API request and updates the interface dynamically. It also adjusts visual themes depending on weather conditions (clear, cloudy, rain, etc.) and switches between day and night backgrounds based on API data.

> ⚠️ **Note:** This app was mainly built and tested on mobile, so it might look a bit off on desktop.

---

## ✨ Features

- 🔎 **Region Search**  
  Search weather information by entering a region name.

- 🌡️ **Current Weather Display**  
  Shows the current temperature, weather description, and icon.

- 🎨 **Dynamic Weather Themes**  
  Background color adapts to weather conditions (clear, cloudy, rain, storm, snow, fog).

- 🌙 **Day and Night Mode**  
  Automatically changes the background based on the day/night indicator from the API.

- ⚠️ **Error Handling**  
  Displays an error message if the API request fails or the location is invalid.

- 🎞️ **Animated Background**  
  Smooth gradient animation for the page background.

---

## 📦 Dependencies

This project uses minimal dependencies and runs entirely in the browser.

**External Service**
- Weather data provided by:
  [![WeatherAPI](https://cdn.weatherapi.com/v4/images/weatherapi_logo.png)](https://www.weatherapi.com/)
  https://www.weatherapi.com/

**Technologies**
- HTML5
- CSS3
- JavaScript (ES6+)
- Fetch API (built-in browser API)

---

## 🗂 Project Structure

```

project-folder
│
├── index.html      # Main application interface
├── style.css       # Styling and visual themes
├── index.js        # Application logic and API interaction
└── config.js       # API configuration

````

---

## 🚀 How to Use

1. Clone or download this repository.

```bash
git clone https://github.com/yourusername/weather-app.git
````

2. Open the project folder.

3. Make sure the API key is defined inside:

```
config.js
```

4. Open the application in a browser:

```
index.html
```

5. Enter a **region name** in the search field and press **Search**.

6. The application will display:

* Region name
* Current temperature
* Weather condition
* Weather icon

---

## 🖼 Example Output

After searching for a location, the application will display:

* City / region name
* Temperature in °C
* Weather icon
* Weather condition text
* Theme color that reflects the weather
