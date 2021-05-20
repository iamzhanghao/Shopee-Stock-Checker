from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from discord_webhook import DiscordWebhook

product_url = "https://shopee.sg/product/70006977/1704784042"
chrom_driver_path = "/usr/local/bin/chromedriver"
discord_webhook = "https://discordapp.com/api/webhooks/844968739535716423/h6pt3utoJK1DCt8dLh78wiM5EalA_8Rgawn5flVpbR3-Fl1R494mpl0qVtXrlOk4MHpj"

while True:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(
        executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)
    driver.get(product_url)

    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()

    buttons = soup.find_all("button", {"class": "product-variation"})
    buttons_disabled = soup.find_all(
        "button", {"class": "product-variation--disabled"})

    all = []
    for button in buttons:
        all.append(button.contents[0])

    no_stock = []
    for button in buttons_disabled:
        no_stock.append(button.contents[0])

    for item in all:
        if item in no_stock:
            print(item + ' No Stock')
        else:
            print(item + ' In Stock')
            webhook = DiscordWebhook(
                url=discord_webhook, content=item+' in stock!!!!!')
            response = webhook.execute()

    if len(all) == len(no_stock) and len(all) != 0 and len(no_stock) != 0:
        webhook = DiscordWebhook(
            url=discord_webhook, content="Everything no stock")
        response = webhook.execute()

    time.sleep(900)
