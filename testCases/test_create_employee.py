import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects import AddEmployee
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

from pageObjects import SearchEmployee, DeleteEmployee


class Test_006_CreateEmployee:
    url = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    firstname = ReadConfig.get_firstname()
    lastname = ReadConfig.get_lastname()
    new_username = ReadConfig.get_new_username()
    new_password = ReadConfig.get_new_password()

    logger = LogGen.loggen()

    def test_create_new_emp(self, setup):
        try:
            self.logger.info("***************** Test_006_CreateEmployee **************")
            self.logger.info("***************** Verifying Create Employee Test **************")
            self.driver = setup
            self.lp = LoginPage(self.driver)
            self.driver.get(self.url)
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.lp.username_textbox_xpath))
            )
            self.lp.do_login(self.username, self.password)
            self.ae = AddEmployee.AddEmp(self.driver)
            self.ae.create_new_employee(self.firstname, self.lastname, self.new_username, self.new_password)
            actual_message = self.ae.get_success_message()

            if "Successfully Saved" in actual_message:
                self.logger.info("***************** Create Employee Test Passed **************")
                assert True
            else:
                self.logger.info("***************** Create Employee Test Failed **************")
                assert False
        except Exception as e:
            print("Error is : ", e)
        finally:
            wait = WebDriverWait(self.driver, 10)
            se = SearchEmployee.SearchEmp(self.driver)
            wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, se.emp_list_xpath))
            )
            se.search_emp_by_name(self.firstname + " " + self.lastname)
            self.de = DeleteEmployee.DeleteEmp(self.driver)
            wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.de.delete_button_xpath))
            )
            self.de.delete_result()
            self.logger.info("***************** New Employee is Deleted **************")

    def test_login_created_employee(self, setup):
        try:
            self.logger.info("***************** Test_006_CreateEmployee **************")
            self.logger.info("***************** Verifying Create Employee Test **************")
            self.driver = setup
            self.lp = LoginPage(self.driver)
            self.driver.get(self.url)
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.lp.username_textbox_xpath))
            )
            self.lp.do_login(self.username, self.password)
            self.ae = AddEmployee.AddEmp(self.driver)
            self.ae.create_new_employee(self.firstname, self.lastname, self.new_username, self.new_password)
            actual_message = self.ae.get_success_message()
            self.lp = LoginPage(self.driver)
            if "Successfully Saved" in actual_message:
                self.lp.click_logout()

            wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.lp.username_textbox_xpath))
            )
            self.lp.do_login(self.new_username, self.new_password)
            time.sleep(3)
            profile_name = self.driver.find_element(By.XPATH, self.lp.login_profile_xpath).text
            if profile_name == "Naruto uzu":
                self.lp.click_logout()
                self.logger.info("***************** Login for New Employee is successful **************")
                assert True
            else:
                self.logger.info("***************** Login for New Employee is Unsuccessful **************")
                assert False
        except Exception as e:
            print("Error is : ", e)

        finally:
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.lp.username_textbox_xpath))
            )
            self.lp.do_login(self.username, self.password)
            ad = AddEmployee.AddEmp(self.driver)
            ad.pim_click()
            se = SearchEmployee.SearchEmp(self.driver)
            wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, se.emp_list_xpath))
            )
            se.search_emp_by_name(self.firstname + " " + self.lastname)
            time.sleep(2)
            self.de = DeleteEmployee.DeleteEmp(self.driver)
            self.de.delete_result()
            self.logger.info("***************** New Employee is Deleted **************")
