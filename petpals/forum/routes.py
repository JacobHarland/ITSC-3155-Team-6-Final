from flask import Blueprint, render_template, request
from petpals.models import Post, Reply
from sqlalchemy import func, or_

from .utils import utility_processor

router = Blueprint(
    'forum_router', __name__, template_folder='templates', url_prefix='/forum'
)


@router.get('')
def forum():
    sort_by = request.args.get('sort_by', 'newest')
    page = request.args.get('page', 1, type=int)
    search = request.args.get('q')

    post_query = Post.query

    if search:
        post_query = post_query.filter(
            or_(Post.content.ilike(f'%{search}%'), Post.title.ilike(f'%{search}%'))
        )

    # desc: descending
    match sort_by:
        case 'newest':
            post_query = post_query.order_by(Post.post_id.desc())
        case 'no_replies':
            post_query = post_query.outerjoin(Reply).filter_by(post_id=None)
        case 'most_replies':
            post_query = (
                post_query.outerjoin(Reply)
                .group_by(Post.post_id)
                .order_by(func.count(Reply.post_id).desc())
            )
        case 'most_viewed':
            post_query = post_query.order_by(Post.views.desc())

    posts = post_query.paginate(page=page, per_page=5)

    return render_template('forum.html', posts=posts, sort_by=sort_by, search=search)


router.context_processor(utility_processor)
