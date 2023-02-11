*** Settings ***
Documentation       Keywords with robot syntax

Library            ./Usecases.py
Variables          ./Constants.py

*** Keywords ***

From Home Page
    go_to_home_page

Go To Registration Page
    click_on_registration_button

Fill The Registration Form 
    fill_registration_user           ${unregister_user_jhon}