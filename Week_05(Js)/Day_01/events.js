//click event
function greet(){
    alert("Hello Python")
}
// keyup events
function keyup(){
    var input = document.getElementById('firstname').value
    document.getElementById('sp').innerHTML = input
}

// mouseover

function mouseov(){

    document.getElementById('mouse').style.color = 'Green'
}
// MOUSE OVER ME

function mouseov(){

   document.getElementById('m').style.color = 'Red'
}
// Method 2 
// Onchange Event
// document.getElementById('name').onchange = function(){
//     myfun()
// }
function myfun(){
    var a = document.getElementById('name')
    
    a.value = a.value.toUpperCase()
}

// mehod 3 to create a event

//  addEventListener('click' , function(){
//     alert('Hello Python')
//  })

 addEventListener('click2' , function(){
    alert('Hellow')
 })

// method 4
let click_fun = document.getElementById('cc')
click_fun.addEventListener('cc', display)
function display(){
    alert('Helow display')
}

function bigimg(a){
    a.style.height = "64px"
    a.style.width = '64px'
}
function normal(a){
     a.style.height = "32px"
    a.style.width = '32px'
}

function onsub(){
    alert ('Name already existed')
}

function double(){
    document.getElementById('dbl_click').innerHTML += "Hellow Double Click Event"
}

// Multiple Event use on same element

var y = document.getElementById('btn')
y.addEventListener('click',myfun1);
y.addEventListener('click',myfun2)

function myfun1(){
    alert('Hellow Function one')
}
function myfun2(){
    alert("Second function ")
}

// On Focus Event

let nn = document.getElementById('uname')
nn.addEventListener('focus',()=> {
  console.log("User is entering name")
})

// on blur
let pw = document.getElementById('password')
pw.addEventListener('blur' , ()=> {
    console.log('User is gone')
    pw.style.border = '3px solid red'
})
