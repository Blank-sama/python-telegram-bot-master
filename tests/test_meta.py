import os

import pytest

from tests.conftest import env_var_2_bool


@pytest.mark.skipif(
    not env_var_2_bool(os.getenv('TEST_BUILD', False)), reason='TEST_BUILD not enabled'
)
def test_build():
    assert os.system('python setup.py bdist_dumb') == 0  # pragma: no cover


@pytest.mark.skipif(
    not env_var_2_bool(os.getenv('TEST_BUILD', False)), reason='TEST_BUILD not enabled'
)
def test_build_raw():
    assert os.system('python setup-raw.py bdist_dumb') == 0  # pragma: no cover
