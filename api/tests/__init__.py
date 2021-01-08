"""Testing module"""
from fastapi.testclient import TestClient

from app import APP


CLIENT = TestClient(APP)


class AssertResponse:

    status_code = 200
    body = "OK"

    def __init__(self, status_code=200, body="OK"):
        self.status_code = status_code
        self.body = body


def assert_get(route: str, request: dict, response: AssertResponse):
    """Testing GET method assertions

    Arguments:
        route {str} -- Request route
        request {dict} -- Request dict, must have `query` property
        response {AssertResponse} -- Response
    """

    resp = CLIENT.get(f"{route}", headers=request["headers"], params=request["query"],)

    assert (
        resp.status_code == response.status_code
    ), f"{resp.status_code} does not match {response.status_code}"
    assert resp.text == response.body, f"{resp.text} does not match {response.body}"


def assert_post(route: str, request: dict, response: AssertResponse):
    """Testing POST method assertions

    Arguments:
        route {str} -- Request route
        request {dict} -- Request dict, must have `headers`, `payload` property
        response {AssertResponse} -- Response
    """

    resp = CLIENT.post(f"{route}", headers=request["headers"], json=request["payload"],)

    assert (
        resp.status_code == response.status_code
    ), f"{resp.status_code} does not match {response.status_code}"
    assert resp.text == response.body, f"{resp.text} does not match {response.body}"


def assert_delete(route: str, request: dict, response: AssertResponse):
    """Testing POST method assertions

    Arguments:
        route {str} -- Request route
        request {dict} -- Request dict, must have `headers`, `payload` property
        response {AssertResponse} -- Response
    """

    resp = CLIENT.delete(
        f"{route}", headers=request["headers"], json=request["payload"],
    )

    assert (
        resp.status_code == response.status_code
    ), f"{resp.status_code} does not match {response.status_code}"
    assert resp.text == response.body, f"{resp.text} does not match {response.body}"
