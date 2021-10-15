import requests
from bs4 import BeautifulSoup
from twilio.rest import Client 


cityName = input("Enter the City's Name: ")
url = "https://www.google.com/search?q="+"weather"+cityName

html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')


temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
string = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

data = string.split('\n')
time = data[0]
mausam = data[1]

listOfDiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})


pos = string.find('Wind')
other_data = string[pos:]


account_sid = 'XXXXXXXXXXXXXXXXXXXXX' 
auth_token = 'XXXXXXXXXXXXXXXXXXXXX' 
client = Client(account_sid, auth_token)

message = client.messages \
.create(
body=f"Temerature of {cityName} is {temperature} on {time} and the sky is {mausam}",
from_='+XXXXXXXXXXXXXX',
        to='+XXXXXXXXXXXXXX'
)

