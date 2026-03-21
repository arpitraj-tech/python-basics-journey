import requests
import json 


def save_data(data_to_save):
        with open("wheather_response.json","w") as file :
            json.dump(data_to_save,file,indent=4) 

url="https://api.weatherstack.com/current" 
params={
    "access_key":"YOUR_OWN_API_KEY BY LOGGING TO WEATHERSTACK.COM IN DASBOARD SECTION",
    "type":"city",#just a sample 
    "query":"Ranchi,India"#use your own city and country
}

response=requests.get(url,params=params)
data=response.json()

save_data(data)

    