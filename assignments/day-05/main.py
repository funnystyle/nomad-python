import os
import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"
    
def scrapy_data(url):
  result = requests.get(url)
  trs = BeautifulSoup(result.text, "html.parser").find_all("tr")[1:]
  return make_list(trs)

def make_list(trs):
  data = []
  for tr in trs:
    append_data(data, tr)
  return data

def extract_data(tr):
  tds = tr.find_all("td")
  return { 
    "country": tds[0].string.capitalize(),
    "currency": tds[2].string 
  }
  
def append_data(data, tr):
  d = extract_data(tr)
  if (d['currency'] is not None):
    data.append(d)
  return data

def print_countries(data):
  for i, d in enumerate(data):
      print(f"# {i} {d['country']}")

def input_number(max):
  while True:
    try:
      number = int(input("#: "))
      if (is_valid(number, max)):
        return number
      else:
        print("Choose a number from the list.")
    except:
      print("That wasn't a number.")

def is_valid(number, max):
  return number >= 0 and number < max

def print_result(data, number):
  print(f"You chose {data[number]['country']}")
  print(f"The currency code is {data[number]['currency']}")

def main():
  os.system("clear")
  print("Hello! Please choose select a country by number:")
  data = scrapy_data(url)
  print_countries(data)
  number = input_number(len(data))
  print_result(data, number)

main()