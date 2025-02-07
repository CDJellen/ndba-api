import pytest
import yaml

from ndbc_api.api.requests.opendap.stdmet import StdmetRequest
from tests.api.requests.opendap._base import (HISTORICAL_END, HISTORICAL_START,
                                              REALTIME_END, REALTIME_START,
                                              REQUESTS_TESTS_DIR)

TEST_FP = REQUESTS_TESTS_DIR.joinpath('stdmet.yml')
TEST_STN = 'tplm2'


@pytest.fixture
def stdmet():
    yield StdmetRequest


@pytest.fixture
def stdmet_requests():
    with open(TEST_FP, 'r') as f:
        data = yaml.safe_load(f)
    yield data


@pytest.fixture
def stdmet_realtime_requests(stdmet_requests):
    yield stdmet_requests.get('realtime')


@pytest.fixture
def stdmet_historical_requests(stdmet_requests):
    yield stdmet_requests.get('historical')


@pytest.mark.private
def test_stdmet_realtime(stdmet, stdmet_realtime_requests):
    want = stdmet_realtime_requests
    got = stdmet.build_request(TEST_STN, REALTIME_START, REALTIME_END)
    assert want == got


@pytest.mark.private
def test_stdmet_historical(stdmet, stdmet_historical_requests):
    want = stdmet_historical_requests
    got = stdmet.build_request(TEST_STN, HISTORICAL_START, HISTORICAL_END)
    assert want == got
