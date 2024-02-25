from selenium.webdriver.common.by import By


class OrderPageLocators:
    

    ORDER_BUTTON_HEADER = By.XPATH, "//button[@class='Button_Button__ra12g']"
    ORDER_BUTTON_MIDDLE_PAGE = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"
    ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    CONFIRM_BUTTON = By.XPATH, "//button[text()='Да']"
    VIEW_BUTTON = By.XPATH, "//button[text()='Посмотреть статус']"

    CANCEL_ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']"
    LOGO_SCOOTER_BUTTON = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"
    LOGO_YANDEX_BUTTON = By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"
    HOME_HEADER = By.XPATH, "//div[@class='Home_Header__iJKdX']"

    INPUT_FIRST_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    INPUT_SECOND_NAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    INPUT_ADDRESS= By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    INPUT_PHONE_NUMBER = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    INPUT_DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    INPUT_TIME_OF_RENT = By.XPATH, "//div[@class='Dropdown-control']"
    FIRST_VAR_TIME_OF_RENT = By.XPATH, "//div[text()='сутки']"
    INPUT_METRO_STATION = By.XPATH, "//input[@class='select-search__input']"
    CHOOSE_METRO_STATION = By.XPATH, "//li[@data-index='0']"
    CHOOSE_COLOR_SCOOTER = By.CLASS_NAME, 'Checkbox_Input__14A2w'
    INPUT_COMMENT = By.XPATH, './/input[@class = "Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder = "Комментарий для курьера"]'
    MODAL_WINDOW_SUCCESSFUL_ORDER = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"
    COOKIE_BUTTON = By.XPATH, "//button[text()='да все привыкли']"
    ORDER_HEADER = By.XPATH, "//div[@class='Order_Header__BZXOb']"
    DZEN = By.CLASS_NAME, 'dzen-desktop__widget-r2'

