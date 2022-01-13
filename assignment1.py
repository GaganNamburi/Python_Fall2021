#Gagan Namburi, AA502, Python Assignment 1

#Packages.
import requests
import sys
from datetime import datetime
from datetime import timedelta
from datetime import date
from statistics import mean
import csv
import pandas as pd

#Locations list.
locs = ["Anchorage, Alaska", "Chennai, India", "Jiangbei, China", "Kathmandu, Nepal", "Kothagudem, India", "Lima, Peru", "Manhasset, New York", "Mexico City, Mexico", "Nanaimo, Canada", "Peterhead, Scotland", "Polevskoy, Russia", "Round Rock, Texas", "Seoul, South Korea", "Solihull, England", "Tel Aviv, Israel"]

#Create dataframe.
df = pd.DataFrame(columns = ["City", "Min 1", "Max 1", "Min 2", "Max 2", "Min 3", "Max 3", "Min 4", "Max 4", "Min 5", "Max 5", "Min Avg", "Max Avg"])

#API key to access OpenWeather API.
api_key = '0ecea89a10a153974569ba5a21346e33'

#Loop through the locations list and access the weather forecasts.
for l in locs:
  
  #Access the URL for OpenWeather API.
  URL = 'https://api.openweathermap.org/data/2.5/forecast?'
  URL = URL + 'q=' + l + '&units=metric&appid=' + api_key
  response = requests.get( URL )
  
  #Check if the response will fail.
  if response.status_code != 200:      # Failure?
    print( 'Error:', response.status_code )
    sys.exit( 0 )
  
  #The data from the response.
  data = response.json()
  
  #Today's date based off system time.
  cur_dt = date.today()

  #Check for if the date in the data is the same day as the system time.
  for i in range(0, len(data['list'])):
    dt_str = data['list'][i]['dt_txt']
    dt_tm = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    tz_offset = data['city']['timezone']
    dt_tm = dt_tm + timedelta(seconds=tz_offset)

    if cur_dt.day == dt_tm.day:
      pass
    else:
      start_point = i
      break

  #Creation of the list of indices corresponding to day starts. It will always be a length of 5.
  day_starts = []

  #The start_point variable from before is added to the list as day 1's start point.
  day_starts.append(start_point)
  
  #Check if the start_point is 0 or not
  if start_point == 0:
    for i in range(start_point, len(data['list'])):
      start_day = datetime.strptime(data['list'][start_point]['dt_txt'], '%Y-%m-%d %H:%M:%S') + timedelta(seconds=tz_offset)
      dt_day_next = datetime.strptime(data['list'][i]['dt_txt'], '%Y-%m-%d %H:%M:%S') + timedelta(seconds=tz_offset)

      #Compare days until the next day is reached (usually less than 8 units away).
      if start_day.day != dt_day_next.day:
        start_point2 = i
        break

    #Add second start point if start_point is 0 and the start is in the middle of the next day.
    day_starts.append(start_point2)

    while start_point2 + 8 < len(data['list']) and len(day_starts) < 5:
      start_point2 += 8
      day_starts.append(start_point2)

    #API call list splicing corresponding for each day to get only pertinent data per day.
    day_1_data = data['list'][day_starts[0]:day_starts[1]]
    day_2_data = data['list'][day_starts[1]:day_starts[2]]
    day_3_data = data['list'][day_starts[2]:day_starts[3]]
    day_4_data = data['list'][day_starts[3]:day_starts[4]]
    day_5_data = data['list'][day_starts[4]:day_starts[4] + 8]
  else:
    #Add start points to day_starts by incrementing by 8 if the start_point is not 0 and
    #stopping just before 40 because that index value is invalid.
    while start_point + 8 < len(data['list']):
      start_point += 8
      day_starts.append(start_point)

    #API call list splicing corresponding for each day to get only pertinent data per day.
    day_1_data = data['list'][day_starts[0]:day_starts[1]]
    day_2_data = data['list'][day_starts[1]:day_starts[2]]
    day_3_data = data['list'][day_starts[2]:day_starts[3]]
    day_4_data = data['list'][day_starts[3]:day_starts[4]]
    day_5_data = data['list'][day_starts[4]:len(data['list'])]

  #Day 1 min-max lists.
  day_1_mins = []
  day_1_maxs = []

  #Day 2 min-max lists.
  day_2_mins = []
  day_2_maxs = []

  #Day 3 min-max lists.
  day_3_mins = []
  day_3_maxs = []

  #Day 4 min-max lists.
  day_4_mins = []
  day_4_maxs = []

  #Day 5 min-max lists.
  day_5_mins = []
  day_5_maxs = []
  
  #Days 1-4 will always be a full length of 8, so they can be looped through together.
  for a,b,c,d in zip(day_1_data, day_2_data, day_3_data, day_4_data):
    #Day 1 min and max.
    day_1_mins.append(a['main']['temp_min'])
    day_1_maxs.append(a['main']['temp_max'])

    #Day 2 min and max.
    day_2_mins.append(b['main']['temp_min'])
    day_2_maxs.append(b['main']['temp_max'])

    #Day 3 min and max.
    day_3_mins.append(c['main']['temp_min'])
    day_3_maxs.append(c['main']['temp_max'])

    #Day 4 min and max.
    day_4_mins.append(d['main']['temp_min'])
    day_4_maxs.append(d['main']['temp_max'])

  #Day 5 may not be a full length of 8, so it is looped through separately.
  for e in day_5_data:
    #Day 5 min and max.
    day_5_mins.append(e['main']['temp_min'])
    day_5_maxs.append(e['main']['temp_max'])
      
  #Get mins and maxs for the mins and maxs respectively.

  #Day 1.
  day_1_min = round(min(day_1_mins), 2)
  day_1_max = round(max(day_1_maxs), 2)

  #Day 2.
  day_2_min = round(min(day_2_mins), 2)
  day_2_max = round(max(day_2_maxs), 2)

  #Day 3.
  day_3_min = round(min(day_3_mins), 2)
  day_3_max = round(max(day_3_maxs), 2)

  #Day 4.
  day_4_min = round(min(day_4_mins), 2)
  day_4_max = round(max(day_4_maxs), 2)

  #Day 5.
  day_5_min = round(min(day_5_mins), 2)
  day_5_max = round(max(day_5_maxs), 2)

  #Get the min average and max average.
  min_avg = round(mean([day_1_min, day_2_min, day_3_min, day_4_min, day_5_min]), 2)
  max_avg = round(mean([day_1_max, day_2_max, day_3_max, day_4_max, day_5_max]), 2)
  
  #Append the data to a new dataframe column.
  df = df.append({"City" : l, "Min 1" : day_1_min, "Max 1" : day_1_max, "Min 2" : day_2_min, "Max 2" : day_2_max, "Min 3" : day_3_min, "Max 3" : day_3_max, "Min 4" : day_4_min, "Max 4" : day_4_max, "Min 5" : day_5_min, "Max 5" : day_5_max, "Min Avg" : min_avg, "Max Avg" : max_avg}, ignore_index=True)

#Convert dataframe to csv file.
df.to_csv("temp.csv", index=False, mode="w+", float_format="%.2f")