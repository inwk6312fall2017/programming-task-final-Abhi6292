from weather import Weather
weather = Weather()



# Lookup via location name.

location = weather.lookup_by_location('dublin')
condition = location.condition()
hi=0
lo=0
a=0
b=0
for forecasts in location.forecast():
  # print(forecasts)
   hi=int(forecasts['high'])

   if hi > b:
      b=hi
      print('high :',b)

for forecasts in location.forecast():
    lo = int(forecasts['low'])
    print(lo)
    if lo < a:
        a = lo
        print('low :', a)

for forecasts in location.forecast():
    while forecasts['text'] == 'Rain':
        print('It might rain on :', forecasts['day'])
        print(condition['text'])
        break
#print ('condition:',forecasts['text'],end=" ")     print ("on",forecasts['date'])
 
 #    print ((forecasts['high']))
 #    print ('Low:',forecasts['low'])
