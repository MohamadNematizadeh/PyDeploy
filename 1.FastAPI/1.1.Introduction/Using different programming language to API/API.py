import json
import requests

response_fruit = requests.get("https://www.fruityvice.com/api/fruit/peach")
print("api fruit :", json.loads(response_fruit.text))


response_numbers = requests.get("http://numbersapi.com/42")
print("api numbers :",response_numbers.text)

response_Harry_Potte = requests.get("https://hp-api.onrender.com/api/characters")
print("api Harry Potte :",json.loads(response_Harry_Potte.text))

response_Quran = requests.get("https://api.alquran.cloud/v1/surah/114")
print("api Quran :",json.loads(response_Quran.text))

