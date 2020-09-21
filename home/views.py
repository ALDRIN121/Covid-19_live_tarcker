from django.shortcuts import render
from django.http import HttpResponse
import requests
import bs4
import plyer
import time
import datetime
import threading
# Create your views here.
def get_html_data(url):
    data = requests.get(url)
    return data
def home(request):
    url = "https://www.worldometers.info/coronavirus/country/india/"
    html_data = requests.get(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    products = []
    for a in bs.findAll('div',attrs={'class':'maincounter-number'}):
        name = a.find('span').text
        products.append(name)
    return render(request,'index.html',{'Active':products[0],'Death':products[1],'Recovered':products[2]})

