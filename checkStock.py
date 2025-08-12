from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

def get_in_stock_tcins():
    url = "https://redsky.target.com/redsky_aggregations/v1/web/product_summary_with_fulfillment_v1"

    params = {
        "key": "9f36aeafbe60771e321a7cc95a78140772ab3e96",
        "tcins": "94681770,94681785,94681780,94681767,94636863",
        "store_id": "184",
        "zip": "91011",
        "state": "CA",
        "latitude": "34.210",
        "longitude": "-118.200",
        "scheduled_delivery_store_id": "3293",
        "paid_membership": "false",
        "base_membership": "false",
        "card_membership": "false",
        "required_store_id": "184",
        "skip_price_promo": "true",
        "visitor_id": "0194DDA645A202019B49A5CF13146A67",
        "channel": "WEB",
        "page": "/s/pokemon+cards"
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    r = requests.get(url, params=params, headers=headers)
    data = r.json()
    in_stock = []
    for product in data.get("data", {}).get("product_summaries", []):
        shipping = product.get("fulfillment", {}).get("scheduled_delivery", [])
        if shipping.get("availability_status") != "UNAVAILABLE":
            item_title = product.get("item").get("product_description").get("title")
            in_stock.append((item_title, product["tcin"]))
    return in_stock

def addFromPage(tcin, email, password):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 7)
    driver.get("https://www.target.com/p/-/A-" + tcin)

    buttonID = "addToCartButtonOrTextIdFor" + tcin
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, buttonID)))
    add_to_cart_button.click()

    go_to_cart_button = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR,
    "a.styles_ndsBaseButton__W8Gl7.styles_md__X_r95.styles_mdGap__9J0yq.styles_fullWidth__3XX6f.styles_ndsButtonSecondary__iSf2I"
    )))
    go_to_cart_button.click()

    time.sleep(1)

    sign_in_button = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR,
    ".styles_ndsBaseButton__W8Gl7.styles_md__X_r95.styles_mdGap__9J0yq.styles_fullWidth__3XX6f.styles_ndsButton__XOOOH.styles_md__Yc3tr.styles_filleddefault__7QnWt"
    )))
    sign_in_button.click()

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    email_input.clear()
    email_input.send_keys(email)

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
    if login_button:
        login_button.click()

    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.clear()
    password_input.send_keys(password)

    login_button = wait.until(EC.visibility_of_element_located((By.ID, "login")))
    login_button.click()

    time.sleep(20)
    # placeOrder_button = wait.until(EC.element_to_be_clickable((
    # By.CSS_SELECTOR,
    # "styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButton__XOOOH styles_md__Yc3tr styles_filleddefault__7QnWt"
    # )))
    # placeOrder_button.click()
    driver.quit()