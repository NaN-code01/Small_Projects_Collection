// Weather App

const searchBtn = document.querySelector("#searchBtn");
const searchRegion = document.querySelector("#searchRegion");
const errorMsg = document.querySelector("#errorMsg");
const weatherContainer = document.querySelector("#weatherContainer");

// accessing child elements from #weatherContainer
const regionDisplay = weatherContainer.querySelector("#region");
const temperatureDisplay = weatherContainer.querySelector("#temperature");
const weatherIconDisplay = weatherContainer.querySelector("#weatherIcon");
const weatherDisplay = weatherContainer.querySelector("#weather");

// "click" action on the search button
searchBtn.addEventListener("click", async event => {
    event.preventDefault();
    const region = encodeURIComponent(searchRegion.value.trim());

    if (region) {
        searchBtn.disabled = true;
        const weatherData = await getWeatherData(region);
        if (weatherData) displayWeatherData(weatherData);
        searchBtn.disabled = false;
    }
});

// Get weatherAPI data function
// -> for callin APi and receive some responses as data
async function getWeatherData(region) {
    const API_URL = `https://api.weatherapi.com/v1/current.json?key=${API_KEY}&q=${region}`;
    try {
        const response = await fetch(API_URL); // API call
        const data = await response.json(); // turning the response to JSON
        if (!response.ok) throw new Error(data.error.message);

        clearError();
        console.log("Weather Data Successfully Retrieved");
        console.log(data);
        return data;
    } catch (error) {
        console.log("An Error Occurred When Retrieving Weather Data");
        errorDisplay(error);
    }
}

// Error display function
// -> for displaying some errors
function errorDisplay(error) {
    console.error(error);
    errorMsg.textContent = `error: ${error.message}`;
    errorMsg.style.display = "block";
}

// Clear error display function
// -> for clearing error display
function clearError() {
    errorMsg.textContent = null;
    errorMsg.style.display = "none";
}

// Display weather data function
// -> for displaying weather data to the Weather Container Box
function displayWeatherData(weatherData) {
    weatherContainer.style.display = "block";

    regionDisplay.textContent = `${weatherData.location.name}, ${weatherData.location.region}`;
    temperatureDisplay.textContent = `${weatherData.current.temp_c}°C`;
    weatherIconDisplay.src = `https:${weatherData.current.condition.icon}`;
    weatherDisplay.textContent = weatherData.current.condition.text;

    document.body.classList.toggle("night", !weatherData.current.is_day);
    applyWeatherTheme(weatherData.current.condition.code);
}

// Gettin weather theme function
// -> for determine which weather it is by the code given
// -> return a string that describe the general weather
function getWeatherTheme(code) {
    const weatherMap = {
        clear: [1000],
        cloudy: [1003, 1006, 1009],
        fog: [1030, 1135, 1147],
        storm: [1087, 1273, 1276, 1279, 1282],
    };

    for (const [theme, codes] of Object.entries(weatherMap)) {
        if (codes.includes(code)) return theme;
    }

    if (
        (code >= 1066 && code <= 1117) ||
        (code >= 1204 && code <= 1237) ||
        (code >= 1210 && code <= 1225) ||
        (code >= 1255 && code <= 1264)
    ) return "snow";

    if (
        (code >= 1063 && code <= 1072) ||
        (code >= 1150 && code <= 1201) ||
        (code >= 1240 && code <= 1246)
    ) return "rain";

    return "unknown";
}

// Applying weather theme function
// -> for changing the color of weatherContainer depending on the weather
function applyWeatherTheme(code) {
    const theme = getWeatherTheme(code);
    // hapus class bg lama
    weatherContainer.classList.forEach(bg => {
        if (bg.startsWith("bg-")) weatherContainer.classList.remove(bg);
    });
    weatherContainer.classList.add(`bg-${theme}`);
}
