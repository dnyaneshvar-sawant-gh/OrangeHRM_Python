import configparser
import os

config = configparser.RawConfigParser()
current_dir = os.path.dirname(os.path.abspath(__file__))
config_folder = os.path.join(current_dir, "..", "Configurations")
config_path = os.path.join(config_folder, "config.ini")
config.read(config_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get("common info", "url")
        return url

    @staticmethod
    def get_username():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def get_firstname():
        firstname = config.get("create employee", "firstname")
        return firstname

    @staticmethod
    def get_new_password():
        password = config.get("create employee", "password")
        return password

    @staticmethod
    def get_employee_id():
        employee_id = config.get("create employee", "employeeId")
        return employee_id

    @staticmethod
    def get_lastname():
        lastname = config.get("create employee", "lastname")
        return lastname

    @staticmethod
    def get_new_username():
        username = config.get("create employee", "username")
        return username
