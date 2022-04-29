from flask import Blueprint, render_template, request
from petpals.models import Post, db

router = Blueprint(
    "forum_router", __name__, template_folder="templates", url_prefix="/forum"
)


@router.get("")
def forum():
    posts = Post.query.all()
    return render_template("forum.html", posts=posts)


@router.post("/search")
def search():
    search_param = request.form["search_param"]
    posts = db.session.query(Post).filter(Post.content.contains(search_param)).all()
    return render_template("forum.html", posts=posts)
