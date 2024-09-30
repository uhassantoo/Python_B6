const API_KEY = 'd02c827db6mshaf33db73f46d633p11289ajsnbf8e802432f1';
const HOST = 'open-weather13.p.rapidapi.com';

const form = document.querySelector('form');


form.addEventListener('submit', handleSubmit); // callback function

function handleSubmit(e) {
    e.preventDefault();

    const loc = e.target.location.value;

    console.log(loc);

    fetchWeather(loc);

    console.log('hello');
}

const fetchWeather = async (city) => {
    const url = `https://open-weather13.p.rapidapi.com/city/${city}/EN`;
    const options = {
        method: 'GET',
        headers: {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': HOST,
        },
    };

    const response = await fetch(url, options);

    const data = await response.json()
    console.log(data);

    const temp = data["main"]["temp"];

    console.log(temp);

    const feels_like = data["main"]["feels_like"];

    console.log(feels_like);

    const pressure = data["main"]["pressure"];

    console.log(pressure);

    const humidity = data["main"]["humidity"];

    console.log(humidity);
}