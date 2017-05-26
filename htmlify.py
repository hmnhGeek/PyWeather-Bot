
def htmlify(info, unit):
    if unit == 'K':
        units = "Default, Kelvin"
    elif unit == 'F':
        units = "Imperial, Fahrenheit"
    else:
        units = "Metric, Celsius"
    
    try:
        name = info['name']
    except:
        name = " --- "
    
    try:
        visibility = info['visibility']
    except:
        visibility = " --- "
        
    try:
        country = info['sys']['country']
    except:
        country = " --- "

    
    try:

        main = info['weather'][0]['main']
        description = info['weather'][0]['description']
    except:
        main = " --- "
        description = " --- "
    
    try:

        latitude = info['coord']['lat']
        longitude = info['coord']['lon']
    except:
        latitude = " --- "
        longitude = " --- "

    try:
        pressure = info['main']['pressure']
        temp_min = info['main']['temp_min']
        temp_max = info['main']['temp_max']
        temp = info['main']['temp']
        humidity = info['main']['humidity']
    except:
        pressure = " --- "
        temp_min = " --- "
        temp_max = " --- "
        temp = " --- "
        humidity = " --- " 

    try:

        windspeed = str(info['wind']['speed'])
    except:
        windspeed = " --- "

    htmlified = '''

<!doctype html>
<head>
<title> City Weather Result </title>
<link rel="stylesheet" media="screen" href = "{{ url_for('static', filename='bootstrap.min.css') }}">
</head>

<body>
<center><h2> Hey, I got you the results for the place %s.</h2><br>
Units used:        %s<br><br><br>
Name of the place: %s<br>
Visibility:        %s<br>
Country:           %s<br>
Weather:           %s<br>
Description:       %s<br>
Latitude:          %s<br>
Longitude:         %s<br>
Pressure:          %s<br>
Min. Temperature:  %s<br>
Max. Temperature:  %s<br>
Temperature:       %s<br>
Humidity:          %s<br>
Wind Speed:        %s<br>
<br>
<br>

Want to find temperature of any other place?? Click <a href = "http://127.0.0.1:5000">here</a> if you want to do so.

</center>

</body>
</html>

''' % (name, units, name, visibility, country, main, description, latitude, longitude, pressure, temp_min, temp_max, temp, humidity, windspeed)

    return htmlified
