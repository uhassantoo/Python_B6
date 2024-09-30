let form  = document.getElementById('form')
const kelvin = 273.15

const api_key = 'f840fc703d990af2cfcad33ddaa5f837'
form.addEventListener('submit', async function (e) {
    e.preventDefault()


    let  city_name = document.getElementById('city_name').value
    let url = `https://api.openweathermap.org/data/2.0/weather?q=${city_name}&appid=${api_key}&units=metric`

    if (city_name == ''){
        alert("Enter the valid city name")
    }else {
        let response = await fetch(url)
        let data = await response.json()


        // data

        get_data(data)
        get_loc(data)
        get_temp(data)

        console.log(response)

        // url
        console.log(url)
    }
})


function get_data(data){
    const  months_start = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    let date_dt = data.dt * 1000

    let date = new Date(date_dt)

    let month_index  = date.getMonth()
    let month = months_start[month_index]

    let current_date = date.getDate()
    let min = date.getMinutes()
    let hours = date.getHours()


    let num = ''

    if(hours>12){
        num = 'PM'
    }else {
        num = 'AM'
    }

    let final_date =  `${month} ${current_date}, ${min}, ${hours} `

    let date_element = document.getElementById('date')
    date_element.innerText = final_date

}

function get_loc(data){
    let city = data.name
    let country = data.sys.country


    let  final_loc = `${city},${country}`

    let loc_element = document.getElementById('loc')
    loc_element.innerText = final_loc
}