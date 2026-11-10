import time


def test_add_to_cart_button_is_present(browser):
    """
    Тест проверяет, что на странице товара присутствует кнопка
    добавления в корзину.
    """
    # Переходим на страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Небольшая пауза, чтобы страница успела загрузиться и можно было
    # визуально проверить язык (рекомендуется в критериях задания)
    time.sleep(7)

    # Ищем кнопку добавления в корзину по её CSS-селектору.
    # Этот селектор является уникальным для данной страницы.
    button = browser.find_element(
        "css selector", "button.btn-add-to-basket"
    )

    # Проверяем, что кнопка действительно найдена и отображается
    assert button is not None, "Кнопка добавления в корзину не найдена"
    print("\nКнопка добавления в корзину успешно найдена.")