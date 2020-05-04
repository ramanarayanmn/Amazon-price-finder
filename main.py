import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = 'https://www.amazon.in/realme-Sparkling-Blue-64GB-Storage/dp/B07Y8K4D7X/ref=sr_1_6?dchild=1&keywords=realme&qid=1588570700&sr=8-6' # realme moble amazon link

headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"} # google:  my user agent


def check_price():
	page = requests.get(URL,headers=headers)
	soup = BeautifulSoup(page.content,'html.parser')

	title = soup.find(id = 'productTitle').get_text()
	price = soup.find(id='priceblock_ourprice').get_text()
	converted_price = (price[2:8])
	converted_price=converted_price.replace(',','')
	converted_price = float(converted_price)

	if converted_price<13000.0:
		send_mail()


def send_mail():
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('suprith.narayan@gmail.com','# put App password') # put App password

	subject = 'Price Fell down!'

	# change the body according to URL
	body = 'check amazon link https://www.amazon.in/realme-Sparkling-Blue-64GB-Storage/dp/B07Y8K4D7X/ref=sr_1_6?dchild=1&keywords=realme&qid=1588570700&sr=8-6'

	msg = f"subject: {subject}\n\n{body}"
	server.sendmail('suprith.narayan@gmail.com','ramanarayan@protonmail.com',msg)
	print("Email has been sent!")

	server.quit()


while True:
	check_price()
	time.sleep(60)

