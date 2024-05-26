from selenium.webdriver.common.by import By


class LoginPage:
    username_textbox_xpath = "//input[@name='username']"
    password_textbox_xpath = "//input[@name='password']"
    login_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"
    logout_dd_xpath = "//*[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    logout_link_xpath = "//a[text()='Logout']"
    login_profile_xpath = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p"

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_dd_xpath).click()
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()

    def do_login(self, username, password):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
