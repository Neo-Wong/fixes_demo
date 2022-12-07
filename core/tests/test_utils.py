from core import utils as _u


def test_empty_file_path():
    assert _u.delete_upload_file('file_path') is False


def test_error_upload_file_path():
    assert _u.delete_upload_file(__file__) is False
