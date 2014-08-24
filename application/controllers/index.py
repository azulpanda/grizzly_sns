from flask import render_template
from application import app

@app.route('/')
def layout():
	return render_template('layout.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return render_template('404.html')