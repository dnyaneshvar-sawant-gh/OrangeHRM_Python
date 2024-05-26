import random
import string
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.readProperties import ReadConfig
from pageObjects import LoginPage
from pageObjects import AddEmployee
from utilities.customLogger import LogGen


def generate_random_string(length):
    characters = string.ascii_lowercase
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


class Test_003_AddEmployee:
    url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    first_name = generate_random_string(5)
    last_name = generate_random_string(5)
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_employee(self, setup):
        self.logger.info("***************** Test_003_AddEmployee **************")
        self.logger.info("***************** Verifying Add Employee Test **************")
        self.driver = setup
        self.lp = LoginPage.LoginPage(self.driver)
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.lp.username_textbox_xpath))
        )
        self.lp.do_login(self.username, self.password)
        self.ae = AddEmployee.AddEmp(self.driver)
        self.ae.add_emp_without_login_details(self.first_name, self.last_name)
        wait.until(
            expected_conditions.visibility_of_element_located((By.ID, self.ae.success_message_id))
        )
        actual_message = self.ae.get_success_message()

        if "Successfully Saved" in actual_message:
            self.logger.info("******************** Add Employee test Passed *******************")
            assert True
        else:
            time.sleep(2)
            self.driver.save_screenshot(".\\Screenshots\\" + "addEmpFailed.png")
            self.logger.info("******************** Add Employee test Failed *******************")
            allure.attach(self.driver.get_screenshot_as_png(), name="addEmployeeTest",
                          attachment_type=AttachmentType.PNG)
            assert False
        self.driver.close()
