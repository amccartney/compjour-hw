import mandrill
import requests
from tokens import *
from base64 import b64encode

imgurl = 'http://python.mfamt.org/files/images/pics/hoover-tower-fog.jpg'
img = requests.get(imgurl)
imgdata = b64encode(img.content)

#import mandrill
MANDRILL_API_KEY = MY_API_KEY
mandrill_client = mandrill.Mandrill(MANDRILL_API_KEY)
message = {
	'from_email': 'anmccartney@gmail.com',
	'from_name': 'Allison McCartney',
	'to': [{
		'email': 'allison.n.mccartney@gmail.com',
		'name': 'Allison',
		'type': 'to'
	}],
	'subject': 'Sending you a pic of the Stanford campus',
	'html': "<p>Here's a photo of the <a href='https://www.flickr.com/photos/zokuga/15138926354/'>Stanford campus</a></p>",
	'attachments': [{
		'name': 'hoover-tower-fog.jpg',
		'type': 'image/jpeg',
		'content': imgdata
	}]
}
result = mandrill_client.messages.send(message = message)
print (result)
