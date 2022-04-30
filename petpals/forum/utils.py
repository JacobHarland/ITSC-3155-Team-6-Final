import re

from flask import url_for
from markupsafe import Markup


def replace_markup(match: re.Match) -> str:
    url = url_for("profile_router.profile_user", username=match[1])
    return f'<a href="{url}">{match[0]}</a>'


def utility_processor():
    def content_markup(content: str) -> Markup:
        safe_content = Markup.escape(content)

        return Markup(re.sub(r'@([\w-]+)', replace_markup, safe_content))

    return dict(content_markup=content_markup)
