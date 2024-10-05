# currency convertor 
import os
from dotenv import load_dotenv
import requests 
import json

load_dotenv()

print("\n _______WELCOME TO CURRENCY CONVERTOR_______ \n")
print("Note: Please keep the currency codes handy \n ")

convert_from = input("enter the currency (code only) to convert from : ").upper().strip()
convert_to = input ("enter the currency (code only) you wish to convert to: ").upper().strip()
amount = float(input("enter the amount of money: "))


BASE_URL = "https://api.currencyapi.com/v3/latest/"

API_KEY = os.getenv("API_KEY")

endpoint = BASE_URL + "?apikey=" + API_KEY      #paste your apikey inplace of API_KEY


response = requests.get(endpoint)
#print(response.status_code)                resposnse code is 200: if data is successfully retrieved from server 
data1 = response.json()
#format_json = json.dumps(data1, indent=3)
#print(data1)
#print(data)

rate1 = round(1 / data1['data'][convert_from]["value"], 2)
rate2 = round(data1['data'][convert_to]['value'], 2)
rate3 = round(rate1 * rate2, 2)

#print(f'{convert_from} to USD rate is: {rate1}')
#print(f'USD to {convert_to} rate is: {rate2} ')
print(f'{convert_from} to {convert_to} rate is: {rate3}')

#converted_amount = round((amount/rate1), 2)
#print(converted_amount)
final_amount = round(amount * rate3, 2)
print(f'{amount} {convert_from} to {convert_to} is: {final_amount}')