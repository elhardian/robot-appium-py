from modules.account.Models import User
# INPUT
unregister_user_jhon = User("Jhone Doe", "08123456789", "jhondoe@elhardian.tech", "hellojhon")

# ELEMENTS 
element_class_chain_registration_button = '**/XCUIElementTypeButton[`label == "Sign Up"`]'
element_class_chain_full_name = '**/XCUIElementTypeTextField[`value == "Full Name"`]'
element_class_chain_phone = '**/XCUIElementTypeTextField[`value == "Phone Number"`]'
element_class_chain_email = '**/XCUIElementTypeTextField[`value == "E-mail Address"`]'
element_class_chain_password = '**/XCUIElementTypeSecureTextField[`value == "Password"`]'