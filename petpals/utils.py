import os
import secrets
from flask_login import current_user
from petpals import app

def save_picture(form_picture):
    # random name for each file uploaded
    random_hex = secrets.token_hex(8)
    # _ for unused variables
    # returns and splits the text and file type of the file uploaded by user
    _, f_ext = os.path.splitext(form_picture.filename)
    # combine random hex with file extension in order to save it
    picture_filename = random_hex + f_ext
    # path of location to save the file
    picture_path = os.path.join(app.root_path, 'static/images/profile_pictures', picture_filename)

    form_picture.save(picture_path)

    prev_picture = os.path.join(app.root_path, 'static/images/profile_pictures', current_user.image_file)
    if os.path.exists(prev_picture) and current_user.image_file != 'default.jpg':
        os.remove(prev_picture)

    return picture_filename