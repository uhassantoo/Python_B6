
// make array of questions
let questions = [
    {
        'title' : "What is the power house of the cell",
        'options': ['Mitochondria','unique',' radicals',' diverse'],
        'answer' : 'Mitochondria'
    },

    {
        'title' : "Which is the strongest chamber of heart ",
        'options': ['left ventricle','right atrium',' Wrong',' diverse'],
        'answer' : 'left ventricle'
    },

    {
        'title' : "What is CPU  ",
        'options': ['Central Processing Unit','Mouse',' Hard Drive',' Keyboard'],
        'answer' : 'Central Processing Unit'
    },
    {
        'title' : "What is the Top Speed of  koenigsegg  ",
        'options': [256,100,250,320],
        'answer' : 256
    },
    {
        'title' : "What is the forth letters of greek   ",
        'options': ['Delta ','Alpha ','Barvo ','Charlie'],
        'answer' : 'Delta '
    },

    {
        'title' : "how many dots appear on a pair of dice  ",
        'options': ['42 dots ','44 dots ','46 dots ','48 dots'],
        'answer' : 42 
    },
    {
        'title' : "who is known as the poet of the east  ",
        'options': ['Sir Muhammad Iqbal ','Sir Mursaleen  ','Muhammad Ali Jinnah','Johar '],
        'answer' : 'Sir Muhammad Iqbal '
    },
    {
        'title' : "how many hours  in a week  ",
        'options':  [40,168,250,320],
        'answer' : 168
    },
    {
        'title' : "Who is founder of Muslim legue Party  ",
        'options':  ['Nawaz Sherif ','Imran Khan  ','Shahbaz Sherif','Capt Safadar'],
        'answer' : 'Nawaz Sherif'
    },
    {
        'title' : "What is total songs of Sindhu Moose Wala ",
        'options':  [107,18,20,320],
        'answer' : 107
    },

]

// initialise variables
let questions_index = 0
let result = 0

// function to start the game on start button click
function start() {
    questions_index = 0
    result = 0
    let start_btn = document.getElementById('start')
    start_btn.addEventListener('click',function() {
        add_question()
    })
}

// call the start function
start()


// function for displaying new question on the screen every time
function add_question() {
    let current_question = questions[questions_index]
    console.log(current_question)

    let container = document.getElementById('container')
    container.innerHTML = '<h1>' + current_question.title +'</h1>'

    for(option of current_question.options ) {
        let option_btn_new = document.createElement('button')
        option_btn_new.innerText = option
        container.append(option_btn_new)
    }
    
    check_answer()
}

// function for evaluating the user option seletion and then displaying the next question
function check_answer() {
    let current_question = questions[questions_index]
    let option_btns = document.querySelectorAll('button')

    for(option_btn of option_btns){
        option_btn.addEventListener('click',function() {

            // get the value of button on which user clicked
            let user_selection = this.innerText

            // check if user selection is matched with the correct answer
            if(user_selection == current_question.answer){
                result++
            }

            //place check weither diplay new question of end the game if question finished.
            if(questions_index < questions.length  - 1)
            {
                questions_index++
                add_question()
            }
            else{
                end_game()
                // console.log('game over ')
            }

        });
    }
}

// function of creating end game elements
function end_game(){
    let container = document.getElementById('container')
    container.innerHTML = '<h1> Game Over ! </h1> <h1> Score: ' + result + '/' + questions.length + '</h1>'

    let restart_btn = document.createElement('button')
    restart_btn.id = 'start'
    restart_btn.innerText = 'Restart'

    container.append(restart_btn)
    start()
}