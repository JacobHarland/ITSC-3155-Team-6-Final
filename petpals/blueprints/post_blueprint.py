from flask import Blueprint, redirect, render_template, url_for

router = Blueprint('profile_router', __name__, url_prefix='/post')


@router.get('')
def post():
    return render_template('post.html')


@router.post('')
def create_post():
    # TODO: Add post to DB
    # TODO: Redirect to post
    return redirect(url_for('post_router.post'))


@router.get('/form')
def post_form():
    return render_template('post_form.html')
