import pytest
from pages.main_page import MainPage


@pytest.fixture(scope='module')
def mp(pages) -> MainPage:
    return pages.main_page


@pytest.mark.xfail(reason='Wrong text')
def test_failed_logo_text(mp):
    assert mp.get_text(mp.LOGO_FIELD) == mp.LOGO_TEXT + 's'
