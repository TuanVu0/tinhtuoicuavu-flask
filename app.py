from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    birth_year = int(request.form['birth_year'])
    age = 2025 - birth_year
    return render_template('result.html', age=age)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)