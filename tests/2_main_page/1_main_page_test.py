import allure
import pytest
from pages.main_page import MainPage


@pytest.fixture(scope='module')
def mp(pages) -> MainPage:
    return pages.main_page


@allure.title('Главная страница')
@allure.description('Тест проверки наличия элементов главной страницы')
@allure.tag("Selenium")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Komarov Maksim")
@pytest.mark.parametrize(
        'el', [
            MainPage.LOGO_FIELD,
            MainPage.BURGER_BTN,
            MainPage.CART_BTN,
            MainPage.TITLE_FIELD,
        ],
        ids=['logo_field', 'burger_btn', 'cart_btn', 'title_field']
        
)
def test_check_main_page_elements(mp, el):
    """Тест на наличие на сранице элементов
    """
    assert mp.locate_element(el)


@allure.title('Главная страница')
@allure.description('Тест на клик всех кнопок добавления в корзину и проверка счетчика')
@allure.tag("Selenium")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Komarov Maksim")
def test_add_to_cart_counter(mp):
    """Тест на клик всех кнопок добавления в корзину и проверка счетчика
    """
    atcb = mp.locate_elements(mp.ADD_TO_CART_BTN)
    for btn in atcb:
        btn.click()
    assert mp.get_text(mp.CART_COUNTER) == '6'


@allure.title('Главная страница')
@allure.description('Тест на клик всех кнопок удаления из корзины и проверка отсутствия счетчика')
@allure.tag("Selenium")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Komarov Maksim")
def test_rm_from_cart_counter(mp):
    """Тест на клик всех кнопок удаления из корзины и проверка отсутствия счетчика
    """
    atcb = mp.locate_elements(mp.RM_TO_CART_BTN)
    for btn in atcb:
        btn.click()
    assert mp.not_locate_element(mp.CART_COUNTER)
