## Описание
Демонстрационные автотесты https://www.saucedemo.com/ с использованием selenium, pytest, allure и других инструментов.

## Установка
- Установить техстек
- Выполнить команду pip install -r requirements.txt

## Запуск
Запуск тестов производится командой python -m pytest tests Для генерации отчета Allure добавить флаг --alluredir allure-results
Для создания и запуска отчета выполнить команду allure serve allure-results

При коммите и ручном запуске происходит автотестирование кода с помощью GitHub Actions, при этом автоматически создается и загружается
в Github Pages allure-отчет.
