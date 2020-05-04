from flask import Flask

from flask import render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<id>')
def flag(id=None):
    if id is None:
        return redirect('/')
    if int(id) == 31337:
        return "surctf_its_not_rick_astley"
    else:
        return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=31337)
