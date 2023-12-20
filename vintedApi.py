import json
import os
import time
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


class Browser:
    def __init__(self, vpn_path=None):
        self.last_used_time = time.time()  # Initialize last used time
        if vpn_path:
            self.options = Options()
            self.options.add_extension(vpn_path)
            self.browser = webdriver.Chrome(options=self.options)

    def getAuth(self):
        self.browser.get('https://vinted.nl/')

    async def wait_for_browser(self):
        elapsed_time = time.time() - self.last_used_time
        if elapsed_time < 4:
            remaining_time = 4 - elapsed_time
            await asyncio.sleep(remaining_time)

    async def get(self, url):
        await self.wait_for_browser()
        self.last_used_time = time.time()  # Update last used time
        self.browser.get(url)
        try:
            return json.loads(self.browser.find_element(By.TAG_NAME, 'pre').text)
        except NoSuchElementException:
            print("couldn't get pre element")
            input()

class VintedApi():
    def __init__(self):
        self.browsers = []
        self.vpn_files = [f for f in os.listdir('./vpns') if f.endswith('.crx')]
        self.currentBrowser = 0
        self.lastIds = []
        self.searchUrl = 'https://www.vinted.nl/api/v2/catalog/items?page=1&per_page=10&search_text=&catalog_ids=&price_to=30&currency=EUR&color_ids=&brand_ids=362&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first'

    def getAuth(self):
        for browser in self.browsers:
            browser.getAuth()


    async def add(self, vpn_index=None):
        vpn_path = None

        if vpn_index is not None:
            vpn_path = './vpns/' + self.vpn_files[vpn_index % len(self.vpn_files)]

        browser = Browser(vpn_path=vpn_path)
        self.browsers.append(browser)

    def delete_search_browser(self, index):
        del self.browsers[index]

    async def search(self):
        if self.browsers:
            new_ids = await self.search_for_new_items()
            result = []
            for item_id in new_ids:
                result.append(await self.item_search(item_id))
            return result
        else:
            return []

    async def item_search(self, item_id):
        if self.currentBrowser == len(self.browsers) - 1:
            self.currentBrowser = 0
        else:
            self.currentBrowser += 1

        data = await self.browsers[self.currentBrowser].get('https://www.vinted.nl/api/v2/items/' + str(item_id))

        try:
            data = data['item']
        except KeyError :
            print(data)
            input()


        shortdata = {
            "id": data['id'],
            "title": data['title'],
            "description": data['description'],
            "url": data['url'],
            "price_numeric": data['price_numeric'],
            "total_item_price": data['total_item_price'],
            "currency": data['currency'],
            "size": data['size'],
            "country_title": data['user']['country_title'],
            "brand": data['brand'],
            "feedback_reputation": data['user']['feedback_reputation'],
            "feedback_count": data['user']['feedback_count'],
            "photos": [photo['full_size_url'] for photo in data['photos']]
        }
        return shortdata

    async def search_for_new_items(self):
        if self.currentBrowser == len(self.browsers) - 1:
            self.currentBrowser = 0
        else:
            self.currentBrowser += 1

        data = await self.browsers[self.currentBrowser].get(self.searchUrl)
        try:
            data = data['items']
        except KeyError :
            print(data)
            input()
        except TypeError:
            print(type(data))
            input()


        if self.lastIds:
            new_items_ids = []
            new_last_ids = [item['id'] for item in data[:5]]

            for item in data:
                if item['id'] in self.lastIds:
                    self.lastIds = new_last_ids
                    return new_items_ids
                else:
                    new_items_ids.append(item['id'])
        else:
            self.lastIds = [item['id'] for item in data[:5]]
            return []
