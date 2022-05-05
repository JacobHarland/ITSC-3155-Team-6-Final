import re

from flask import url_for
from markdown import markdown
from markupsafe import Markup


def replace_markup(match: re.Match) -> str:
    if match['pet']:
        url = url_for(
            'profile_router.profile_pet', username=match['user'], pet_name=match['pet']
        )
    else:
        url = url_for("profile_router.profile_user", username=match['user'])

    return f'<a href="{url}">{match[0]}</a>'


def utility_processor():
    def content_markup(content: str) -> Markup:
        RE = r'(?:(?<=\s)|(?<=^))@(?P<user>[\w-]+)(?:\[(?P<pet>[\w -]+)\])?'

        content = Markup.escape(content)
        content = re.sub(RE, replace_markup, content)
        content = markdown(content)
        return Markup(content)

    return dict(content_markup=content_markup)
