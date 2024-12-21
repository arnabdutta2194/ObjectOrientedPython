import threading
from bs4 import BeautifulSoup
import requests
from lxml import html
import time
import datetime
import random
from queue import Empty


class  YahooFinancePriceScheduler(threading.Thread):
    def __init__(self,input_queue,output_queue,**kwargs):
        self._input_queue = input_queue
        temp_queue= output_queue
        if type(temp_queue) != list:
            temp_queue = [temp_queue]
        self._output_queues = temp_queue
        super(YahooFinancePriceScheduler,self).__init__(**kwargs)
        self.start()

    def run(self):
        while True:
            try:
                val = self._input_queue.get(timeout=10)
            except Empty:
                print("Yahoo scheduler queue is empty, stopping")
            if val == 'DONE':
                for output_queue in self._output_queues:
                    output_queue.put('DONE')
                break
            yahooFinancePriceWorker = YahooFinancePriceWorker(symbol=val)
            price = yahooFinancePriceWorker.get_price()
            for output_queue  in self._output_queues:
                output_values = (val, price, datetime.datetime.now())
                output_queue.put(output_values)
            time.sleep(random.random())

            
class YahooFinancePriceWorker():
    def __init__(self,symbol,**kwargs):
        self._symbol = symbol
        _base_url = 'https://finance.yahoo.com/quote/'
        self._url = f'{_base_url}{self._symbol}'
    
    def get_price(self):
        response = requests.get(self._url)
        if response.status_code != 200:
            print("Could not get data")
            return 
        page_contents  = html.fromstring(response.text)
        raw_price = page_contents.xpath('//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section[1]/div[1]/fin-streamer[1]/span')[0].text
        price = float(raw_price.replace(',',''))
        return price
