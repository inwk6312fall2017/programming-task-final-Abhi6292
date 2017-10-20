from weather import Weather
weather = Weather()



# Lookup via location name.

location = weather.lookup_by_location('dublin')
condition = location.condition()
#print (condition['text'])

# Get weather forecasts for the upcoming days.

for forecasts in location.forecast():
  #  print(forecasts)
    while forecasts['text'] == 'Rain':
        print('It might rain on :',forecasts['day'])
        print(condition['text'])
        break
    """
    print ('condition:',forecasts['text'],end=" ")
    print ("on",forecasts['date'])

    print ((forecasts['high']))
    print ('Low:',forecasts['low'])
    """