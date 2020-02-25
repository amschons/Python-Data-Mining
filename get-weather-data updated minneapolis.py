from bs4 import BeautifulSoup
import urllib, urllib.request, time
from urllib.request import Request, urlopen

# Create/open a file called wunder.txt (which will be a comma-delimited file)
f = open('minneapolis-data.txt', 'w')

 
# Iterate through year, month, and day
for y in range(2018, 2019):
  for m in range(1, 13):
    for d in range(1, 32):
 
      # Check if leap year
      if y%400 == 0:
        leap = True
      elif y%100 == 0:
        leap = False
      elif y%4 == 0:
        leap = True
      else:
        leap = False
 
      # Check if already gone through month
      if (m == 2 and leap and d > 29):
        continue
      elif (m == 2 and d > 28):
        continue
      elif (m in [4, 6, 9, 10] and d > 30):
        continue
 
      # Open wunderground.com url
      url = "https://www.wunderground.com/history/daily/us/mn/fort-snelling/KMSP/date"+str(y)+ "/" + str(m) + "/" + str(d)
      req = Request(url, headers={'User-Agent': 'Chrome/63.0.3239.132'})
      page = urlopen(req).read()


      soup = BeautifulSoup(page, "html.parser")
      # AvgDayTemp = soup.body.nobr.b.string
      AvgDayTemp = soup.findAll(attrs={"class":"nobr"})[5].span.string
      
      # Get MaxTemp from page
      MaxTemp = spans[6].span.string

      #Get MinTemp from page
      MinTemp = spans[13].span.string

      #Get precip from page
      precip = spans[9].span.string

	  	#Get dewpoint from page
      dewpoint = spans[8].span.string
      
 
      # Format month for timestamp
      if len(str(m)) < 2:
        mStamp = '0' + str(m)
      else:
        mStamp = str(m)
 
      # Format day for timestamp
      if len(str(d)) < 2:
        dStamp = '0' + str(d)
      else:
        dStamp = str(d)
 
      # Build timestamp
      timestamp = str(y) + mStamp + dStamp
 
      # Write timestamp and temperature to file
      f.write(timestamp + ',' + dayTemp + '\n')

      #pause code for a few seconds
      time.sleep(3)
 
# Done getting data! Close file.
f.close()
