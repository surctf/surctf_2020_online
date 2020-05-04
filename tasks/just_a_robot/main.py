from flask import Flask, send_file

app = Flask(__name__)
app.secret_key = "keklolorbidol"

@app.route('/')
@app.route('/index.html')
def index():
	return "Тут ничего нет, правда"

@app.route('/robots.txt')
def for_robots():
	return send_file('robots.txt')

@app.route('/super_secret_place/')
def secret_place():
	return send_file('secret.html')

@app.errorhandler(404)
def page_not_found(e):
    return "Говорю же, НИЧЕГО!!!!!d093d0bbd183d0bfd18bd0b920d187d0b5d0bbd0bed0b2d0b5d187d0b5d188d0bad0b0"

if __name__ == "__main__":
	app.run(port=9003, debug=False, threaded=True)