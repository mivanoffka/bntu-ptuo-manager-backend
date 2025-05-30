import os
import uuid


def upload_to_images(instance, filename):
    ext = filename.split(".")[-1]

    new_filename = f"{uuid.uuid4().hex}.{ext}"

    return os.path.join("images", new_filename)
