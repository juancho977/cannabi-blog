from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')
 

if __name__== '__main__':
    app.run(debug=True)