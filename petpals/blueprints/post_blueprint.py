from flask import Blueprint, redirect, render_template, url_for, flash, request
from flask_login import current_user, login_required
from petpals.forms import NewPostForm
from petpals.models import Post
from petpals import db

router = Blueprint('post_router', __name__, url_prefix='/post')


@router.get('')
def post():
    return render_template('post.html')

@router.route('/form', methods=['GET', 'POST'])
@login_required #user must be logged into create a post
def post_form():
    form = NewPostForm()
    if form.validate_on_submit():
        poster = current_user.id
        post = Post(title=form.title.data, content=form.content.data, user_id=poster)

        #Add Post to databse
        db.session.add(post)
        db.session.commit()

        #Return a Success Message
        flash('Forum Post Submitted Sucessfully!', 'success')
        return redirect(url_for('forum'))
    
    elif request.method == 'GET':
        return render_template('post_form.html', form=form)
