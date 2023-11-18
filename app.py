from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/name', methods=['POST'])
def hey():
    return ('Hi')

if __name__ == '__main__':
    app.run()