#!/usr/bin/env python
# coding: utf-8

import json
import requests
from datetime import date
import datetime    
import time
import os
from playsound import playsound

def get_slot_details():
    center_access = data.get('centers')
    for center_data in center_access:
        session_access = center_data['sessions']
        for session_data in session_access:
            #print (center_data['name'], center_data['address'], session_data['date'], session_data['available_capacity_dose2'], session_data['available_capacity_dose1'], session_data['min_age_limit'] )
            if (session_data['min_age_limit'] == age):
                if (dose == 1):
                    if (session_data['available_capacity_dose1'] > 0):
                        print ("Name: ", center_data['name'])
                        print ("Address: ", center_data['address'])
                        print ("Date: ", session_data['date'])
                        print ("First Dose Availability: ", session_data['available_capacity_dose1'])
                        print ("Minimum Age Limit: ", session_data['min_age_limit'])
                        print ("\n")
                        return(1)
                elif (dose == 2):
                    if (session_data['available_capacity_dose2'] > 0):
                        print ("Name: ", center_data['name'])
                        print ("Address: ", center_data['address'])
                        print ("Date: ", session_data['date'])
                        print ("Second Dose Availability: ", session_data['available_capacity_dose2'])
                        print ("Minimum Age Limit: ", session_data['min_age_limit'])
                        print ("\n")
                        return(1)
                else:
                    continue

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=363&"
#srchfld = {'date' : '31-05-2021'}

srchfld = {}
p1 = 'date'

print ("Select an age criteria: ")
print ("1. Age 18 and above\n2. Age 45 and above")
ageChoice = input ("Enter your choice: ")

if ageChoice == '1':
    age = 18
elif ageChoice == '2':
    age = 45
else:
    print ("Wrong Choice. Using default age of 18. ")
    age = 18
    
time.sleep(1)

print ("Select dose criteria: ")
print ("1. First Dose\n2. Second dose")
doseChoice = input ("Enter your choice: ")

if doseChoice == '1':
    dose = 1
elif doseChoice == '2':
    dose = 2
else:
    print ("Wrong Choice. Using default as first dose. ")
    dose = 1
    
print ("Searching...")
time.sleep(1)


while True:
        i = 1
        for i in range(0, 15):
            p2 = (date.today() + datetime.timedelta(days=i))  
            d = p2.strftime("%d-%m-%Y")
            
            time.sleep(1)
            srchfld[p1] = d 
            r = requests.get(url = URL, params = srchfld)
            data = r.json()  
           
            a = 0
            a = get_slot_details()
            if (a == 1):
                playsound('aircraftalarm.wav')
            else:
                print ("No open slots found for", d)
    
        print ("Last run at: ", datetime.datetime.now())
        print ("Sleeping...") 
        time.sleep(200)
        os.system('cls')
        