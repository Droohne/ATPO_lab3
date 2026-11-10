import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Добавляет опцию --language в командную строку pytest."""
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Выбор языка интерфейса, например: ru, en, es, fr"
    )


@pytest.fixture(scope="function")
def browser(request):
    """
    Фикстура для запуска браузера Chrome с указанным языком.
    Язык берется из параметра командной строки --language.
    """
    # Получаем значение параметра --language из запроса
    language = request.config.getoption("--language")

    # Настраиваем опции для браузера Chrome
    options = Options()
    # Устанавливаем язык интерфейса через экспериментальную настройку
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': language}
    )
    # Для полного переключения языка можно также добавить аргумент
    options.add_argument(f"--lang={language}")

    # Инициализируем браузер
    print(f"\nЗапуск Chrome с языком: {language}")
    browser = webdriver.Chrome(options=options)

    yield browser

    # Закрываем браузер после завершения теста
    print("\nЗакрытие браузера")
    browser.quit()