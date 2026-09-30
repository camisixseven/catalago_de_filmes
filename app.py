from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>hello world</h1>'

@app.route('/usuario')
def buscar_usuario():
    usuario = {
        "nome" "camila"
        "idade": 40,
        "telefone" "(19) 997367474"
    }
    return usuario





if __name__ == '__main__':
    app.run(debug=True)}