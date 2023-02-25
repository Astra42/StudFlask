from flask import Flask
#перове WSGI приложение

app = Flask(__name__)


@app.route('/home')
@app.route('/index')
@app.route('/')
def index():
    return 'index'

@app.route('/about')
def about():
    return '<h1> опс а тут будет о сайте</h1>'

@app.route('/g')
def g():
    return '<h1> g</h1>'

if __name__ == "__main__":
    app.run(debug=True)#запуск локального сервера
print('test')




