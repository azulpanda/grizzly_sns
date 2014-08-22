from flask import render_template
from application import app

@app.route('/')
def layout():
	return render_template('layout.html')

