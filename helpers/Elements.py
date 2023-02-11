from Setting import driver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_scrollable_element_by_id(id):
    try:
        element = driver.find_element_by_accessibility_id(id) 
        driver.execute_script('mobile: scroll', {'element': element, 'toVisible': True})
        return element
    except:
        raise Exception(f"element with id *{id}* couldn't be found after scrolling to the entire page")

def get_scrollable_element_by_ios_class_chain(id):
    try:
        element = driver.find_element_by_ios_class_chain(id) 
        driver.execute_script('mobile: scroll', {'element': element, 'toVisible': True})
        return element
    except:
        raise Exception(f"element with id *{id}* couldn't be found after scrolling to the entire page")

def get_scrollable_element_by_ios_class_chain_dir_down(id):
    try:
        element = driver.find_element_by_ios_class_chain(id) 
        driver.execute_script('mobile: scroll', {'direction': 'down', 'element': element, 'toVisible': True})
        return element
    except:
        raise Exception(f"element with id *{id}* couldn't be found after scrolling to the entire page")

def get_scrollable_element_by_accessebility_id_dir_down(id):
    try:
        element = driver.find_element_by_accessibility_id(id) 
        driver.execute_script('mobile: scroll', {'direction': 'down', 'element': element, 'toVisible': True})
        return element
    except:
        raise Exception(f"element with id *{id}* couldn't be found after scrolling to the entire page")

def get_scrollable_element_by_ios_class_chain_dir_left(id):
    try:
        element = driver.find_element_by_ios_class_chain(id) 
        driver.execute_script('mobile: scroll', {'direction': 'left', 'element': element, 'toVisible': True})
        return element
    except:
        raise Exception(f"element with id *{id}* couldn't be found after scrolling to the entire page")

def get_scrollable_element_by_accessebility_id_dir_left(id):
    try:
        element = driver.find_element_by_accessibility_id(id) 
        driver.execute_script('mobile: scroll', {'direction': 'left', 'element': element, 'toVisible': True})
        return element
    except:
        raise Exception(f"element with id *{id}* couldn't be found after scrolling to the entire page")

def get_element_by_id(element_id):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, element_id))
        )
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 60 seconds")

def get_element_by_accessibility_id(element_id):
    try:
        element = WebDriverWait(driver, 60).until(
            driver.find_element_by_accessibility_id(element_id)
        )
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 60 seconds")

def get_element_by_accessibility_id_without_wait(element_id):
    try:
        element = driver.find_element_by_accessibility_id(element_id)
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after scrolling to the entire page")

def get_element_by_accessibility_id_presence_located(element_id):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, element_id))
        )
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 60 seconds")

def get_element_by_accessibility_id_visibility_located(element_id):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, element_id))
        )
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 60 seconds")

def get_element_invisible_by_accessibility_id(element_id):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.invisibility_of_element((MobileBy.ACCESSIBILITY_ID, element_id))
        )
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 60 seconds")

def get_element_by_xpath_clickable(xpath):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((MobileBy, xpath))
        )
        return element
    except:
        raise Exception(f"element with id *{xpath}* couldn't be found after waiting 60 seconds")

def get_element_by_xpath(xpath):
    try:
        element = WebDriverWait(driver, 60).until(
            driver.find_element_by_xpath(xpath)
        )
        return element
    except:
        raise Exception(f"element with id *{xpath}* couldn't be found after waiting 60 seconds")

def get_element_by_match_text(text):
    try:
        element = driver.find_element_by_name(
            f'new UiSelector().textContains("{text}");'
        )
        return element
    except:
        raise Exception(f"element with id *{text}* couldn't be found after scrolling to the entire page")

def get_element_by_text(text):
    try:
        element = WebDriverWait(driver, 60).until(
            driver.find_element_by_name(text)
        )
        return element
    except:
        raise Exception(f"element with id *{text}* couldn't be found after waiting 60 seconds")

def get_element_by_id_ios_class_chain_clickable(element_ios_class_chain):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((MobileBy.IOS_CLASS_CHAIN, element_ios_class_chain))
        )
        return element
    except:
        raise Exception(f"element with id *{element_ios_class_chain}* couldn't be found after waiting 60 seconds")

def get_element_by_id_ios_class_chain(element_id):
    try:
        element = WebDriverWait(driver, 60).until(
            driver.find_element_by_ios_class_chain(element_id)
        )
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 60 seconds")

def get_element_by_id_ios_class_chain_visibility_located(element_id):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((MobileBy.IOS_CLASS_CHAIN, element_id))
        )
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 60 seconds")

def get_element_by_id_ios_class_chain_presence_located(element_id):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((MobileBy.IOS_CLASS_CHAIN, element_id))
        )
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 60 seconds")

def get_element_invisible_by_id_ios_class_chain(element_id):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.invisibility_of_element((MobileBy.IOS_CLASS_CHAIN, element_id))
        )
        return element
    except:
        raise Exception(f"element with id *{element_id}* couldn't be found after waiting 60 seconds")

def get_element_by_id_ios_predicate_clickable(element_predicate_string):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((MobileBy.IOS_PREDICATE, element_predicate_string))
        )
        return element
    except:
        raise Exception(f"element with id *{element_predicate_string}* couldn't be found after waiting 60 seconds")

def get_element_by_id_ios_predicate(element_predicate_string):
    try:
        element = WebDriverWait(driver, 60).until(
            MobileBy.IOS_PREDICATE, element_predicate_string)
        return element
    except:
        raise Exception(f"element with id *{element_predicate_string}* couldn't be found after waiting 60 seconds")

def get_webview_element_by_id(id):
    try:
        element = driver.find_element_by_xpath(f"//*[@data-automation='{id}']")
        return element
    except:
        raise Exception(f"element with id *{id}* couldn't be found after scrolling to the entire page")