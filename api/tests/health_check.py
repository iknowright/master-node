import pytest

from tests import AssertResponse, assert_get

ROUTE = "/health"

HEADERS = {}

PAYLOAD = {}

INPUT = {"success": {"headers": HEADERS, "query": PAYLOAD}}

OUTPUT = {"success": AssertResponse(200, "OK")}


@pytest.mark.parametrize("test_type", INPUT.keys())
def test_get(test_type):
    assert_get(ROUTE, INPUT[test_type], OUTPUT[test_type])
