from flask import Flask, abort, redirect, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/profiles')
def get_profiles():
    for i in range(5):
        return render_template('profile.html')

@app.get('/profiles/<profile_id>')
def get_profile_by_id( profile.profile_id ):
    return render_template('profile.html')

@app.post('/profiles')
def add_profile():
    name = request.form.get('name', '')
    
