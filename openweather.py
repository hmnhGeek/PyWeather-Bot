import json, urllib2, htmlify

APP_ID = "a453aba51ddf22fa57d0973144ce1e41"

def city(name, by = None, units = 'K'):

    if units == 'K':
        if by == None:
            url = "http://api.openweathermap.org/data/2.5/weather?q="+name+"&APPID="+APP_ID

        elif by == 'zip':
            data = name.split(',')
            pin = [i for i in data[0] if i != ' ']
            pin = ''.join(pin)
            country = [i for i in data[1] if i != ' ']
            country = ''.join(country)
            url = "http://api.openweathermap.org/data/2.5/weather?zip="+pin+','+country+"&APPID="+APP_ID
            
        elif by == 'coords':
            data = name.split(',')
            
            lat = float(data[0])
            lon = float(data[1])
            
            url = "http://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&APPID="+APP_ID

    elif units == 'F':
        
        if by == None:
            url = "http://api.openweathermap.org/data/2.5/weather?q="+name+"&units=imperial"+"&APPID="+APP_ID

        elif by == 'zip':
            data = name.split(',')
            pin = [i for i in data[0] if i != ' ']
            pin = ''.join(pin)
            country = [i for i in data[1] if i != ' ']
            country = ''.join(country)
            url = "http://api.openweathermap.org/data/2.5/weather?zip="+pin+','+country+"&units=imperial"+"&APPID="+APP_ID
            
        elif by == 'coords':
            data = name.split(',')
            
            lat = float(data[0])
            lon = float(data[1])
            
            url = "http://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&units=imperial"+"&APPID="+APP_ID

    elif units == 'C':
        
        if by == None:
            url = "http://api.openweathermap.org/data/2.5/weather?q="+name+"&units=metric"+"&APPID="+APP_ID

        elif by == 'zip':
            data = name.split(',')
            pin = [i for i in data[0] if i != ' ']
            pin = ''.join(pin)
            country = [i for i in data[1] if i != ' ']
            country = ''.join(country)
            url = "http://api.openweathermap.org/data/2.5/weather?zip="+pin+','+country+"&units=metric"+"&APPID="+APP_ID
            
        elif by == 'coords':
            data = name.split(',')
            
            lat = float(data[0])
            lon = float(data[1])
            
            url = "http://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&units=metric"+"&APPID="+APP_ID    

    weatherbot = urllib2.urlopen(url)
    info = json.load(weatherbot)
    return htmlify.htmlify(info, units)
