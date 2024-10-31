from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)


@app.route('/')
def home():
   return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('nm')
    if user:
        return redirect(url_for('success', name=user))
    else:
        return 'You must provide a name', 400

if __name__ == '__main__':
    app.run(debug=True)
