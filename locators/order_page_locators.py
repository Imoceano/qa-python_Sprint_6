from selenium.webdriver.common.by import By

class OrderPageLocators:
    INPUT_FIRTS_NAME = By.XPATH, './/input[@class = "Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder = "* Имя"]'
    INPUT_LAST_NAME = By.XPATH, './/input[@class = "Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder = "* Фамилия"]'
    INPUT_ADDRESS = By.XPATH, './/input[@class = "Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder = "* Адрес: куда привезти заказ"'
    INPUT_METRO_STATION = By.XPATH, './/input[@class = "select-search__input" and @placeholder = "* Станция метро"]'
    VIDGET_METRO_STATION = By.XPATH, ".//div[@class = 'select-search__select']"

    INPUT_PHONE_NUMBER = By.XPATH, './/input[@class = "Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder = "* Телефон: на него позвонит курьер"'

    NEXT_BUTTON = By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM'

    INPUT_DATE_OF_DELIVERY = By.CLASS_NAME, 'Input_Input__1iN_Z Input_Responsible__1jDKN react-datepicker-ignore-onclickoutside'
    CHOOSE_DATE_ON_CALENDAR = By.XPATH, ".//div[@class = 'react-datepicker__day react-datepicker__day--002 react-datepicker__day--weekend react-datepicker__day--outside-month']"
    
    DROPDOWN_TIME_RENT_FOR_CLICK = By.CLASS_NAME, 'Dropdown-placeholder'
    WAIT_FOR_DROPDOWN_MENU = By.CLASS_NAME, 'Dropdown-menu'
    BUTTON_TIME_FOR_1_DAY = By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'сутки']"
    BUTTON_TIME_FOR_2_DAY = By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'двое суток']"
    BUTTON_TIME_FOR_3_DAY = By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'троке суток']"
    BUTTON_TIME_FOR_4_DAY = By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'четверо суток']"
    BUTTON_TIME_FOR_5_DAY = By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'пятеро суток']" 
    BUTTON_TIME_FOR_6_DAY = By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'шестеро суток']"
    BUTTON_TIME_FOR_7_DAY = By.XPATH, ".//div[@class = 'Dropdown-option' and text() = 'семеро суток']"


    CHECK_BOX_BLACK_COLOR = By.CLASS_NAME, 'Checkbox_Input__14A2w'
    CHECK_BOX_GREY_COLOR = By.CLASS_NAME, 'Checkbox_Label__3wxSf'
    INPUT_COMMENT = By.XPATH, './/input[@class = "Input_Input__1iN_Z Input_Responsible__1jDKN" and @placeholder = "Комментарий для курьера"]'
    GO_BACK_BUTTON = By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i'
    SUBMIT_ORDER_BUTTON = By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM'
    MODAL_WINDOW_SUBMIT_ORDER = By.CLASS_NAME, 'Order_Modal__YZ-d3'
    NO_BUTTON_SUBMIT_ORDER = By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text() = 'Нет']"
    YES_BUTTON_SUBMIT_ORDER = By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Да']"