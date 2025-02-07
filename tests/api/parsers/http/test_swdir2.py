import pandas as pd
import pytest
import yaml

from ndbc_api.api.parsers.http.swdir2 import Swdir2Parser
from tests.api.parsers.http._base import PARSED_TESTS_DIR, RESPONSES_TESTS_DIR

TEST_FP = RESPONSES_TESTS_DIR.joinpath('swdir2.yml')
PARSED_FP = PARSED_TESTS_DIR.joinpath('swdir2.parquet.gzip')


@pytest.fixture
def swdir2_response():
    with open(TEST_FP, 'r') as f:
        data = yaml.safe_load(f)
    yield data


@pytest.fixture
def parsed_swdir2():
    df = pd.read_parquet(PARSED_FP)
    yield df


@pytest.fixture
def swdir2():
    yield Swdir2Parser


@pytest.mark.private
def test_available_measurements(swdir2, swdir2_response, parsed_swdir2):
    resp = swdir2_response
    want = parsed_swdir2
    got = swdir2.df_from_responses(resp, use_timestamp=True)
    pd.testing.assert_frame_equal(got,
                                  want,
                                  check_dtype=False,
                                  check_index_type=False)
