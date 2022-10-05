# ///////////////////////////////////////////////////////////////
#
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import lxml.html
import lxml.etree
import requests
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class Railway(QRunnable):
    def __init__(self, current_url='https://pass.rw.by/ru/route/?from=Орша&to=Минск&date=2021-10-14'):
        super().__init__()
        self.url = current_url

    def parse(self):
        # page - full code
        # page = requests.get(self.url)
        # page = open('source.txt')  # DEBUG
        tree = lxml.html.parse('source.txt').getroot()  # DEBUG
        # print(lxml.html.tostring(tree))
        # make a lxml tree
        # tree = lxml.html.fromstring(page.content)
        # tree = lxml.html.fromstring(page)
        # search for trains by ccs
        transport_res = tree.cssselect('div.sch-table__row-wrap')
        result = []
        ans = ''
        # for each train
        for number, data in enumerate(transport_res, start=1):
            # strip - without spaces
            train_name = data.cssselect('span.train-route')[0].text_content().strip()
            train_departure = data.cssselect('div.train-from-time')[0].text_content().strip()
            train_arrive = data.cssselect('div.train-to-time')[0].text_content().strip()
            train_duration = data.cssselect('div.train-duration-time')[0].text_content().strip()
            train_tickets = data.cssselect('div.sch-table__tickets')[0].text_content().strip()

            # print for debug
            ans += f'{number}: {train_name} {train_departure} {train_arrive} {train_duration}\n'
            ans += 'Билеты:\n'

            # collecting info about only tickets for qt
            tickets = ''
            if train_tickets != '\n':
                # items is []
                ticket_items = data.cssselect('div.sch-table__t-item')
                for item in ticket_items:
                    # each item includes name, free, [] of prices
                    ticket_type = item.cssselect('div.sch-table__t-name')
                    ticket_free = item.cssselect('a.sch-table__t-quant')
                    ticket_prices = item.cssselect('span.ticket-cost')

                    if ticket_type[0].text is not None and ticket_type[0].text != ' ':
                        ans += f'Тип: {ticket_type[0].text}'
                        tickets += f'Тип: {ticket_type[0].text}'
                    else:
                        ans += f'Tип: --------'
                        tickets += f'Tип: --------'

                    if ticket_free[0].text_content() is not None:
                        ans += f' --- Свободно: {ticket_free[0].text_content()}'
                        tickets += f' --- Свободно: {ticket_free[0].text_content()}'
                    else:
                        ans += f' --- Свободно: ---'
                        tickets += f' --- Свободно: ---'

                    if ticket_prices is not None:
                        # if it is not one price
                        for num, price in enumerate(ticket_prices):
                            if num < 1:
                                ans += f' --- Цена: {price.text}\n'
                                tickets += f' --- Цена: {price.text}\n'
                            else:
                                ans += f'-------------------------------------- Цена: {price.text}\n'
                                tickets += f'-------------------------------------- Цена: {price.text}\n'
                    else:
                        ans += f' --- Цена: ---\n'
                        tickets += f' --- Цена: ---\n'

            train_tickets_bad = data.cssselect('div.sch-table__no-info')
            if train_tickets_bad:
                train_tickets_bad = data.cssselect('div.sch-table__no-info')
                ans += f'{train_tickets_bad[0].text.strip()}\n'
                tickets = f'{train_tickets_bad[0].text.strip()}\n'
            ans += '\n'

            tickets = tickets[:-1]  # убрать лишний перевод строки
            str_count = tickets.count("\n")  # количество строк

            # полная информация о поезде
            # train_info = [number, train_name, train_departure, train_arrive, train_duration, str_count, tickets]
            train_info = {'number': number, 'train_name': train_name, 'train_departure': train_departure,
                          'train_arrive': train_arrive, 'train_duration': train_duration,
                          'str_count': str_count, 'tickets': tickets}
            result.append(train_info)

        print(ans)
        # print(transport_res)
        # print(page.text)
        # f = open('source.txt', 'w', encoding='utf-8')
        # f.write(page.text)
        # f.close()
        return result


class MinskTransport(QRunnable):
    def __init__(self):
        super().__init__()
        self.url = 'https://www.minsktrans.by/lookout_yard/Home/Index/minsk#/routes/bus'

    # Parse function: Scrape the webpage and store it
    def parse(self):
        arr = []
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        # Output filename
        # f = open('source.txt', 'w', encoding='utf-8')
        driver.implicitly_wait(3)
        # f.write(driver.page_source)
        # f.close()
        # print(driver.page_source)
        # Selector for all the names from the link with class 'ng-binding'
        names = driver.find_elements_by_css_selector("h3.ng-binding")
        for name in names:
            title = name.text
            # print(title)
            arr.append(title)
        driver.quit()
        print(arr)
        return arr


if __name__ == '__main__':
    # url = "https://pass.rw.by/ru/route/?from=%D0%91%D1%80%D0%B5%D1%81%D1%82&from_exp=&from_esr=&to=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&to_exp=&to_esr=&front_date=14+%D0%BE%D0%BA%D1%82.+2021&date=2021-10-14"
    url = "https://pass.rw.by/ru/route/?from=Орша&to=Минск&date=2021-10-14"
    obj = Railway(url)
    obj.parse()
