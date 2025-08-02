import pytest
from pages.start_page import StartPage


@pytest.fixture(scope='module')
def sp(pages) -> StartPage:
    return pages.start_page


def test_title(sp):
    assert sp.get_title == sp.TITLE
def test_header_text(sp):
    assert sp.get_text(sp.HEADER) == sp.HEADER_TEXT


@pytest.mark.parametrize(
        'el', [
            StartPage.HEADER,
            StartPage.USER_FIELD,
            StartPage.PASS_FIELD,
            StartPage.LOGIN_BTN,
        ],
        ids=['header', 'user_field', 'pass_field', 'login_btn']
        
)
def test_check_start_page_elements(sp, el):
    assert sp.locate_element(el)
