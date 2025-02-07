import pytest
import yaml

from ndbc_api.api.requests.opendap.adcp import AdcpRequest
from tests.api.requests.opendap._base import (HISTORICAL_END, HISTORICAL_START,
                                              REALTIME_END, REALTIME_START,
                                              REQUESTS_TESTS_DIR)

TEST_FP = REQUESTS_TESTS_DIR.joinpath('adcp.yml')
TEST_STN = '41001'


@pytest.fixture
def adcp():
    yield AdcpRequest


@pytest.fixture
def adcp_requests():
    with open(TEST_FP, 'r') as f:
        data = yaml.safe_load(f)
    yield data


@pytest.fixture
def adcp_realtime_requests(adcp_requests):
    yield adcp_requests.get('realtime')


@pytest.fixture
def adcp_historical_requests(adcp_requests):
    yield adcp_requests.get('historical')


@pytest.mark.private
def test_adcp_realtime(adcp, adcp_realtime_requests):
    want = adcp_realtime_requests
    got = adcp.build_request(TEST_STN, REALTIME_START, REALTIME_END)
    assert want == got


@pytest.mark.private
def test_adcp_historical(adcp, adcp_historical_requests):
    want = adcp_historical_requests
    got = adcp.build_request(TEST_STN, HISTORICAL_START, HISTORICAL_END)
    assert want == got
