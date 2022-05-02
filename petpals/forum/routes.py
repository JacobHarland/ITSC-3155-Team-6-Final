from flask import Blueprint, render_template, request
from petpals.models import Post, db
from sqlalchemy import or_

from .utils import utility_processor

router = Blueprint(
    'forum_router', __name__, template_folder='templates', url_prefix='/forum'
)


@router.get('')
def forum():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.paginate(page=page, per_page=5)
    return render_template('forum.html', posts=posts)


@router.get('/search')
def search():
    search_param = request.args.get('search_param')
    posts = (
        db.session.query(Post)
        .filter(
            or_(
                Post.content.ilike('%' + search_param + '%'),
                Post.title.ilike('%' + search_param + '%'),
            )
        )
        .all()
    )
    return render_template('forum.html', posts=posts)


router.context_processor(utility_processor)
