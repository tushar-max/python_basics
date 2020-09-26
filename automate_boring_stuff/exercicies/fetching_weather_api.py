"""
Overall, the program does the following:

Reads the requested location from the command line
Downloads JSON weather data from OpenWeatherMap.org
Converts the string of JSON data to a Python data structure
Prints the weather for today and the next two days

So the code will need to do the following:

Join strings in sys.argv to get the location.
Call requests.get() to download the weather data.
Call json.loads() to convert the JSON data to a Python data structure.
Print the weather forecast.
"""

APPID = 'YOUR_APPID_HERE'

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

"""
Command line arguments are split on spaces. The command line argument San Francisco, US would make sys.argv hold ['getOpenWeather.py', 'San', 'Francisco,', 'US']. Therefore, call the join() method to join all the strings except for the first in sys.argv. Store this joined string in a variable named location.
"""

# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location,
APPID)
response = requests.get(url)
# The requests.get() call returns a Response object, you can check for errors by calling raise_for_status(). If no exception is raised, the downloaded text will be in response.text.
response.raise_for_status()

# Uncomment to see the raw JSON text:
#print(response.text)    

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

