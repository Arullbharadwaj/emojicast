async function checkWeather() {
    const city = document.getElementById("cityInput").value.trim();
    const apiKey = "_"; // Replace with your OpenWeatherMap API key
    const baseUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    if (!city) {
        alert("Please enter a city name.");
        return;
    }

    try {
        const response = await fetch(baseUrl);
        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${response.statusText}`);
        }
        const data = await response.json();

        const weatherDescription = data.weather[0].description;
        const temperature = data.main.temp;

        document.getElementById("description").textContent =
            `Weather: ${weatherDescription.charAt(0).toUpperCase() + weatherDescription.slice(1)}`;
        document.getElementById("temperature").textContent =
            `Temperature: ${temperature}°C`;
        document.getElementById("emoji").textContent = getWeatherEmoji(weatherDescription);

        document.getElementById("result").classList.remove("hidden");

    } catch (error) {
        alert("Failed to fetch weather data. " + error.message);
    }
}

function getWeatherEmoji(description) {
    description = description.toLowerCase();
    if (description.includes("cloud")) return "☁️";
    if (description.includes("clear")) return "☀️";
    if (description.includes("rain")) return "🌧️";
    if (description.includes("snow")) return "❄️";
    if (description.includes("storm") || description.includes("thunder")) return "🌩️";
    return "🌥️";
}
