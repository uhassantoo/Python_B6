let form = document.getElementById('form_user')

form.addEventListener('submit', function(e){

  // input validation

  // Frist name Validation

  let fname = document.getElementById('name').value
  let fnam_error = document.getElementById('name_error')


  if (fname == ''){
    fnam_error.innerText = 'First Name is required'
    e.preventDefault()
  }

  else{
    fnam_error.innerText = ''
  }

  // Last Name Validation

  let lname = document.getElementById('lname').value
  let lname_error = document.getElementById('lname_error')


  if (lname == ''){
    lname_error.innerText = 'Last Name is required'
    e.preventDefault()
  }

  else{
    lname_error.innerText = ''
  }

  // Age

  let age = document.getElementById('age').value
  let age_error = document.getElementById('age_error')


  if (age < 13 || age>65){
    console.log('Age Error')
    age_error.innerText = ' Age should be between 13 - 65'
    e.preventDefault()
  }
  else{
    age_error.innerText = ''
  }
  
  // Email Validation 
  let email = document.getElementById('email').value
  let email_error = document.getElementById('email_error')

  if (!email.includes('@') || !email.includes('.')){
    email_error.innerText = " Kindly Enter Proper Email"
    e.preventDefault()
  }
  else{
    email_error.innerText = ""
  }

  // Pasword Validation

  let pwds = document.getElementById('pwd').value
  let pwd_error = document.getElementById('pwd_error')

  if(pwds.length < 8){
    pwd_error.innerText = ' Password should be of 8 Characters'
    e.preventDefault()
  }
  else {
    pwd_error.innerText = ''
  }
  

  let cpw = document.getElementById('pwd1').value
  let pwdd_error = document.getElementById('pwd1_error')


 if(cpw == '' || password != cpw){
  pwdd_error.innerText = ' Password Does not Match'
  e.preventDefault()
 }
 else {
       pwdd_error.innerText = ''
 }

  



  console.log('Form Is Submitted')
})