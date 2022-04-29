import os
from secrets import token_urlsafe

from flask_login import current_user
from PIL import Image
from werkzeug.datastructures import FileStorage

from petpals import app


def get_image_path(filename: str, *rel_path: str) -> str:
    return os.path.join(app.root_path, 'static', 'images', *rel_path, filename)


def generate_image_name(f_ext: str, rel_path: str) -> str:
    "Generate a random name for the image file and check if there are no duplicates"

    while True:
        filename = token_urlsafe(8) + f_ext
        if not os.path.isfile(get_image_path(filename, rel_path)):
            return filename


def save_profile_picture(picture_data: FileStorage, pet=None) -> str:
    "Saves profile picture and returns its filename"

    if pet:
        profile = pet
        rel_path = os.path.join('pet', 'profile')
    else:
        profile = current_user
        rel_path = os.path.join('user', 'profile')

    # Get filename
    f_ext = os.path.splitext(picture_data.filename)[1]
    filename = generate_image_name(f_ext, rel_path)

    # Resize image
    image = Image.open(picture_data)
    # Check if it's too long vertically
    if image.width * (29/23) < image.height:
        size = (round(image.width * (290.0 / image.height)), 290)
    else:
        size = (230, round(image.height * (230.0 / image.width)))
    image = image.resize(size, Image.LANCZOS)

    image.save(get_image_path(filename, rel_path), optimize=True)

    if profile.image_file != 'default.jpg':
        os.remove(get_image_path(profile.image_file, rel_path))

    return filename


def save_recent_photo(picture_data: FileStorage, pet, id: int) -> str:
    "Saves a recent photo and returns its filename"

    rel_path = os.path.join('pet', 'recent')

    f_ext = os.path.splitext(picture_data.filename)[1]
    filename = generate_image_name(f_ext, rel_path)

    # Resize image
    image = Image.open(picture_data)
    # Check if it's too long vertically
    if image.width < image.height:
        size = (round(image.width * (1080.0 / image.height)), 1080)
    else:
        size = (1080, round(image.height * (1080.0 / image.width)))
    image = image.resize(size, Image.LANCZOS)

    image.save(get_image_path(filename, rel_path), optimize=True)

    if getattr(pet, f'img{id}_path'):
        os.remove(get_image_path(getattr(pet, f'img{id}_path'), rel_path))

    return filename