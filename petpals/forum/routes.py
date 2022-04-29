from flask import Blueprint, render_template
from petpals.models import Post

router = Blueprint('forum_router', __name__, template_folder='templates', url_prefix="/forum")


@router.get('')
def forum():
    posts = Post.query.all()
    return render_template('forum.html', posts=posts)
