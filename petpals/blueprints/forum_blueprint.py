from flask import Blueprint, render_template

router = Blueprint('forum_router', __name__, url_prefix="/forum")


@router.get('')
def forum():
    return render_template('forum.html')
