import requests
import scrython

with open("randomMultiIds.txt") as ids:
	content = ids.readlines()

content = [x.strip() for x in content]

count = 1
for c in content:
	card = scrython.cards.Multiverse(id=c)
	img_data = requests.get(card.image_uris(1, 'art_crop')).content
	img_name = 'images_multiverse/' + str(count) +'_'+ c.strip() + '.jpg'
	with open(img_name, 'wb') as handler:
		handler.write(img_data)
	print(str(count) + ' - ' + c)
	count += 1
