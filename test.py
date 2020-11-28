import bs4
import requests
import schedule
import time
import datetime
from win10toast import ToastNotifier
import csv
import sys
from function import send_email


week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today = datetime.date.today()
now = datetime.datetime.now().time()


def get_stock_price():
    try:
        links = 'https://histock.tw/stock/%s' % stock_no
        response = requests.get(links)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        tittle = soup.find('h3').get_text().strip()
        li = soup.find('span', id="Price1_lbTPrice").span.get_text()
        time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        with open('docs\get_price.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([tittle, li, time_now])

        notify(li, tittle)
        print(set_price, li, tittle)

    except Exception as e:
        print('It is not working...')
        print(e)
        sys.exit()


def notify(current_price, stock_title):

    if set_price == current_price:
        msg_text = stock_title + \
            'stock value is  ' + current_price
        send_email(msg_text)
        toaster = ToastNotifier()
        toaster.show_toast("Stock value notification",
                           msg_text,
                           duration=10)
    return


if today.strftime("%A") in week_day and (now > datetime.time(9, 0) and now < datetime.time(13, 30)):
    stock_no = input('Please insert stock no：')
    set_price = '%.2f' % float(input('Please set notification price:'))
    schedule.every(10).seconds.do(get_stock_price)
else:
    print('it is non-business hours now')


while True:
    schedule.run_pending()
    time.sleep(1)
