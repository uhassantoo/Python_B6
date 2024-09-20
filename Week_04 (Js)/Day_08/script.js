// add style to any element

//method 1

let p_style = document.getElementById('p_style')

p_style.style.color = '#059862'
p_style.style.backgroundColor = 'lightpink'

// method 2

document.getElementById('p_style').style.color = 'red'
document.getElementById('p_style').style.backgroundColor = 'green'

// add new tag/element

// create a new element
let new_ele = document.createElement('p')
new_ele.innerText = 'Hi I am New One created element'

let new_ele1 = document.createElement('h3')
new_ele1.innerText = "Heading created by js "
// append in exixting element
document.getElementById('container').append(new_ele,new_ele1)


// append just one element at a time

let new_element2 = document.createElement('u')
new_element2.innerText = ' Underline tag created by js' 

document.getElementById('p_style').appendChild(new_element2)

// remove any tag from document

let item = document.getElementById('remove')
item.remove()

// get attribute
let anchor = document.getElementById('anchor')
let href_value = anchor.href

// method 2
let target_value = anchor.getAttribute('target')
console.log(href_value)
console.log(target_value) 
console.log(anchor)

// set attribute value

let heading = document.getElementById('heading')
heading.setAttribute('class','background')

heading.style.border = '1px solid black'

document.getElementById('div1').setAttribute('class','div-style')
document.getElementById('div1').style.border = '1px solid black '