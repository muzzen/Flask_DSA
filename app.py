from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/name', methods=['GET','POST'])
def hey():
    if request.method == 'POST':
        firstname = request.form['firstname']
        print(firstname)
        return render_template('print.html',name=firstname)

    else:

        return render_template('print.html')

if __name__ == '__main__':
    app.run()