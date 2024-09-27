let form = document.getElementById('form')

// get todo from localstorage
let current_todos = localStorage.getItem('todo_list')

let todo_list = document.getElementById('todo_list')
todo_list.innerHTML = current_todos

// console.log(current_todos)

form.addEventListener('submit' , function(e){
    e.preventDefault()

  // get new todo value from input field

  let new_todo_item = document.getElementById('todo').value
  if(new_todo_item == ''){
    alert('Please Enter a valid todo task....')

  }else{
    // current new li element

    let new_li = document.createElement('li')
    new_li.innerHTML = '<span>'+new_todo_item +'</span> <button type="button" id="delete_btn">X</button>'
    
    // append li in ul tag 
    let todo_list = document.getElementById('todo_list')
    todo_list.append(new_li)

    //Save list in local storage

    add_todo()
    li_events()
  }
} )
function li_events(){
    //Get all  li for loop

    let lis = document.querySelectorAll('li')
    for(li in lis){
        
      let list = lis[li]

      list.children[0].addEventListener('click',function (){
        this.classList.add('marked')
        add_todo()
      })

      list.children[1].addEventListener('click',function(){
        list.remove()
        add_todo()
      })


    }
}
function add_todo(){
    let list = document.getElementById('todo_list').innerHTML
    localStorage.setItem('todo_list',list)
}

li_events()