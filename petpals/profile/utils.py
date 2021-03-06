import os
from io import BytesIO
from math import floor
from secrets import token_urlsafe

from flask_login import current_user
from petpals import app
from PIL import Image
from werkzeug.datastructures import FileStorage


def get_image_memory_size(picture_data: FileStorage):
    "Gets image's number in mebibytes (MB)"
    img_byte_arr = BytesIO()
    picture_data.save(img_byte_arr)

    # 1048576 = 2^20 = 1 mebibyte
    mebibytes = len(img_byte_arr.getvalue()) / 1048576

    # Floored to avoid user frustration
    return floor(mebibytes)


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

    with Image.open(picture_data) as image:
        # Crop image to a 1:1 ratio
        center = (image.width / 2.0, image.height / 2.0)
        if image.height > image.width:
            top = round(center[1] - (image.width / 2.0))
            bottom = top + image.width
            image = image.crop((0, top, image.width, bottom))
        elif image.width > image.height:
            left = round(center[0] - (image.height / 2.0))
            right = left + image.height
            image = image.crop((left, 0, right, image.height))

        image = image.resize((256, 256), Image.LANCZOS)

        image.save(get_image_path(filename, rel_path), optimize=True)

    if profile.image_file != 'default.jpg':
        try:
            os.remove(get_image_path(profile.image_file, rel_path))
        except OSError:
            pass

    return filename


def save_recent_photo(picture_data: FileStorage, pet, id: int) -> str:
    "Saves a recent photo and returns its filename"

    rel_path = os.path.join('pet', 'recent')

    f_ext = os.path.splitext(picture_data.filename)[1]
    filename = generate_image_name(f_ext, rel_path)

    # Resize image
    with Image.open(picture_data) as image:
        if image.height > image.width:
            size = (round(image.width * (1080.0 / image.height)), 1080)
        else:
            size = (1080, round(image.height * (1080.0 / image.width)))
        image = image.resize(size, Image.LANCZOS)

        image.save(get_image_path(filename, rel_path), optimize=True)

    if getattr(pet, f'img{id}_path'):
        try:
            os.remove(get_image_path(getattr(pet, f'img{id}_path'), rel_path))
        except OSError:
            pass

    return filename
