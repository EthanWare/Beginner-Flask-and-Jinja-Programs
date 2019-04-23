from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def advanced():
    students = ['Ethan','Evan','Calvin','Andrew','Tyler','Bill','Alex']
    return render_template('advanced.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
