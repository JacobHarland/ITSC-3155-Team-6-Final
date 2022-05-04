from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from petpals import db
from petpals.models import Post, Reply, ReplyLike

from .forms import NewReplyForm

router = Blueprint(
    'reply_router',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/reply/static',
)


@router.route('/<int:post_id>/reply/create', methods=['GET', 'POST'])
@login_required
def reply_form(post_id):
    post = Post.query.get_or_404(post_id)
    form = NewReplyForm()
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
        return render_template('reply_form.html', post_title=post.title, form=form)


@router.post('/reply/like')
@login_required
def reply_like():
    reply = request.json.get('replyId')
    reply = Reply.query.get_or_404(reply)

    current_user_like = reply.likes.filter_by(user_id=current_user.id).first()
    if current_user_like:
        current_user_like.liked = not current_user_like.liked
        liked = current_user_like.liked
    else:
        db.session.add(ReplyLike(user_id=current_user.id, reply_id=reply.reply_id))
        liked = True
    db.session.commit()

    return jsonify({'liked': liked})
