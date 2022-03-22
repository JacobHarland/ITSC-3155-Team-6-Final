from flask import Flask, abort, redirect, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/forum')
def forum():
    return render_template('forum.html')

@app.get('/post')
def post():
    return render_template('post.html')

@app.route('/post_form', methods=['GET','POST'])
def post_form():
    return render_template('post_form.html')