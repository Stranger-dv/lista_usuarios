from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/usuarios', methods=['GET'])
def usuarios():
    usuarios = [
    {"nombre": "Carlos", "edad": 32, "email": "carlos32@example.com"},
    {"nombre": "Lucía", "edad": 25, "email": "lucia25@example.com"},
    {"nombre": "Martín", "edad": 41, "email": "martin41@example.com"},
    {"nombre": "Ana", "edad": 29, "email": "ana29@example.com"},
    {"nombre": "Sofía", "edad": 36, "email": "sofia36@example.com"},
    {"nombre": "Diego", "edad": 22, "email": "diego22@example.com"},
    {"nombre": "Valeria", "edad": 30, "email": "valeria30@example.com"},
    {"nombre": "Javier", "edad": 27, "email": "javier27@example.com"},
    {"nombre": "Elena", "edad": 35, "email": "elena35@example.com"},
    {"nombre": "Miguel", "edad": 40, "email": "miguel40@example.com"}
    ]
    return render_template('lista.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)