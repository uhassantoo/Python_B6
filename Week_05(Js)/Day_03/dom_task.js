// Task 1

let bgcolor = document.getElementById('bg')

bgcolor.addEventListener('click', function(){
    bgcolor.style.backgroundColor = 'yellow'

})

// Task 2

let counter_btn = document.getElementById('cbtn')
counter_btn.addEventListener('click', function(){
    let counter_span = document.getElementById('counter')
    let counter_value = counter_span.innerText

    counter_value++
    counter_span.innerText = counter_value
})

// Task 3
let color_btn = document.getElementById('form')
color_btn.addEventListener('submit', function(e){
  e.preventDefault()
  let color = document.getElementById('color').value
  
  let body = document.querySelector('body')
  body.style.backgroundColor = color


})

// Task 4
let img_btn = document.getElementById('img_btn')
img_btn.addEventListener('click', function(){
    let img = document.getElementById('img')

    let height = img.style.height
    console.log(height)

    if (height == '500px'){
        img.style.height= '50px'
        img.style.width = '50px'
        img_btn.innerText = 'CLICK TO Enlarge'
    }
    else{
        img.style.height= '500px'
        img.style.width = '500px'
        img_btn.innerText = 'CLICK TO shrink'
    }
})

// Task 5

let items = document.getElementsByClassName('items')

for(let i=0; i<items.length; i++  ){
    items[i].addEventListener('click',function(){
        items[i].style.display = 'none'
    })
    // console.log(items[i])
}

// Task 6
let input_count = 2
let new_btn = document.getElementById('new_btn')
new_btn.addEventListener('click',function(){
    let new_input = document.createElement('input')
    let br_elemment = document.createElement('br')

    new_input.name = 'input-'+input_count
    new_input.placeholder = 'input-'+input_count
    input_count++

    let inputs = document.getElementById('inputs')
    inputs.appendChild(br_elemment)

    inputs.appendChild(new_input)
    
});


// Task 7

let lucky_draw = document.getElementById('lucky')

let std = [

    'Eman',
    'Mariam',
    'Zain',
    'Balaj',
    'Hashir',
    'Adeel',

    'Osama',
   
   
]

lucky_draw.addEventListener('click', function(){
    random_index = Math.floor(Math.random()*std.length)
    alert('Congrats' +std[random_index] + 'You are Winner Now you leave the class')
})