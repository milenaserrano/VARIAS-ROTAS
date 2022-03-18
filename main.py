from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def index():
    return render_template('index.html',
    )

@app.route('/unifran') 
def unifran():
  return '<h2>Universidade de Franca</h2>'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)