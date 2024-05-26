import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddEmp:
    pim_link_xpath = "//a[@href='/web/index.php/pim/viewPimModule']"
    addEmp_link_xpath = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a"
    firstName_input_xpath = "//input[@name='firstName']"
    middleName_input_xpath = "//input[@name='middleName']"
    lastName_input_xpath = "//input[@name='lastName']"
    # xpath needs to change
    empId_input_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input"
    radio_button_xpath = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    username_input_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input"
    password_input_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input"
    confirm_password_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input"
    save_button_xpath = "//button[@type='submit' and @class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    empName_text_xpath = "//div[@class='orangehrm-edit-employee-name']"
    success_message_id = "oxd-toaster_1"

    def __init__(self, driver):
        self.driver = driver

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            expected_conditions.visibility_of_element_located((By.ID, self.success_message_id))
        )
        text = self.driver.find_element(By.ID, self.success_message_id).text
        return text

    def add_emp_without_login_details(self, first_name, last_name):
        wait = WebDriverWait(self.driver, 10)
        pim = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.pim_link_xpath))
        )
        pim.click()
        add_emp = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.addEmp_link_xpath))
        )
        add_emp.click()
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.firstName_input_xpath))
        )
        self.driver.find_element(By.XPATH, self.firstName_input_xpath).send_keys(first_name)
        self.driver.find_element(By.XPATH, self.lastName_input_xpath).send_keys(last_name)
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def create_new_employee(self, firstname, lastname, username, password):
        wait = WebDriverWait(self.driver, 10)
        pim = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.pim_link_xpath))
        )
        pim.click()
        add_emp = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.addEmp_link_xpath))
        )
        add_emp.click()
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.firstName_input_xpath))
        )
        self.driver.find_element(By.XPATH, self.firstName_input_xpath).send_keys(firstname)
        self.driver.find_element(By.XPATH, self.lastName_input_xpath).send_keys(lastname)
        self.driver.find_element(By.XPATH, self.radio_button_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.username_input_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_input_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def pim_click(self):
        wait = WebDriverWait(self.driver, 10)
        pim = wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.pim_link_xpath))
        )
        pim.click()
