"""chereshnya"""



from flask import Flask

app= Flask(__name__)


@app.route('/')
def hello():
    return( 'Yo maboy')


@app.route("/about_me")
def about_me():
    return "wassub bro"


@app.route("/guro")
def guro():
    return "qwerty"


@app.route("/bomb")
def guro():
    return "Меня зовут Кира Йошикаге и мне 33 года"

if __name__ == '__main__':
    app.run(debug=True)
