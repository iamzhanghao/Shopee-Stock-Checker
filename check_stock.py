from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from discord_webhook import DiscordWebhook

product_url = "https://shopee.sg/product/442800909/12801910348/"
# product_url = "https://shopee.sg/Seagate-Backup-Plus-Hub-Desktop-4TB-6TB-8TB-10TB-STEL4000300-External-HDD-i.70006977.1584597848"
chrom_driver_path = "/usr/local/bin/chromedriver"
discord_webhook = "https://discordapp.com/api/webhooks/844968739535716423/h6pt3utoJK1DCt8dLh78wiM5EalA_8Rgawn5flVpbR3-Fl1R494mpl0qVtXrlOk4MHpj"

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(
    executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)

while True:

    driver.get(product_url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    buttons = soup.find_all("button", {"class": "product-variation"})
    buttons_disabled = soup.find_all(
        "button", {"class": "product-variation--disabled"})

    all = []
    for button in buttons:
        all.append(button.contents[0])

    no_stock = []
    for button in buttons_disabled:
        no_stock.append(button.contents[0])

    # for item in all:
    #     if item in no_stock:
    #         print(item + ' No Stock')
    #     else:
    #         print(item + ' In Stock')
    #         webhook = DiscordWebhook(
    #             url=discord_webhook, content='@everyone ' + item + ' in stock!!!!! ')
    #         response = webhook.execute()
    #         webhook = DiscordWebhook(
    #             url=discord_webhook, content='Get it now! ' + product_url)
    #         response = webhook.execute()

    if (not 'Sierra Blue' in no_stock) and (not '256GB' in no_stock):
        print('Sierra Blue 256G in stock!')
        webhook = DiscordWebhook(
            url=discord_webhook, content="@everyone Sierra Blue 256G in stock! GET IT NOW!")
        response = webhook.execute()
        webhook = DiscordWebhook(
            url=discord_webhook, content="@everyone Sierra Blue 256G in stock! GET IT NOW!")
        response = webhook.execute()
    else:
        print('Sierra Blue 256G no stock')
        webhook = DiscordWebhook(
            url=discord_webhook, content="Sierra Blue 256G no stock")
        response = webhook.execute()

    # if len(all) == len(no_stock) and len(all) != 0 and len(no_stock) != 0:
    #     webhook = DiscordWebhook(
    #         url=discord_webhook, content="Everything no stock")
    #     response = webhook.execute()

    time.sleep(600)
