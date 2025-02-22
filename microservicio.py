from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hola():
    return '¡Hola desde mi microservicio!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
