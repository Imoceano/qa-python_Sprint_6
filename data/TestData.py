from selenium.webdriver.common.by import By
import datetime
import random
from locators.order_page_locators import OrderPageLocators as OPL


class TextOfQuestion:
        question_answer1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        question_answer2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        question_answer3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        question_answer4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        question_answer5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        question_answer6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        question_answer7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        question_answer8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
class Urls:
    HOME_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
    DZEN_PAGE_URL = 'https://dzen.ru/?yredirect=true'
    ORDER_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/order'

class OrderData:
    NAME = random.choice(["Ник", "Ашот", "Роман", "Сэм"])
    DATA = datetime.datetime(2024, random.randint(2, 12), random.randint(1, 28))
    LAST_NAME = random.choice (["Шрек", "Ванукян", "Иванов", "Смит"])
    ADDRESS = random.choice(["Нью-Йорк", "Санкт-Петербург", "Ереван", "Сан-Диего"])
    PHONE_NUMBER = random.randint(10000000000, 99999999999)
    COMMENT = random.choice(['Вингардиум левиоса', 'Акцио', 'Авада', 'Пельмени'])
    METRO_STATION = random.choice(["Черкизовская", "Фили", "Теплый стан", "ВДНХ"])

    

    TIME_OF_RENT = random.choice(OPL.LOCATORS_TIME_RENT)

    

    COLOR_OF_SCOOTER = random.choice(OPL.LOCATORS_CHECK_BOX_COLOR)


    