from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('emoticonos.html')

@app.route('/wakeup')
def page1():
    return render_template('wake_up.html')

@app.route('/message_wakeup')
def page2():
    return render_template('message_wakeup.html')

@app.route('/page2')
def page3():
    return render_template('nervioso.html')

@app.route('/page3')
def page5():
    return render_template('triste.html')

@app.route('/page4')
def page7():
    return render_template('enfadado.html')

if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=False)
    app.run(host='0.0.0.0', debug=True)
