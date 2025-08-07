from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

def login_to_target_via_homepage(driver, email, password):
    wait = WebDriverWait(driver, 5)
    driver.get("https://www.target.com/")

    # Step 1: Click Account button (top-right corner)
    account_button = wait.until(EC.element_to_be_clickable((By.ID, "account-sign-in")))
    account_button.click()

    # Step 2: Click "Sign in / Create Account"
    sign_in_btn = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR,
    ".styles_ndsBaseButton__W8Gl7.styles_md__X_r95.styles_mdGap__9J0yq.styles_fullWidth__3XX6f.styles_ndsButton__XOOOH.styles_md__Yc3tr.styles_filleddefault__7QnWt.h-margin-t-x2.h-margin-b-default"
    )))
    sign_in_btn.click()

    # Step 3: Click "Keep me signed in" checkbox
    keep_signed_in_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "keepMeSignedIn")))
    keep_signed_in_checkbox.click()

    # Step 4: Enter email
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    email_input.clear()
    email_input.send_keys(email)

    # Step 5: Click Continue
    continue_button = driver.find_element(By.ID, "login")
    continue_button.click()

    # Step 6: Click on password login
    password_button = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_button.click()

    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.clear()
    password_input.send_keys(password)

    # Step 7: Click "Sign in with password"
    final_sign_in_button = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR,
    ".styles_ndsBaseButton__W8Gl7.styles_lg___H2IL.styles_lgGap__bPB7P.styles_fullWidth__3XX6f.styles_ndsButton__XOOOH.styles_lg__T5sAi.styles_filleddefault__7QnWt.h-margin-v-default"
    )))
    final_sign_in_button.click()

def addToCart(tcin):
    driver.get("https://www.target.com/")
    search_input = wait.until(EC.visibility_of_element_located((By.ID, "search")))
    search_input.clear()
    search_input.send_keys(tcin)

    search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "styles_searchButton__Mkp1S")))
    search_button.click()

    buttonID = "addToCartButtonOrTextIdFor" + tcin
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, buttonID)))
    add_to_cart_button.click()

    modal_add_to_cart_button = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR,
    ".styles_ndsBaseButton__W8Gl7.styles_md__X_r95.styles_mdGap__9J0yq.styles_fullWidth__3XX6f.styles_ndsButtonPrimary__tqtKH"
    )))
    modal_add_to_cart_button.click()

    go_to_cart_button = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR,
    "a.styles_ndsBaseButton__W8Gl7.styles_md__X_r95.styles_mdGap__9J0yq.styles_fullWidth__3XX6f.styles_ndsButtonSecondary__iSf2I"
    )))
    go_to_cart_button.click()
    
    time.sleep(100)

def continueShop():
    continueShop = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR,
    ".styles_ndsBaseButton__W8Gl7.styles_md__X_r95.styles_mdGap__9J0yq.styles_fullWidth__3XX6f.styles_ndsButtonPrimary__tqtKH"
    )))
    continueShop.click()