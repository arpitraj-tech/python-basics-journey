import json
import os
import time
#by  response u get through your own apikey 
with open("wheather_response.json","r") as f :
    data=json.load(f)

def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
    
    print("Welcome to wheather forecast".center(123))
    print("\n")
    print("what do you want to know :\n1.your location\n2.current temperature\n3.wheather condition\n4.Timing of sun and moon rise and set\n5.Air quality and cloud cover\n6.Exit")
    print("\n")

while True:
    clear()
    ask=input("from above options please select appropriate response only : ")
    while ask not in "123456":
        ask=input("from above options please select appropriate response only : ")
    
    if ask=="6":
        print("\nThank you for using our Wheather forcast")
        exit()
    if ask=="1":
        city=data["location"]["name"]
        state=data["location"]["region"]
        country=data["location"]["country"]
        lat=data["location"]["lat"]
        lon=data["location"]["lon"]
        print("\n")
        print(f"\nyour current location is\n\ncity-{city}\nstate-{state}\ncountry-{country}\nlatitude-{lat}\nlongitude-{lon}")
        time.sleep(10)
    
    if ask=="2":
        temp=data["current"]["temperature"]
        print("\n")
        print(f"The current temperature in your location is : {temp} degree")
        time.sleep(4)
    
    if ask=="3":
        con=data["current"]["weather_descriptions"][0]
        print("\n")
        print(f"the current weather condions is likely {con}")
        time.sleep(4)
    
    if ask=="4":
        sr=data["current"]["astro"]["sunrise"]
        st=data["current"]["astro"]["sunset"]
        mr=data["current"]["astro"]["moonrise"]
        mt=data["current"]["astro"]["moonset"]
        print("\n")
        print(f"Timing of sunrise is : {sr}\nTiming of sunset is : {st}\nTiming of moonrise is : {mr}\nTiming of moonset is : {mt}")
        time.sleep(10)

    if ask=="5":
        air=data["current"]["air_quality"]
        cl=data["current"]["cloudcover"]
        print("\n")
        print(f"The air quality is as follows :\n{air}\nand clout coverage is {cl}%")
        time.sleep(10)
    

