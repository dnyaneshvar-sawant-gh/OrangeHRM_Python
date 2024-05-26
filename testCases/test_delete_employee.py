import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects import LoginPage, AddEmployee, SearchEmployee, DeleteEmployee
from testCases.test_add_employee import generate_random_string
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_005_DeleteEmp:
    url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()
    first_name = generate_random_string(5)
    last_name = generate_random_string(5)

    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_emp(self, setup):
        self.logger.info("*************** Test_005_DeleteEmp ***************")
        self.logger.info("*************** Verifying test_delete_emp ***************")
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
        se.search_emp_by_name(self.first_name)
        self.de = DeleteEmployee.DeleteEmp(self.driver)
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.de.delete_button_xpath))
        )
        self.de.delete_result()
        wait.until(
            expected_conditions.visibility_of_element_located((By.ID, self.de.success_message_id))
        )
        actual_message = self.de.get_message()
        if "Successfully Deleted" in actual_message:
            self.logger.info("*************** test_delete_emp passed ***************")
            assert True
        else:
            time.sleep(2)
            self.logger.info("*************** test_delete_emp failed ***************")
            self.driver.save_screenshot(".\\Screenshots\\" + "deleteEmpFailed.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="deleteEmpTest", attachment_type=AttachmentType.PNG)
            assert False

        self.driver.close()
