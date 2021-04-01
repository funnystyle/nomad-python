import os
import requests
import validators

def gen_url(url):
  return url.lower() if url.startswith("http") else ("http://" + url).lower()

def is_up(url):
  try:
    response = requests.get(url)
    return response.status_code == requests.codes.ok
  except requests.exceptions.ConnectionError:
    return False

while True: 
  os.system("clear")
  print("Welcome to IsItDown.py!")
  urls = input("Please write a URL or URLs you want to check. (separated by comma)\n").split(",")

  for u in urls:
    stripped_url = u.strip()
    url = gen_url(stripped_url)
    if validators.url(url):
      if is_up(url):
        print(url, "is up!")
      else:
        print(url, "is down!")
    else:
      print(stripped_url, "is not a valid URL")

  while True: 
    restart = input("Do you want to start over? y/n ").lower()
    if restart == "y" or restart == "n":
      break
    else:
      print("That's not a valid answer")

  if restart == "n":
    print("k. bye!")
    break
