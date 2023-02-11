import os, sys
current_directory = os.getcwd()
sys.path.append(current_directory)

from helpers.Elements import Element
from helpers.Application import Application
from modules.account.Constants import *

class Usecases:
    element_helper = Element()
    app_helper = Application()

    def go_to_home_page(self):
        self.app_helper.reopen_application()
    
    def click_on_registration_button(self):
        input_search_element = self.element_helper.get_element_by_class_chain(element_class_chain_registration_button)
        input_search_element.click()

    def fill_registration_user(self, user:User):
        element_fullname = self.element_helper.get_element_by_class_chain(element_class_chain_full_name)
        element_fullname.send_keys(user.fullname)

        element_phone = self.element_helper.get_element_by_class_chain(element_class_chain_phone)
        element_phone.send_keys(user.phone)

        element_email = self.element_helper.get_element_by_class_chain(element_class_chain_email)
        element_email.send_keys(user.email)

        element_password = self.element_helper.get_element_by_class_chain(element_class_chain_password)
        element_password.send_keys(user.password)

