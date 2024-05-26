import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchEmp:
    # need to change the xpath
    emp_list_xpath = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a"
    emp_name_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
    emp_id_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input"
    search_button_xpath = "//button[@type='submit']"
    results_name_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div"

    def __init__(self, driver):
        self.driver = driver

    def get_result(self):
        wait = WebDriverWait(self.driver, 10)
        result = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.results_name_xpath))
        )
        return result.text

    def search_emp_by_name(self, name):
        self.driver.find_element(By.XPATH, self.emp_list_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.emp_name_xpath))
        )
        element.send_keys(name)
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        result = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.results_name_xpath))
        )
        return result.text

    def search_emp_by_id(self, emp_id):
        self.driver.find_element(By.XPATH, self.emp_list_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.emp_id_xpath))
        )
        element.send_keys(emp_id)
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        result = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.results_name_xpath))
        )
        return result.text
