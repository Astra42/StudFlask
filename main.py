from flask import Flask, render_template
#перове WSGI приложение

app = Flask(__name__)

menu = ['котики большие', 'котики поменбше', 'микрочелс']
@app.route('/home')
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='главненькая', menu=menu)

@app.route('/about')
def about():
    return render_template('about.html', title='о котиках')

@app.route('/g')
def g():
    return '<h1> g</h1>'

if __name__ == "__main__":
    app.run(debug=True)#запуск локального сервера
print('test')




