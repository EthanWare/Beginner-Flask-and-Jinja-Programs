from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def students():
    students = ['Ethan','Evan','Calvin','Andrew','Tyler','Bill','Alex']
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)