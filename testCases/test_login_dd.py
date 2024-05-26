import os
import time

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects import LoginPage
from utilities import XLUtils


class Test_002_DDT_Login:
    url = ReadConfig.get_application_url()
    logger = LogGen.loggen()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_folder = os.path.join(current_dir, "..", "TestData")
    path = os.path.join(config_folder, "LoginTestData.xlsx")

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_dd(self, setup):
        self.logger.info("************* Test_002_DDT_Login ***********")
        self.logger.info("************* Verifying login ddt  ***********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp = LoginPage.LoginPage(self.driver)
        list_status = []

        self.rows = XLUtils.get_row_count(self.path, "Sheet1")
        self.columns = XLUtils.get_column_count(self.path, "Sheet1")
        for r in range(2, self.rows + 1):
            self.username = XLUtils.read_data(self.path, "Sheet1", r, 1)
            self.password = XLUtils.read_data(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.read_data(self.path, "Sheet1", r, 3)

            wait = WebDriverWait(self.driver, 10)
            wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.lp.username_textbox_xpath))
            )
            self.lp.do_login(self.username, self.password)
            time.sleep(3)
            try:
                self.driver.find_element(By.XPATH, self.lp.logout_dd_xpath)
                flag = 1
            except Exception as e:
                self.logger.info("******** Exception is: " + str(e) + " *********")
                flag = 0

            if flag == 1:
                if self.exp == "Pass":
                    self.logger.info("******** login successful for " + self.username + " *********")
                    self.lp.click_logout()
                    time.sleep(4)
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("******** login Unsuccessful for " + self.username + " *********")
                    list_status.append("Fail")
            elif flag == 0:
                if self.exp == "Pass":
                    self.logger.info("******** login successful for " + self.username + " *********")
                    self.lp.click_logout()
                    time.sleep(4)
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("******** login Unsuccessful for " + self.username + " *********")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("***************** Login DDT Test is passed ******************")
            self.driver.close()
            assert True
        else:
            self.logger.info("***************** Login DDT Test is Failed ******************")
            self.driver.close()
            assert False

    logger.info("***************** Completed Test_002_DDT_Login **********************")
