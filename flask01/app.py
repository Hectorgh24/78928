from flask import Flask
app = Flask(__name__)
@app.route('/')
def hola_mundo():
    return 'Hola Mundo'
if __name__ == '__main__': #para que lo ejecute como  principal
    app.run(host = '0.0.0.0', debug = True)