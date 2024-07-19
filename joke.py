import requests

url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,racist,sexist&type=single"

response = requests.get(url)
# print(response)

recieved_data= response.json()
# print(recieved_data)

for i in recieved_data.keys():
  if i=="error" or i=="category" or i=="type" or i=="flags" or i=="id" or i=="safe" or i=="lang":
    continue
  print("{} : {}".format(i, recieved_data[i]))

# print(response.text)
