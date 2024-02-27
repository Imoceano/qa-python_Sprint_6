

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver

   
   
    def find_element_with_wait(self,locator):
        WAIT(self.driver, 10).until(EC.visibility_of_element_located(locator)) #Поиск элемента с ожиданием
        return self.driver.find_element(*locator)
    
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click() #клик на элемент

    def get_text_from_element(self,locator):
        element = self.find_element_with_wait(locator) #Получить текст элемента
        return element.text
    

    
    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #Скролл к подвалу
    
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element) #Скролл к элементу

    def get_url(self,url):
        self.driver.get(url)

    def switch_window(self,element):
        self.driver.switch_to.window(self.driver.window_handles[element])
    
    def check_element_on_page(self,locator):
        self.driver.is_element_present(locator)