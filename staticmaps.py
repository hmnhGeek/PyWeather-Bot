
API_KEY = "AIzaSyDwwLrlJDaqCtQa2CMBKtWOC6IkYli_vl4"

def convertforurl(string):

    words = string.split(' ')

    string = ''
    for i in range(len(words)):
        if i != len(words) - 1:
            string += (words[i]+'+')
        else:
            string += words[i]

    return string

def add_key(url):
    url+="&key="+API_KEY

    return url

def add_param(url, param, value):
    param = convertforurl(param)
    value = convertforurl(value)
    url+="&"+param+"="+value
    return url

def get_url(place, zoom = 10, height = 500, width = 500):

    
    place = convertforurl(place)
    
    url = "https://maps.googleapis.com/maps/api/staticmap?center="+place

    url = add_param(url, 'size', str(height)+'x'+str(width))
    url = add_param(url, 'zoom', str(zoom))
    url = add_key(url)

    return url

    
    
