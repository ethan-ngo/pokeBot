# check_and_add.py
from checkStock import get_in_stock_tcins, addFromPage
from dotenv import load_dotenv
import os
def main():
    tcins = get_in_stock_tcins()
    if not tcins:
        print("No preorders")
        return
    load_dotenv()
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    for item_title, tcin in tcins:
        print(f"In stock: {item_title}, adding to cart...")
        addFromPage(tcin, email, password)

if __name__ == "__main__":
    main()