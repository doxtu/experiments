'''
    Functions for downloading and emailing catgirls

    Catgirls are binary representation of images of drawings of girls that look like cats. We can save and send these binary representations to people - yay.
'''
import os

LOGIN = os.environ.get('DANBOORU_USERNAME')
API_KEY = os.environ.get('DANBOORU_API_KEY')
URL = 'https://danbooru.donmai.us'
ACTION = '/posts.json'
TAGS = 'cat_girl%20large_breasts'
PARAMS = f'?login={LOGIN}&api_key={API_KEY}&tags={TAGS}&random=true&limit=1'

def get_random_catgirl_json(save=False):
    from requests import get
    import json

    ret = {}

    try:
        r = get(f'{URL}{ACTION}{PARAMS}')
        if r.status_code == 200:
            ret = r.json()
        else:
            print(r.json())
            ret = [{'error':'failed to get catgirl'}]
    except Exception as e:
        ret = [{'error':'failed to get catgirl'}]

    if save == True:
        with open('output-catgirl.json', 'w') as f:
           f.write(json.dumps(ret)) 

    return ret

def get_random_catgirl():
    '''Get a binary representation of an image from Danbooru's API for a random catgirl'''
    
    from requests import get

    ret = b''

    data = get_random_catgirl_json()

    if 'error' in data[0]:
        return print(data[0]['error'])

    # The catgirl is not worthy unless she has a large file size ;)
    if 'large_file_url' not in data[0]: return get_random_catgirl()
    image_url = data[0]['large_file_url']
    ir = get(image_url)

    if ir.status_code == 200:
        ret = ir.content
    else:
        print('failed to get catgirl image')

    return ret


def dl_random_catgirl(random_catgirl=None):
    if random_catgirl == None:
        random_catgirl = get_random_catgirl()

    import json
    
    from random import randrange
    filename = str(randrange(1,99999999))

    from PIL import Image
    from io import BytesIO
    with Image.open(BytesIO(random_catgirl)) as i:
        file_type = i.format
        i.save(f'{filename}.{file_type}')


FROM_ADDRESS = os.environ.get('NICK_EMAIL')
TO_ADDRESS = os.environ.get('KIM_EMAIL')

def email_random_catgirl(random_catgirl=None, save=False, recipients=[FROM_ADDRESS, TO_ADDRESS]):
    import smtplib, os, random
    from email.message import EmailMessage

    if random_catgirl == None:
        random_catgirl = get_random_catgirl()

    if save == True:
        dl_random_catgirl(random_catgirl)

    PASSWORD = os.environ.get('G_PASSWORD')

    message = EmailMessage()
    message['Subject'] = 'Catgirl of the day!'
    message['From'] = FROM_ADDRESS
    message['To'] = recipients
    message.set_content('''Cute catgirl is here to brighten up your day!''')

    message.add_attachment(random_catgirl, maintype='image', subtype='jpg', filename=f'random-catgirl-{str(random.randint(1000000000,9999999999))}.jpg')
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(FROM_ADDRESS,PASSWORD)
        smtp.send_message(message)
