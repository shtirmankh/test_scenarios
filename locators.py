from selenium.webdriver.common.by import By

class MainPageLocators(object):

    SIGNUP_BUTTON = (By.CSS_SELECTOR, ".btn.btn-construct.btn-sign-up-now")
    CHECKBOX = (By.NAME, "selling_outside_app_store")
    SOLUTIONFORM = (By.XPATH, ".//*[@id='form-signup']/input[5]")
    FEATURES_BUTTON = (By.CSS_SELECTOR, ".container>nav>a")
    ELEM_PIC = (By.CSS_SELECTOR, ".container>nav>a")
    ELEM_BLOCK = (By.CSS_SELECTOR, ".visual-slider-img.on>img")


class UrlLinks(object):
    signUpPage = "http://devmate.com/signup"
    startPage = "http://devmate.com"
    framePage = "http://devmate.com/features/frameworks"
    link = "http://devmate.com/features/app-management"