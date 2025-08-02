import allure
import pytest
from pages.main_page import MainPage


@pytest.fixture(scope='module')
def mp(pages) -> MainPage:
    return pages.main_page


@allure.title('Главная страница')
@allure.description('Тест на проверку текста лого')
@allure.tag("Selenium")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Komarov Maksim")
@pytest.mark.xfail(reason='Wrong text')
def test_failed_logo_text(mp):
    """Намеренная ошибка в тесте проверки текста лого"""
    assert mp.get_text(mp.LOGO_FIELD) == mp.LOGO_TEXT + 's'
