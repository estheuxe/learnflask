from app import app
from flask import render_template

# корневая директория
@app.route('/')
def index():
	name = 'Joseph'
	return render_template('index.html', n=name)
