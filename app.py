from flask import Flask, render_template,request
import pickle

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/name', methods=['GET','POST'])
def hey():
    if request.method == 'POST':
        firstname = request.form['firstname']
        height = request.form['height']
        print(firstname)
        model = pickle.open('model.pkl','rb')
        weight = model.predict(height)
        print(weight)

        return render_template('print.html',name=firstname,height=height)

    else:

        return render_template('print.html')

if __name__ == '__main__':
    app.run()