from Setting import driver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,sys

current_directory = os.getcwd()
sys.path.append(current_directory)

class Element():
    element_timeout = os.environ.get('ELEMENT_TIMEOUT', 30)

    def get_element_by_class_chain(self, element_ios_class_chain):
        try:
            element = WebDriverWait(driver, self.element_timeout).until(
                EC.element_to_be_clickable((MobileBy.IOS_CLASS_CHAIN, element_ios_class_chain))
            )
            return element
        except:
            raise Exception(f"element with class chain *{element_ios_class_chain}* couldn't be found after waiting {self.element_timeout} seconds")
