*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  arto
    Set Password  salainen1
    Set Password Confirmation  salainen1
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  salasana1
    Set Password Confirmation  salasana1
    Submit Register
    Register Should Fail With Message  Username must be at least 3 characters 

Register With Valid Username And Too Short Password
    Set Username  maija
    Set Password  lyhyt1
    Set Password Confirmation  lyhyt1
    Submit Register
    Register Should Fail With Message  Password must be at least 8 characters 

Register With Valid Username And Invalid Password
    Set Username  pekka
    Set Password  salasanat
    Set Password Confirmation  salasanat
    Submit Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  liisa
    Set Password  salainen1
    Set Password Confirmation  salainen2
    Submit Register
    Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  uusi1234
    Set Password Confirmation  uusi1234
    Submit Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Register
    Click Button  Register

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
