*** Settings ***
Documentation    This is some basic info about the whole suite
Library          SeleniumLibrary

*** Variables ***

*** Test Cases ***
Should be able to add new customer
    [Documentation]         This is some basic info about the test
    [Tags]                  1006  Smoke   Contacts
    #Intialize Selenium
    set selenium speed      .2s
    set selenium timeout    10s

    #open the browser
    log                     Startting the test case!
    open browser            https://www.irctc.co.in/nget/train-search    chrome

    # resize browser windows for recording
    set window position     x=-5    y=5
    set window size         width=1280  height=720

    click link              xpath=/html/body/app-root/app-home/div[1]/app-header/div[1]/div[2]/a
    click button            xpath=//*[@id="slide-menu"]/p-sidebar/div/nav/div/label/button
    page should contain     LOGIN
    input text              id="7021445"     Amirthe
    input password          xpath=//*[@id="8195910"]    Genpact@123
    sleep                   3s
    close browser

*** Keywords ***
