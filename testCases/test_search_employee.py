import random
import string
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects import AddEmployee
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects import LoginPage
from pageObjects import SearchEmployee


def generate_random_string(length):
    characters = string.ascii_lowercase
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


class Test_004_SearchEmp:
    url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    first_name = generate_random_string(5)
    last_name = generate_random_string(5)
    logger = LogGen.loggen()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_by_name(self, setup):
        self.logger.info("*************** Test_004_SearchEmp ***************")
        self.logger.info("*************** Verifying test_search_by_name ***************")
        self.driver = setup
        self.driver.get(url=self.url)
        lp = LoginPage.LoginPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, lp.username_textbox_xpath))
        )
        lp.do_login(self.username, self.password)
        ad = AddEmployee.AddEmp(self.driver)
        ad.add_emp_without_login_details(self.first_name, self.last_name)
        time.sleep(4)
        se = SearchEmployee.SearchEmp(self.driver)
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, se.emp_list_xpath))
        )
        search_results = se.search_emp_by_name(self.first_name + " " + self.last_name)
        if self.first_name in search_results:
            self.logger.info("*************** Search Employee by name test Passed ***************")
            assert True
        else:
            self.logger.info("*************** Search Employee by name test Failed ***************")
            self.driver.save_screenshot(".\\Screenshots\\" + "searchByName.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="searchEmpTestByName",
                          attachment_type=AttachmentType.PNG)
            assert False

        self.driver.close()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_by_id(self, setup):
        self.logger.info("*************** Test_004_SearchEmp ***************")
        self.logger.info("*************** Verifying test_search_by_name ***************")
        self.driver = setup
        self.driver.get(url=self.url)
        lp = LoginPage.LoginPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, lp.username_textbox_xpath))
        )
        lp.do_login(self.username, self.password)
        ad = AddEmployee.AddEmp(self.driver)
        ad.add_emp_without_login_details(self.first_name, self.last_name)
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, ad.empId_input_xpath))
        )
        emp_id = self.driver.find_element(By.XPATH, ad.empId_input_xpath).text
        se = SearchEmployee.SearchEmp(self.driver)
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, se.emp_list_xpath))
        )
        search_results = se.search_emp_by_id(emp_id)
        if emp_id in search_results:
            self.logger.info("*************** Search Employee by Emp id Test Passed ***************")
            assert True
        else:
            self.logger.info("*************** Search Employee by Emp id Test Failed ***************")
            self.driver.save_screenshot(".\\Screenshots\\" + "searchById.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="searchEmpTestById",
                          attachment_type=AttachmentType.PNG)
            assert False

        self.driver.close()
