from selenium.webdriver.common.by import By

class MainPageLocators(object):

    SIGNUP_BUTTON = (By.CSS_SELECTOR, ".btn.btn-construct.btn-sign-up-now")
    CHECKBOX = (By.NAME, "selling_outside_app_store")


class UrlLinks(object):
    signUpPage = "http://devmate.com/signup"
    startPage = "http://devmate.com"