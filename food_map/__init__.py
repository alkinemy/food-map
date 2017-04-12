from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def show_map():
	return render_template('map_test.html')