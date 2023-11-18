from flask import Flask, render_template,request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/name', methods=['GET','POST'])
def hey():
    if request.method == 'POST':
        firstname = request.form['firstname']
        height = float(request.form['height'])
        print(firstname)
        
        model = pickle.load(open('model.pkl','rb'))
        weight = model.predict([[height]])

        result = round(weight[0],2)
        print(result)

        return render_template('print.html',name=firstname,height=height,weight=result)

    else:

        return render_template('print.html')

if __name__ == '__main__':
    app.run()