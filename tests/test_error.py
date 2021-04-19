import pytest

import fondat.error

from http import HTTPStatus
from fondat.error import error_for_status


def test_get_error_int():
    assert error_for_status(400) == fondat.error.BadRequestError
    assert error_for_status(404) == fondat.error.NotFoundError
    assert error_for_status(200) == fondat.error.InternalServerError
    assert error_for_status(200, None) is None


def test_get_error_http_status():
    assert error_for_status(HTTPStatus.BAD_REQUEST) == fondat.error.BadRequestError
    assert error_for_status(HTTPStatus.NOT_FOUND) == fondat.error.NotFoundError
    assert error_for_status(HTTPStatus.OK) == fondat.error.InternalServerError
    assert error_for_status(HTTPStatus.OK, None) is None
