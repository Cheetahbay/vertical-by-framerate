from flask import Flask, render_template
from calculator import Calculator

app = Flask(__name__)

@app.route('/')
def vert_calc():
    form = Calculator()
    render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=False)
    