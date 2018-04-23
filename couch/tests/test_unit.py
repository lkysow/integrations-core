# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest

from datadog_checks.couch import CouchDb

CHECK_NAME = 'couch'
WRONG_CONFIG = {
    "server": "http://localhost:11111"
}
BAD_CONFIG = {}


@pytest.fixture
def aggregator():
    from datadog_checks.stubs import aggregator
    aggregator.reset()
    return aggregator


def test_bad_config(aggregator):

    check = CouchDb(CHECK_NAME, {}, {})
    try:
        check.check(WRONG_CONFIG)
    except Exception:
        assert True
    else:
        assert False, 'Should have raised an exception with wrong configuration'

    aggregator.assert_service_check(
        check.SERVICE_CHECK_NAME,
        status=CouchDb.CRITICAL,
        tags=['instance:http://localhost:11111'],
        count=1
    )
