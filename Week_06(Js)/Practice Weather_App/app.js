// Selecting HTML elements
const searchInput = document.querySelector('.search input');
const searchButton = document.querySelector('.search button');
const weatherIcon = document.querySelector('.weather-icon');
const temperatureElement = document.querySelector('.temp');
const cityElement = document.querySelector('.city');
const humidityElement = document.querySelector('.humidity');
const windElement = document.querySelector('.wind');

// Rapid API endpoint and API key
const apiUrlBase = 'https://open-weather13.p.rapidapi.com/city/';
const apiKey = 'f32ba4c286msh13e9d35538aaab4p15a267jsne36d90915591';

// Event listener for search button
searchButton.addEventListener('click', async () => {
    const city = searchInput.value.trim();
    if (city) {
      try {
        const apiUrl = `${apiUrlBase}${city}/EN`;
        //console.log  check api is working or not
        console.log(`API URL: ${apiUrl}`);
        const response = await fetch(apiUrl, {
          method: 'GET',
          headers: {
            'X-RapidAPI-Key': apiKey,
            'X-RapidAPI-Host': 'open-weather13.p.rapidapi.com',
          },
        });
        console.log(`Response status: ${response.status}`);
        if (response.ok) {
          const data = await response.json();

        //console.log  check api is working or not
          console.log(`Data: ${JSON.stringify(data)}`);
          displayWeatherData(data);
        } else {
          console.error(`Error: ${response.status} ${response.statusText}`);
        }
      } catch (error) {
        console.error(`Error: ${error.message}`);
      }
    }
  });

// Function to display weather data
function displayWeatherData(data) {
    console.log('Data:', data); // Log the entire data object
  
    const { main, weather, wind, name } = data;
  
    // Get the icon code for the current weather condition
    const iconCode = weather[0].icon;
  
    // Check if the icon code is present and has a valid value
    if (iconCode) {
      weatherIcon.src = `http://openweathermap.org/img/wn/${iconCode}@2x.png`;
    } else {
      weatherIcon.src = ''; // Set a default icon or handle the case where icon is undefined
    }
  
    temperatureElement.textContent = `${main.temp}°C`;
    cityElement.textContent = name;
    humidityElement.textContent = `${main.humidity}%`;
    windElement.textContent = `${wind.speed} km/h`;
  }