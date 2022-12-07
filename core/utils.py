import os
from django.conf import settings


def delete_upload_file(file_path):
    if not os.path.isfile(file_path):
        return False
    if not file_path.startswith(settings.MEDIA_ROOT):
        return False
    if os.path.exists(file_path):
        os.remove(file_path)
