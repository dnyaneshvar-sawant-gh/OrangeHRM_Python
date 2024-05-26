import time

from selenium.webdriver.common.by import By


class DeleteEmp:
    delete_button_xpath = "//i[1][@class='oxd-icon bi-trash']"
    delete_popup_xpath = "//*[text()=' Yes, Delete ']"
    success_message_id = "oxd-toaster_1"

    def __init__(self, driver):
        self.driver = driver

    def delete_result(self):
        self.driver.find_element(By.XPATH, self.delete_button_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.delete_popup_xpath).click()

    def get_message(self):
        message = self.driver.find_element(By.ID, self.success_message_id).text
        return message
