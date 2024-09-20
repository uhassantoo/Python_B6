// Document get element by id
//console.log(document.getElementById('heading'))

// get any element using id 
let heading = document.getElementById('heading')
console.log(heading)

// get any element by using class
let class_head = document.getElementsByClassName('heading')
console.log(class_head)

// get any element by using tag name 
let para = document.getElementsByTagName('p')
console.log(para)

// get any elemnt by using id or class or tag name 

let query_id = document.querySelector('#heading')
let query_class = document.querySelector('.heading')
let query_tag = document.querySelector('p')

console.log(query_tag)
console.log(query_id)


// query selector all

let q_all_id = document.querySelectorAll('#heading')
console.log(q_all_id)

let q_all_class = document.querySelectorAll('.heading')
console.log(q_all_class)

let q_tag = document.querySelectorAll('p')
console.log(q_tag)




// get value/innerText content of any tag
let heading1 = document.getElementById('heading').innerText

let heading2 = document.getElementById('heading')
let inner_heading = heading2.innerText

console.log(heading1)
console.log(inner_heading)


// BY Tag name

let div_elemt = document.getElementsByTagName('div')

let inner_text = div_elemt[0].innerText

console.log(div_elemt)
console.log(inner_text)
