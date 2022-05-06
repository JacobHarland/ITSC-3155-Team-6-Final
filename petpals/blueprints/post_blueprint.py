from flask import Blueprint, redirect, render_template, url_for, flash, request
from flask_login import current_user, login_required
from petpals.forms import NewPostForm
from petpals.models import Post
from petpals import db

router = Blueprint('post_router', __name__, url_prefix='/post')


@router.route('/posts/<int:post_id>')
def post(post_id):
    #Locate Correct Post
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)


@router.route('/form', methods=['GET', 'POST'])
@login_required  # user must be logged into create a post
def post_form():
    form = NewPostForm()
    if form.validate_on_submit():
        poster = current_user.id
        post = Post(title=form.title.data,
                    content=form.content.data, user_id=poster)

        # Add Post to databse
        db.session.add(post)
        db.session.commit()

        # Return a Success Message
        flash('Forum Post Submitted Sucessfully!', 'success')
        return redirect(url_for('forum'))

    elif request.method == 'GET':
        return render_template('post_form.html', form=form)

@router.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required #User must be logged in to edit a post 
def edit_post(post_id):

    #Locate Correct Post
    post = Post.query.get_or_404(post_id)
    form = NewPostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data

        # Update Database
        db.session.add(post)
        db.session.commit()

        #Success Message
        flash('Post Has Been Updated!', 'success')
        return redirect(url_for('forum', post_id=post.post_id))

    if current_user.id == post.user_id or current_user.id:
        form.title.data = post.title
        form.content.data = post.content
        return render_template('edit_post.html', form=form)
    else:
        flash("You Aren't Authorized To Edit This Post...")
        posts = Post.query.order_by(Post.timestamp)
        return redirect("forum.html", posts=posts)

@router.route('/delete/<int:post_id>')
@login_required
def delete_post(post_id):
	post_to_delete = Post.query.get_or_404(post_id)
	id = current_user.id
	if id == post_to_delete.user_id:
		try:
			db.session.delete(post_to_delete)
			db.session.commit()

			# Return a message
			flash("Blog Post Was Deleted!", 'success')

			# Grab all the posts from the database
			posts = Post.query.order_by(Post.timestamp)
			return redirect("forum.html", posts=posts)


		except:
			# Return an error message
			flash("Whoops! There was a problem deleting post, try again...")

			# Grab all the posts from the database
			posts = Post.query.order_by(Post.timestamp)
			return redirect('post.html', post_id=post.post_id)
	else:
		# Return a message
		flash("You Aren't Authorized To Delete That Post!", 'danger')

		# Grab all the posts from the database
		posts = Post.query.order_by(Post.timestamp)
		return render_template("forum.html", posts=posts)
