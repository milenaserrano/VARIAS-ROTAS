from flask import Flask
app = Flask('app')

@app.route('/') 
def hello_world():
  return '<h1>Olá Mundo!</h1>'

@app.route('/unifran') 
def unifran():
  return '<h1>Universidade de Franca</h1>'

@app.route('/dashboard/<name>') 
def name(name):
  return f'Olá, {name}!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)