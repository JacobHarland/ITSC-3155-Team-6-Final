from flask import Blueprint, render_template

router = Blueprint('home_router', __name__, template_folder='templates')


@router.get('/')
def index():
    return render_template('index.html')


@router.get("/about")
def about():
    return render_template('about.html')


@router.get("/faq")
def faq():
    return render_template('faq.html')
