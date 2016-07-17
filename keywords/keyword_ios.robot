
*** Keywords ***
launch app
    ${driver}=  setup appium  ${APP}  iOS
    should not be empty  ${driver}