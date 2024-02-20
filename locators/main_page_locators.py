from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTION_LOC = By.ID, 'accordion__heading-{}'
    ANSWER_LOC = By.XPATH, ".//div[@aria-labelledby = 'accordion__heading-{}']"
    ORDER_BUTTON_HEADER = By.CLASS_NAME, 'Button_Button__ra12g'
    ORDER_BUTTON_MIDDLE_PAGE = By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM'
    SCROLL_LOCATOR = By.XPATH, ".//div[@class= 'Home_SubHeader__zwi_E' and text() = 'Вопросы о важном']"