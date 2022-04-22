import os
from secrets import token_urlsafe

from flask_login import current_user
from PIL import Image
from werkzeug.datastructures import FileStorage

from petpals import app


def save_profile_picture(form_picture: FileStorage) -> str:
    "Saves profile picture and returns its filename"

    def get_picture_path(filename):
        return os.path.join(app.root_path, 'static', 'images', 'profile_pictures', filename)

    # Get file extension
    f_ext = os.path.splitext(form_picture.filename)[1]

    while True:
        filename = token_urlsafe(8) + f_ext
        if not os.path.isfile(get_picture_path(filename)):
            break

    image = Image.open(form_picture)
    if image.width * (29/23) < image.height:
            # Check if it's too long vertically
            size = (round(image.width * (290.0 / image.height)), 290)
    else:
        size = (230, round(image.height * (230.0 / image.width)))

    image = image.resize(size, Image.LANCZOS)
    image.save(get_picture_path(filename), optimize=True)

    if not current_user.image_file is None:
        os.remove(get_picture_path(current_user.image_file))

    return filename

def save_pet_profile_picture(pet, form_profile_picture: FileStorage) -> str:
    "Saves profile picture and returns its filename"

    def get_picture_path(filename):
        return os.path.join(app.root_path, 'static', 'images', 'pet_pictures', filename)

    # Get file extension
    f_ext = os.path.splitext(form_profile_picture.filename)[1]

    while True:
        filename = token_urlsafe(8) + f_ext
        if not os.path.isfile(get_picture_path(filename)):
            break

    image = Image.open(form_profile_picture)
    if image.width * (29/23) < image.height:
            # Check if it's too long vertically
            size = (round(image.width * (290.0 / image.height)), 290)
    else:
        size = (230, round(image.height * (230.0 / image.width)))

    image = image.resize(size, Image.LANCZOS)
    image.save(get_picture_path(filename), optimize=True)

    if not pet.image_file is None:
        os.remove(get_picture_path(pet.image_file))

    return filename
