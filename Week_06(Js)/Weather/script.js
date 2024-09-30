const form = document.getElementById('form')
const city = document.getElementById('city_name')
const search = document.getElementById('search')


const url = 'https://open-weather13.p.rapidapi.com/city/landon/EN';
const options = {
	method: 'GET',
	headers: {
		'x-rapidapi-key': 'd02c827db6mshaf33db73f46d633p11289ajsnbf8e802432f1',
		'x-rapidapi-host': 'open-weather13.p.rapidapi.com'
	}
};
async function getWeather(city) {
    const loc = document.getElementById('loc')
    loc.innerHTML = city
    try {
        const response = await fetch(url, options);
        const result = await response.text();
        console.log(result);
        const temp = document.getElementById('temp')
        temp.innerHTML = result.temp;
        const feels_like = document.getElementById('feels_like')
        feels_like.innerHTML = result.feels_like
        const humdity = document.getElementById('humdity')
        humdity.innerHTML = result.humdity;
        const pressure = document.getElementById('pressure')
        pressure.innerHTML = result.pressure
        
    } catch (error) {
        console.error(error);
    }
}

search.addEventListener('click', (e) => {
    e.preventDefault();
    const city = city_name.value
    getWeather(city)
})
