*** Settings ***
Documentation     Your documentation related to test-cases on this module

Resource            ../modules/account/Keywords.robot

*** Test Cases ***
Scenario: Fill Registerion Form
    Given From Home Page
    When Go To Registration Page
    Then Fill The Registration Form 