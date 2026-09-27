import pytest
from pages.main_page import MainPage


def test_python_download_link_in_second_iframe(driver, target_url):
    main_page = MainPage(driver)

    # открытие сайта
    main_page.open(target_url)

    #переключение во втрой фрейм
    frame = main_page.switch_to_second_iframe()

    #переход к разделу загрузок
    frame.go_to_downloads()
    download_url = frame.get_python_stable_download_url()

    #проверка валидности
    assert download_url is not None, "Ссылка на стабильную версию Python не найдена!"
    assert "selenium" in download_url.lower(), f"Неверная ссылка: {download_url}"
    assert "pypi.org" in download_url or "github.com" in download_url, (
        f"Ожидался URL ведущий на pypi/github, получено: {download_url}"
    )

    main_page.leave_iframe()
