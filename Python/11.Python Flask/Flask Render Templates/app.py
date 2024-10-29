from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/var')
def var():
    user = 'Jinja Pratice Variable'
    return render_template('var.html', name=user)

@app.route('/if')
def ifelse():
    user = 'Conditions Jinja Pratice'
    return render_template('if.html', name=user)

@app.route('/for')
def forloop():
    list_course = ['Python','JS','HTML','CSS']
    return render_template('for.html', courses=list_course)


if __name__ == "__main__":
    app.run(debug=True)