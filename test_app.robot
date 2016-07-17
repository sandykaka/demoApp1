*** Settings ***
Documentation    Suite description for ios app
Resource         settings_ios.robot
Suite Setup      start appium
Suite Teardown   stop appium

*** Test Cases ***
Launch test app
    [Tags]    ios
    sleep  5
    launch app

