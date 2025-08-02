from time import sleep
import pytest
from pages.start_page import StartPage
from pages.main_page import MainPage


@pytest.fixture(scope='module')
def sp(pages) -> StartPage:
    return pages.start_page

@pytest.fixture(scope='module')
def mp(pages) -> MainPage:
    return pages.main_page

@pytest.mark.parametrize(
        'usr, pswrd, error_text', [
            ('', '', StartPage.NO_USERNAME_TEXT),
            ('maks', '', StartPage.NO_PSWRD_TEXT),
            ('maks', '1234', StartPage.WRONG_CREDS),
            
        ],
        ids=['no_creds', 'no_password', 'wrong_creds']
)
def test_negative_credentials(sp, usr, pswrd, error_text):
    """Тест на ввод неверных креденшелов
    """
    sp.send_text(sp.USER_FIELD, usr)
    sp.send_text(sp.PASS_FIELD, pswrd)
    sp.click_element(sp.LOGIN_BTN)
    assert sp.get_text(sp.ERR_TEXTFIELD) == error_text

def test_positive_auth(sp, mp):
    """Тест на корректну. авторизацию standart_user
    """
    sp.send_text(sp.USER_FIELD, 'standard_user')
    sp.send_text(sp.PASS_FIELD, 'secret_sauce')
    sp.click_element(sp.LOGIN_BTN)
    assert mp.verify_main_page