"""
File name - ackerman_class_project.py
Name - Tanner Ackerman
Date - 1/20/2022
Professor - Allen Voelcker
University - Bellevue
Assignment - Class Project - Week 7 Rough Draft
Description - This is a program that will get a list of weather statisitcs from the webservice openweathermap.org only requiring a user input of either a city name or zipcode.
"""

# appid = cc3a52490a266a947ec67d513ee04251
# after browsing the openweather website information on how to use their api the following url has been decided based off of US metrics and the weather information I would logically like to include for this assignment.
# the url that is going to be used is "https://api.openweathermap.org/data/2.5/weather?{zip=*****} or {q="state"},us&units=imperial&appid={above stated appid}

# since we will be making a request to a web page we will use "import requests" to access the requests library. "import time" is to allow the program to use time.sleep() function to allow for a better flow of the program.

import requests
import time



# Welcome the user to the program. Also inform the user of the statistics that will be included in the program's search.

print("Welcome to the Weather Data Program!!")
print()
time.sleep(2)
print("The following weather statistics will be provided on each search:\n1.Longitude\n2.Latitude\n3.Weather description\n4.Current temperature\n5.Feel temperature\n6.Low temperature\n7.High temperature\n8.Atmospheric Pressure\n9.Humidity\n10.Wind speed")
print()
time.sleep(5)
print("Lets get started!!")
print()
time.sleep(2)



# created a function to search request via zip code, adjusting URL accordingly for openweathermap.org.

def search_by_zipcode():
  zip_code = int(input("Type in the zipcode you would like to search the weather for - "))
  print()
  response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=3cfb3ef209130bbc71e87da6c0f41baf".format(zip_code))
  data_retrieved = response.json()
  print()
  print("Searching weather for your zip code...")
  print()
  time.sleep(3)
  print_data(data_retrieved)
   
# using an "if" statement within the function to allow the user search again, if desired. It just either starts the main() function or exits it if the user chooses not to continue. 

  choice = input("Would you like to search for more weather details?? Yes/Y or No/N: ")
  print()
  if choice == "Yes" or choice == "Y":
    main()
  if choice == "No" or choice == "N":
    print()
    print("Well okay then! Suit yourself, we will see you next time!!")
    exit()



# created a function to search request via city name, adjusting URL accordingly for openweather.org. Almost identical to function created for zipcode, except user inputs a string instead of an integer.

def search_by_city():
  user_city = input("Type the name of your city you would like to search the weather for - ")
  print()
  responce = requests.get("https://api.openweathermap.org/data/2.5/weather?q={},us&appid=cc3a52490a266a947ec67d513ee04251&units=imperial".format(user_city))   
  data_retrieved = responce.json()
  print()
  print("Searching weather for your city...")
  print()
  time.sleep(3)
  print_data(data_retrieved)
  print()

# again using an "if" statement to allow the user to continue searching, if desired. It is needed in both functions "search_by_zipcode()" and "search_by_city()" to acheive this for both user options.

  choice = input("Would you like to search for more weather details?? Yes/Y or No/N: ")
  print()
  if choice == "Yes" or choice == "Y":
    main()
  if choice == "No" or choice == "N":
    print()
    print("Well okay then! Suit yourself, we will see you next time!!")
    exit()



# This function is responsible for getting the specific weather statistics out of the json webpage and printing it in the order stated at the beginning of the program. I used the url from above in a browser to see the layout of the json page and to pick which information to include.

def print_data(statistics):
    longitude = statistics["coord"]["lon"]
    latitude = statistics["coord"]["lat"]
    weather_description = statistics["weather"][0]["description"]
    current_temperature = statistics["main"]["temp"]
    feels_like = statistics["main"]["feels_like"]
    low_temp = statistics["main"]["temp_min"]
    high_temp = statistics["main"]["temp_max"]
    atmospheric_pressure = statistics["main"]["pressure"]
    humidity = statistics["main"]["humidity"]
    wind_speed = statistics["wind"]["speed"]
    
    print("The longitude is {}".format(longitude))
    print("The latitude is {}".format(latitude))
    print("Weather description is '{}'".format(weather_description))
    print("Current temperature is {} degrees fahrenheit".format(current_temperature))
    print("It feels like {} degrees fahrenheit".format(feels_like))
    print("The low temperature is {} degrees fahrenheit".format(low_temp))
    print("The high temperature is {} degrees fahrenheit".format(high_temp))
    print("The atmospheric pressure is {}mb or millibars".format(atmospheric_pressure))
    print("The humidity is {}%".format(humidity))
    print("The Wind Speed is {}mph or miles per hour".format(wind_speed))
    print()


# Below is the main() function. As required it includes try blocks to notify the user of an established connection with exceptions to allow user to try again, it also notifies the user of invalid input attempts and lets them try again. 

def main():
 
  while True:
    search_choice = input("Please type 'Zip' to search weather by zip code or 'City' to search weather by city name - ")
        
    if search_choice == "zip" or search_choice == "Zip":
      try:
        print()
        print("Connecting now...")
        time.sleep(3)
        print("Connection has been established!!")
        print()
        search_by_zipcode()

      except Exception:
        print("Invalid entry, please try again and enter a valid zip code!")
        print()
        search_by_zipcode()
        
    if search_choice == "city" or search_choice == "City":
      try:
        print()
        print("Connecting now...")
        time.sleep(3)
        print("Connection has been established!!")
        print()
        search_by_city()

      except Exception:
        print("Invalid entry, please try again and enter a valid city name!")
        print()
        search_by_city()
    
    else:
      print("Unfortunatley, what you entered was invalid.")
      print("Give it another shot!")

main()






"""The only issue I ran into is, the program crashes if the user fails an attempt at entering a specific city name or zipcode more than twice. I couldn't figure out the right logic for either the main() fucntion or the two search functions to fix this. I know that is where the problem lies.""" 