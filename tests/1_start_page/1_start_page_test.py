import allure
import pytest
from pages.start_page import StartPage


@pytest.fixture(scope='module')
def sp(pages) -> StartPage:
    return pages.start_page


@allure.title('Стартовая страница')
@allure.description('Тест проверки текста вкладки')
@allure.tag("Selenium")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Komarov Maksim")
def test_title(sp):
    """Тест заголовка вкладки
    """
    assert sp.get_title == sp.TITLE


@allure.title('Стартовая страница')
@allure.description('Тест проверки текста заголовка')
@allure.tag("Selenium")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Komarov Maksim")
def test_header_text(sp):
    """Тест заголовка на странице
    """
    assert sp.get_text(sp.HEADER) == sp.HEADER_TEXT


@allure.title('Стартовая страница')
@allure.description('Тест проверки наличия элементов стартовой страницы')
@allure.tag("Selenium")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Komarov Maksim")
@pytest.mark.parametrize(
        'el', [
            StartPage.HEADER,
            StartPage.USER_FIELD,
            StartPage.PASS_FIELD,
            StartPage.ERR_CNTNR,
            StartPage.LOGIN_BTN,
        ],
        ids=['header', 'user_field', 'pass_field', 'err_cntnr', 'login_btn']
        
)
def test_check_start_page_elements(sp, el):
    """Тест на наличие на сранице элементов
    """
    assert sp.locate_element(el)


@allure.title('Стартовая страница')
@allure.description('Тест проверки кликабельности элементов')
@allure.tag("Selenium")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Komarov Maksim")
@pytest.mark.parametrize(
        'el', [
            StartPage.USER_FIELD,
            StartPage.PASS_FIELD,
            StartPage.LOGIN_BTN,
        ],
        ids=['user_field', 'pass_field', 'login_btn']
        
)
def test_clickable_start_page_elements(sp, el):
    """Тест на кликабельность элементов
    """
    assert sp.is_clickable(el)
