import allure


@allure.id("34081")
@allure.title("Auth via Google")
@allure.tag("web", "smoke")
@allure.story("External auth")
@allure.label("owner", "allure8")
@allure.feature("Auth")
def test_google_auth():
    with allure.step("Открываем главную страницу"):
        pass
    with allure.step("Выбираем способ авторизации через Google"):
        pass
    with allure.step("Авторизуемся как пользователь 'Mr. Random'"):
        pass
        with allure.step("Вводим Логин - 'random-user@gmail.com'"):
            pass
        with allure.step("Вводим Пароль - random-password"):
            pass
        with allure.step("Нажимаем кнопку - войти"):
            pass
    with allure.step("Проверяем, что авторизация прошла успешно"):
        with allure.step("Expected Result"):
            with allure.step("Данные профиля обновились"):
                pass
            with allure.step("Имя: 'Mr. Random'"):
                pass
            with allure.step("Email: 'random-user@gmail.com'"):
                pass
