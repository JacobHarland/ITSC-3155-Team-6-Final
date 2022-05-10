from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from petpals import db
from petpals.models import Post, Reply, ReplyLike

from .forms import ReplyForm

router = Blueprint('reply_router', __name__, template_folder='templates')


@router.route('/<int:post_id>/reply/create', methods=['GET', 'POST'])
@login_required
def reply_new(post_id):
    post = Post.query.get_or_404(post_id)
    form = ReplyForm()
    if form.validate_on_submit():
        reply = Reply(
            content=form.content.data, user_id=current_user.id, post_id=post_id
        )
        db.session.add(reply)
        db.session.commit()

        flash('Replied Sucessfully!', 'success')
        return redirect(
            url_for(
                'forum_router.post_router.post',
                post_id=post_id,
                _anchor=f'reply{reply.reply_id}',
            )
        )

    elif request.method == 'GET':
        return render_template('new_reply.html', post=post, form=form)


@router.post('/reply/like')
@login_required
def reply_like():
    reply = request.json.get('id')
    reply = Reply.query.get_or_404(reply)

    current_user_like = reply.likes.filter_by(user_id=current_user.id).first()
    if current_user_like:
        current_user_like.liked = not current_user_like.liked
        liked = current_user_like.liked
    else:
        db.session.add(ReplyLike(user_id=current_user.id, reply_id=reply.reply_id))
        liked = True
    db.session.commit()

    return {'liked': liked}


@router.route('/<int:post_id>/reply/<int:reply_id>/edit', methods=['GET', 'POST'])
@login_required
def reply_edit(post_id, reply_id):
    post = Post.query.get_or_404(post_id)
    reply = Reply.query.get_or_404(reply_id)

    if reply.user_id != current_user.id:
        abort(403)
    elif post.post_id != reply.post_id:
        abort(404)

    form = ReplyForm()
    if form.validate_on_submit():
        reply.content = form.content.data
        db.session.commit()
        flash('Edited Reply Sucessfully!', 'success')
        return redirect(
            url_for(
                'forum_router.post_router.post',
                post_id=post_id,
                _anchor=f'reply{reply.reply_id}',
            )
        )

    form.content.data = reply.content
    return render_template('edit_reply.html', post=post, reply=reply, form=form)


@router.post('/<int:post_id>/reply/<int:reply_id>/delete')
@login_required
def reply_delete(post_id, reply_id):
    post = Post.query.get_or_404(post_id)
    reply = Reply.query.get_or_404(reply_id)

    if reply.user_id != current_user.id:
        abort(403)
    elif post.post_id != reply.post_id:
        abort(404)

    db.session.delete(reply)
    db.session.commit()

    flash('Your reply has been deleted!', 'success')
    return redirect(url_for('forum_router.post_router.post', post_id=post_id))
