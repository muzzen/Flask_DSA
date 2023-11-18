from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/name', methods=['POST'])
def hey():
    user_value = request.values['firstname']
    return ("Hi {}".format(user_value))

if __name__ == '__main__':
    app.run()