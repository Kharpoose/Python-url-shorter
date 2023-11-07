import requests

def shorten_link(full_link, link_name):
    API_KEY = '29c9223931d7abfdb9e033c41120505b75c8b'
    BASE_URL = 'https://cutt.ly/api/api.php'
    
    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()
    
    print('')
    
    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        
        print('Title:', title)
        print('Link:', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)
        
link = input('Enter your looong link: ')
name = input('Give your short link to name: ')

shorten_link(link, name)         
    
