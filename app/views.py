from app import app
from flask import render_template


@app.route('/')
def get_page_home():
    return render_template('home.html')
