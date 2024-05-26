import time

import allure
from allure_commons.types import AttachmentType
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utilities.customLogger import LogGen

from pageObjects import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_Login:
    url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_homepage_title(self, setup):
        self.logger.info("*************** Test_001_Login ***************")
        self.driver = setup
        self.driver.get(url=self.url)
        actual_title = "OrangeHRM"
        if self.driver.title == actual_title:
            self.logger.info("************* test_homepage_title test passed *****************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.logger.info("************* test_homepage_title test failed *****************")
            allure.attach(self.driver.get_screenshot_as_png(), name="testHomepage", attachment_type=AttachmentType.PNG)
            assert False

        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):
        self.logger.info("*************** Login test started ***************")
        self.driver = setup
        self.driver.get(url=self.url)
        self.lp = LoginPage.LoginPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.lp.username_textbox_xpath))
        )
        self.lp.do_login(self.username, self.password)
        time.sleep(4)
        if self.driver.title == "OrangeHRM":
            self.logger.info("************* login test passed *****************")
            assert True
        else:
            time.sleep(2)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.info("************* login test failed *****************")
            allure.attach(self.driver.get_screenshot_as_png(), name="testLogin", attachment_type=AttachmentType.PNG)
            assert False

        self.driver.close()
