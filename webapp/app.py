from flask import Flask, render_template, url_for, request, jsonify, flash, send_from_directory, redirect, session
from tf_model.model import inference

app = Flask(__name__)

@app.route('/')
def index():
    if 'result' in session:
        message = session['result']
        session.pop('result')
        return render_template('index.html', message = message)
    else: 
        return render_template('index.html', message = 'Nah')

@app.route('/predict', methods=['POST'])
def predict():
    form = request.form.get('inputText')
    res = inference(form)
    return jsonify({'prediction': str(res)})

app.secret_key = 'your_secret_key'

if __name__ == "__main__":
    print(inference("I love this product so much!"))
    app.run(debug=True)